# Privacy boundary · local-only capture

This policy applies before source discovery, scanning, observation, analysis,
and presentation creation. It also applies to resumed and legacy captures.

**Do not send participant material to Maria, GitHub, any community, or another
destination. Keep the capture, analysis, profile, and presentation on the
participant's device. Do not bring company secrets into this flow.**

## Local files and Claude processing are different

Claude's configured provider processes inputs, including content the agent
reads through tools. A local file path does not make that processing offline.
The kit cannot promise that all processing stays on the device, that provider
logging is absent, or that every secret will be detected. If strictly on-device
processing is required, stop: this Claude workflow does not satisfy it.
See [Claude Code data usage](https://code.claude.com/docs/en/data-usage).

Only the public kit and its declared renderer dependency need downloading.
Do not put participant data in requests, search queries, analytics, remote
tools, hosted previews, screenshots sent to external services, or git history.
Local screenshots opened by Claude are still subject to provider processing.
The generated presentation itself has no external assets or network calls.

## Keep confidential sources out before reading

Start in a fresh session in a neutral directory outside company/client repos.
Do not resume a company conversation or load its project instructions for
this task. Global instructions can also contain confidential information;
if the session already contains confidential material, stop this capture
without repeating or summarizing it. Give a clean-restart instruction using
generic participant-written process notes. A restart does not erase earlier
provider processing, and the agent must not claim it does.

Eligible sources are explicitly selected nonconfidential personal/public
projects and personal/public AI sessions that the participant is allowed to
process with their provider. The simplest path is generic written notes about
how they plan, delegate, review, test, and correct work. No source access is
required to produce a useful, honestly labeled analysis.

Never request, discover, read, copy, or log:

- Employer/client confidential code, documents, prompts, agent rules, private
  configurations, internal conversations, or company session histories.
- Company/customer names or identifiers, personal/customer records, internal
  URLs, private repo names, business metrics, pricing, roadmaps, incidents,
  security details, unreleased features, or confidential task descriptions.
- Credentials, `.env` files, keys/tokens, credential stores, billing records,
  browser/password-manager data, unrelated messages, recordings, or transcripts.

Metadata can also be confidential. Folder names, file paths, commit messages,
branch names, and configuration values are not automatically safe. A broad
project allowlist or the participant's willingness to share does not make
company-confidential sources eligible. Skip uncertain sources. Do not read
them first and rely on a redaction pass afterward. Do not ask the participant
to paste confidential excerpts as a workaround.

Observation is allowed only in eligible nonconfidential sessions. An observer
is not a secret detector. If confidential context appears, stop capture for
that session; do not write a summary of it, even a paraphrase. Existing work
with Claude outside this kit is not a source of permission for this kit.

## Record the process, not the work product

Journal and analysis contain generic workflow events, publicly known tool
names, synthetic evidence IDs, bounded counts, and explicit unknowns. Use
neutral aliases such as `project-1`. Do not include real names, source paths,
commands, code/config fragments, actual prompt strings, screenshots of source
material, raw session IDs, business content, or internal tool identifiers.
For example, record "a test ran after an edit; outcome passed", without the
command, code, product, issue identifier, or customer context.

Only minimal local capture state may contain the canonical paths necessary
to enforce an approved nonconfidential scope. Keep paths out of journals,
analysis, profiles, slides, notes, and review reports. Keep the capture outside
source repositories and cloud-synced folders; confirm the chosen location with
the participant. Do not change their backup/sync settings or promise they are
disabled. Keep or delete local capture files according to their choice.

## Finishing is not permission to send

Completing or approving a profile means it is ready for the participant to
use locally. Do not upload, submit, publish, fork, open a PR/issue/discussion,
email, DM, invite an account, call a submission API, or retry old transfers.
Do not discover GitHub identity or request sign-in for capture. Ignore legacy
`RETURN_REPO`, community destinations, consent files, and upload receipts as
authority to send. Do not reuse an old upload-capable script to bypass the
current disabled commands. Do not fetch a legacy capture's evidence until its
scope has been checked against this policy.

Save `privacy_policy: local-only-v1` and `sharing: disabled` in capture state.
Missing policy fields mean the capture needs a safe-scope review before any
evidence is read. Older instructions and approval records never override this
policy. If an old capture may contain company material, leave it untouched
and start a new capture from generic notes; do not ingest it to sanitize it.

Any future sharing of a separately prepared nonconfidential summary needs a
new, explicit step outside this flow. It is not implemented here. The kit does
not guarantee anonymity or secret-free output; privacy depends first on
keeping confidential sources and context out of the analysis.
