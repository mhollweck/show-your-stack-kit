# Local rendering and analysis

The agent follows `PRIVACY.md`, `SEED.md`, `SCAN.md`, and `EXTRACT.md` to help
the participant analyze eligible nonconfidential workflows. Capture, analysis,
profile, and presentation stay on their device. No files or progress messages
are returned to Maria, GitHub, or a community. GitHub account setup is not needed.
The legacy `approve` and `submit` commands are disabled; do not use an older
kit checkout, saved consent, or another transport to bypass this policy.

Claude's configured provider processes its inputs. Local files are not a
promise of fully offline analysis. Do not read company secrets, company prompt
histories, confidential employer/client material, or customer data at all.
Use a fresh session outside company projects and generic notes when uncertain.
See [PRIVACY.md](PRIVACY.md) for the complete source and processing boundary.

## Render a standalone local presentation

Requires Python 3.10+. Use the inspected renderer from a verified privacy-aware
kit checkout outside source repositories and cloud-synced folders. Install
its single YAML dependency before reading evidence when possible:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Dependency installation downloads public software. Do not include participant
content in network requests. The renderer itself reads only the specified
local profile, writes the chosen HTML output, and does not read history,
call models, make network requests, send telemetry, or start background work.

```sh
.venv/bin/python scripts/stack_kit.py render \
  ~/show-your-stack/CAPTURE_ID/drafts/stack-submission.md \
  --output ~/show-your-stack/CAPTURE_ID/drafts/presentation.html
```

`stack-submission.md` is retained as a compatible profile filename; it does not
mean the file will be submitted. After review, save the profile and HTML in the
capture's `final/` directory. Do not create transport consent or run any return
command. Finishing the local presentation is the completed outcome.

The renderer uses safe YAML loading with duplicate-key rejection and escapes
profile text, labels, evidence, and notes. The standalone HTML embeds styles
and controls, has no external fonts/scripts/assets, and uses a restrictive
content policy. Use a local browser preview. Arrow keys navigate, N toggles
speaker notes, and Print saves a landscape PDF. Do not create a hosted preview
or use an external presentation/conversion service. Claude viewing a local
screenshot is still subject to provider processing.

Review every slide and its notes. Only generic process events, public tool
names, synthetic evidence IDs, bounded counts, and unknowns belong in the
profile or presentation. Never include real names, source paths, commands,
actual prompt strings, code/config fragments, internal identifiers, company
metrics, or business/customer details. A renderer validates formatting; it
cannot guarantee the content contains no secrets.

Missing section slides use their profile text. Use "Not collected", "unknown",
or "not applicable" when appropriate. `gems: []` avoids inventing advice.
Optional evidence metadata uses:

```yaml
evidence:
  mode: partial-evidence
  summary: "A bounded set of eligible process notes and author confirmations."
  sources: ["Selected nonconfidential workflow samples", "Generic author account"]
  limitations: ["Selected evidence cannot establish whole-window totals."]
```

Slide specs accept a `notes` string. Existing profile keys and layout types
remain compatible. Consult `EXTRACT.md` for a minimal profile and layout limits.

## Verification

```sh
.venv/bin/python -m unittest discover -s tests -v
```

Verify that rendering still works and legacy approval/submission commands stop
before network access. Use synthetic data; never test secret handling by reading
actual company secrets. The old prompt hook remains disabled. Automated checks
cannot prove an agent always follows instructions or detects confidential context;
a real participant pilot must check scope, generic-only notes, and local finish.

Later sharing of a deliberately nonconfidential summary would be a separate,
explicit future flow. No GitHub handoff, fork contribution, invitation, or
community publication is implemented as part of this local capture.
