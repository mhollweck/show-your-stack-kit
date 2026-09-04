import argparse
from contextlib import ExitStack, redirect_stderr, redirect_stdout
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

SPEC = importlib.util.spec_from_file_location("stack_kit", Path(__file__).resolve().parents[1] / "scripts/stack_kit.py")
kit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(kit)
FIXTURE = Path(__file__).parent / "fixtures/stack-submission.md"
SCRIPT = kit.KIT_ROOT / "scripts/stack_kit.py"


class NeverInspect:
    """Any old code accessing arguments, paths, or a GitHub client must fail."""
    def __getattribute__(self, name):
        raise AssertionError("Disabled export inspected its inputs")

    def __bool__(self):
        raise AssertionError("Disabled export evaluated a GitHub client")


class KitTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.capture = Path(self.temp.name)
        self.bundle = self.capture / "approved"
        self.bundle.mkdir()
        self.profile = FIXTURE.read_bytes()
        self.deck = kit.render(self.profile)
        (self.bundle / "stack-submission.md").write_bytes(self.profile)
        (self.bundle / "presentation.html").write_bytes(self.deck)

    def add_legacy_approval(self):
        files = {name: hashlib.sha256((self.bundle / name).read_bytes()).hexdigest()
                 for name in ("stack-submission.md", "presentation.html")}
        consent = {"schema_version": 1, "submission_id": "01e8e1bc-4c31-42b6-a858-2b9aba7b9c3a",
                   "subject_github": "sample-friend", "author_approved": True,
                   "approved_at": "2026-01-01T00:00:00Z", "kit_commit": "a" * 40,
                   "kit_worktree_dirty": False, "return_repo": "mhollweck/sys-intake-example01",
                   "audience": "community", "community_repo": "mhollweck/example-community",
                   "community_visibility": "private", "public": False, "file_sha256": files}
        (self.bundle / "consent.json").write_text(json.dumps(consent))
        (self.capture / "submission-state.json").write_text(json.dumps({"return_repo": consent["return_repo"], "submission_id": consent["submission_id"]}))
        return consent

    def assert_export_disabled(self, callback):
        """Fail if capture access, a subprocess, or a network socket is attempted."""
        with ExitStack() as stack:
            guards = [
                stack.enter_context(patch.object(kit, 'read_file', side_effect=AssertionError('read_file called'))),
                stack.enter_context(patch.object(Path, 'read_bytes', side_effect=AssertionError('file read attempted'))),
                stack.enter_context(patch.object(Path, 'write_bytes', side_effect=AssertionError('file write attempted'))),
                stack.enter_context(patch.object(Path, 'open', side_effect=AssertionError('file open attempted'))),
                stack.enter_context(patch.object(Path, 'exists', side_effect=AssertionError('path inspected'))),
                stack.enter_context(patch.object(subprocess, 'run', side_effect=AssertionError('subprocess attempted'))),
                stack.enter_context(patch.object(socket, 'create_connection', side_effect=AssertionError('connection attempted'))),
                stack.enter_context(patch.object(socket, 'socket', side_effect=AssertionError('socket attempted'))),
            ]
            with self.assertRaisesRegex(kit.KitError, 'local-only'):
                callback()
            for guard in guards:
                guard.assert_not_called()

    def test_renderer_offline_keyboard_notes_and_evidence(self):
        self.assertEqual(self.deck, kit.render(self.profile))
        text = self.deck.decode()
        self.assertEqual(text.count('<section class="slide"'), 12)
        self.assertIn("What this is based on", text)
        self.assertIn("Limitation: These were selected sources", text)
        self.assertIn("ArrowRight", text)
        self.assertIn("@media print", text)
        self.assertNotIn("src=", text)
        self.assertNotIn("http://", text)
        self.assertNotIn("https://", text)

    def test_renderer_escapes_every_dynamic_context(self):
        profile = kit.parse_profile(self.profile)
        attack = '</script><script>alert("test")</script><img src=x onerror=alert(1)>'
        for key in ["name", "oneLiner", *kit.SECTIONS]:
            profile[key] = attack
        profile["tags"], profile["gems"] = [attack], [attack]
        profile["slides"] = {"harness": {"type": "roster", "why": attack, "notes": attack,
                                        "items": [{"label": attack, "sub": attack, "meta": attack}]}}
        profile["evidence"] = {"mode": attack, "summary": attack, "sources": [attack], "limitations": [attack]}
        source = ('---\n' + kit.yaml.safe_dump(profile) + '---\n').encode()
        output = kit.render(source).decode()
        self.assertEqual(output.count('<script>'), 1)
        self.assertNotIn('<img', output)
        self.assertIn('&lt;img', output)

    def test_duplicate_yaml_and_object_construction_rejected(self):
        for bad in (b'---\nname: A\nname: B\n---\n', b'---\nname: !!python/object/apply:os.system [echo unsafe]\n---\n'):
            with self.subTest(bad=bad), self.assertRaises(kit.KitError):
                kit.render(bad)

    def test_empty_gems_do_not_invent_advice(self):
        profile = kit.parse_profile(self.profile)
        profile['gems'] = []
        output = kit.render(('---\n' + kit.yaml.safe_dump(profile) + '---\n').encode())
        self.assertNotIn(b'Try this in your own stack', output)

    def test_slide_density_limits_ask_for_shorter_content(self):
        profile = kit.parse_profile(self.profile)
        profile['slides']['harness']['nodes'][0]['label'] = 'One two three four five'
        with self.assertRaisesRegex(kit.KitError, 'shorten labels'):
            kit.render(('---\n' + kit.yaml.safe_dump(profile) + '---\n').encode())

    def test_renderer_rejects_symlink_and_oversized_input(self):
        path = self.capture / 'linked-profile.md'
        path.symlink_to(FIXTURE)
        with self.assertRaises(kit.KitError):
            kit.read_file(path)
        path = self.capture / 'oversized-profile.md'
        path.write_bytes(b'x' * (kit.MAX_FILE_BYTES + 1))
        with self.assertRaises(kit.KitError):
            kit.read_file(path)

    def test_render_cli_reads_only_explicit_profile_and_writes_local_output(self):
        output = self.capture / 'local-presentation.html'
        source = self.bundle / 'stack-submission.md'
        with patch.object(kit, 'read_file', wraps=kit.read_file) as reader, \
                patch.object(subprocess, 'run', side_effect=AssertionError('subprocess attempted')) as process, \
                patch.object(socket, 'socket', side_effect=AssertionError('network attempted')) as network, \
                redirect_stdout(io.StringIO()):
            self.assertEqual(kit.main(['render', str(source), '--output', str(output)]), 0)
        reader.assert_called_once_with(source)
        process.assert_not_called()
        network.assert_not_called()
        self.assertEqual(output.read_bytes(), self.deck)
        self.assertFalse((self.bundle / 'consent.json').exists())

    def test_approve_rejects_before_inspecting_arguments(self):
        self.assert_export_disabled(lambda: kit.approve(NeverInspect()))
        self.assert_export_disabled(lambda: kit.approve())

    def test_submit_rejects_before_inspecting_bundle_or_client(self):
        self.assert_export_disabled(lambda: kit.submit(NeverInspect(), NeverInspect()))
        self.assert_export_disabled(lambda: kit.submit())

    def test_old_valid_consent_and_resume_state_cannot_enable_submission(self):
        self.add_legacy_approval()
        before = {path: path.read_bytes() for path in self.capture.rglob('*') if path.is_file()}
        gh = Mock()
        self.assert_export_disabled(lambda: kit.submit(self.bundle, gh))
        self.assert_export_disabled(lambda: kit.submit(self.bundle, gh))
        gh.assert_not_called()
        self.assertFalse(gh.mock_calls)
        self.assertEqual(before, {path: path.read_bytes() for path in self.capture.rglob('*') if path.is_file()})
        self.assertFalse((self.capture / 'receipt.json').exists())

    def test_invalid_or_missing_bundles_are_rejected_by_policy_first(self):
        (self.bundle / 'consent.json').write_text('invalid-json')
        for bundle in (self.bundle, self.capture / 'does-not-exist', None):
            with self.subTest(bundle=bundle):
                self.assert_export_disabled(lambda: kit.submit(bundle, Mock()))

    def test_approve_never_creates_or_updates_sharing_consent(self):
        args = argparse.Namespace(bundle=self.bundle, author_approved=True,
                                  github='sample-friend', return_repo='mhollweck/sys-intake-example01',
                                  audience='community', community_repo='mhollweck/example-community',
                                  community_visibility='public', allow_uncommitted_kit=True)
        self.assert_export_disabled(lambda: kit.approve(args))
        self.assertFalse((self.bundle / 'consent.json').exists())
        self.add_legacy_approval()
        before = (self.bundle / 'consent.json').read_bytes()
        self.assert_export_disabled(lambda: kit.approve(args))
        self.assertEqual((self.bundle / 'consent.json').read_bytes(), before)

    def test_legacy_cli_flags_cannot_override_local_only_policy(self):
        self.add_legacy_approval()
        for command in ('approve', 'submit'):
            for flags in ([], ['--help'], ['--bundle', str(self.bundle), '--author-approved',
                                        '--return-repo', 'mhollweck/sys-intake-example01',
                                        '--audience', 'community', '--community-visibility', 'public',
                                        '--allow-uncommitted-kit', '--force']):
                stderr = io.StringIO()
                with self.subTest(command=command, flags=flags), \
                        patch.object(kit, 'read_file', side_effect=AssertionError('capture read')) as reader, \
                        patch.object(subprocess, 'run', side_effect=AssertionError('auth/network')) as process, \
                        patch.object(socket, 'socket', side_effect=AssertionError('network')) as network, \
                        redirect_stderr(stderr):
                    self.assertEqual(kit.main([command, *flags]), 1)
                    self.assertIn('local-only', stderr.getvalue())
                    reader.assert_not_called()
                    process.assert_not_called()
                    network.assert_not_called()

    def test_executable_export_commands_reject_even_without_yaml_dependency(self):
        # -S omits site-packages. Export commands must hit policy before PyYAML.
        for command in ('approve', 'submit'):
            result = subprocess.run([sys.executable, '-S', str(SCRIPT), command,
                                     '--bundle', str(self.capture / 'missing'),
                                     '--allow-uncommitted-kit'], text=True, capture_output=True)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(result.stdout, '')
            self.assertIn('local-only', result.stderr)
            self.assertNotIn('Install dependencies', result.stderr)

    def test_old_hook_is_silent_and_inert(self):
        result = subprocess.run(['sh', str(kit.KIT_ROOT / 'observer-hook.sh')],
                                input='{"prompt":"synthetic-private-value","cwd":"/private"}',
                                text=True, capture_output=True, env={'HOME': self.temp.name})
        self.assertEqual((result.returncode, result.stdout, result.stderr), (0, '', ''))
        self.assertFalse((self.capture / 'show-your-stack').exists())


if __name__ == '__main__':
    unittest.main()
