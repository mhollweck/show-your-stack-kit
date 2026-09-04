# Privacy boundary · local-only capture

This policy applies before source discovery, scanning, observation, analysis,
and presentation creation. It also applies to resumed and legacy captures.

**Do not send participant material to Maria, GitHub, any community, or another
destination. Keep the capture, analysis, profile, and presentation on the
participant's device. Do not bring company secrets into this flow.**

Private or unpublished does not automatically mean company-confidential.
The participant's own scripts, plugins, agents, functions, configurations,
and internal tools can be central to their stack. Include them when the
participant owns or controls the material, authorizes the relevant scope,
and is allowed to process it with their configured Claude provider.

## Local files and Claude processing are different

Claude's configured provider processes inputs, including content the agent
reads through tools. A local file path does not make that processing offline.
The kit cannot promise that all processing stays on the device, that provider
logging is absent, or that every secret will be detected. If strictly on-device
processing is required, stop: this Claude workflow does not satisfy it.
See [Claude Code data usage](https://code.claude.com/docs/en/data-usage).

Downloading the public kit, its declared dependency, or relevant public tool
documentation uses the network. Do not include participant content, private
tool names, source paths, internal identifiers, or other private details in
search queries or external requests. Do not send capture data to analytics,
remote tools, hosted previews, external screenshot services, or git remotes.
Local screenshots opened by Claude are still subject to provider processing.
The generated presentation itself has no external assets or network calls.

## Use relevant knowledge without expanding access

A fresh blank session is not mandatory. Existing relevant memory or conversation
context can help identify the participant's own tooling and workflow when that
use is authorized and the facts are nonconfidential. Do not search every memory
store or reload unrelated conversations merely because memory exists. A useful
existing fact can guide a focused question without opening another source.

Keep the following distinct:

- **Existing authorized context:** a remembered tool or workflow is a lead.
  Label it as context-recalled until current use is confirmed or observed.
- **New source access:** opening a file, configuration, function, or past session
  requires the agreed source scope. Access in an earlier task or a tool's
  presence in memory does not grant new read access for this capture.
- **Public research:** public documentation can explain a named public tool's
  capabilities. It does not establish the participant's setup or actual use.
  Do not use private details to search for documentation about unpublished tools.
- **Observed behavior or participant confirmation:** these can establish use
  within their stated scope. Distinguish self-report from directly observed
  behavior. Installed, configured, available, or remembered never means used.

Do not copy or incorporate company/client confidential business material that
happens to be in context, and do not broaden access to it. Ask for a generic
participant-written description of the process instead of summarizing the
confidential content. If safe facts cannot be separated confidently, pause
capture and offer a neutral, clean session using those generic descriptions.
Do not demand a restart when the current relevant context is already safe.
A restart does not undo earlier provider processing or erase provider records.

## Agree scope for owned tools before reading more

Eligible sources include explicitly selected personally owned unpublished
projects, scripts, skills, plugins, agent definitions, safe configurations,
function interfaces, public projects, and relevant nonconfidential AI sessions.
Personal ownership alone does not make a source safe: it can still contain
credentials, employer/client material, or customer data that must be excluded.
If ownership or processing authority is unclear, use a generic description.

Start from the participant's description and safe metadata for the selected
scope. A metadata preview may show neutral aliases, file categories, and sizes,
without exposing sensitive names or paths. Review what a more detailed read
would add. Within the approved scope, narrow reads of personally owned scripts,
nonsecret configuration fields, function signatures, or tool interfaces may
explain triggers, inputs, outputs, dependencies, and workflow connections.
Do not dump complete settings, broad source trees, environment variables, or
whole histories. Do not execute unknown scripts or functions to inspect them.

Metadata is not a safety certificate. Folder names, file paths, branch names,
commit messages, and config values can themselves be confidential. Do not scan
a forbidden source just to list its metadata. If a candidate mixes eligible
personal tooling with excluded content, select a safely separable part or use
the participant's own generic account. Do not read it first and rely on later
redaction. Existing scope approval persists for eligible reads; an expansion
needs approval, without repeated prompts for the same unchanged scope.

## Exclude company secrets and credentials

Never request, inspect, copy, or record:

- Employer/client confidential implementation, code, business documents,
  prompts, agent rules, configurations, conversations, or company histories.
- Customer/personal records, company/customer identifiers, internal business
  URLs, proprietary metrics, pricing, roadmaps, incidents, security details,
  unreleased company features, or confidential task/work-product details.
- Credentials, `.env` files, keys/tokens, credential stores, billing records,
  browser/password-manager data, unrelated messages, recordings, or transcripts.

A participant's personally owned unpublished tool name or local repo name is
not excluded merely because it is private. A name that reveals an employer,
client, customer, or confidential business context remains excluded. The
participant's consent cannot make employer/client secrets eligible. Do not ask
them to paste confidential excerpts or whole secret-bearing settings into chat.

An observer rule is not a secret detector. Observe only the authorized safe
parts of eligible work. If confidential material appears, stop capturing that
material without copying or paraphrasing it, and use generic participant
process descriptions for any gaps. If the safe scope cannot be maintained,
pause observation and use a clean context. Do not treat ordinary agent access
to company work as permission to add it to this capture.

## Keep useful local detail, minimize unnecessary content

The local analysis can name personally owned tools when the participant wants
that detail retained. It may map how scripts, functions, agents, and manual
steps connect, with generic descriptions of triggers, inputs, outputs, and
observed use. Use neutral aliases where names would expose excluded information
or where the participant prefers them. Public tool names may be used normally.

Keep the observation journal concise: process events, eligible tool names or
aliases, synthetic evidence IDs, bounded counts, and explicit unknowns. Do not
copy raw prompts, logs, work products, customer/business content, credentials,
or source screenshots into it. Do not equate a configured integration with an
observed workflow or infer a whole-window metric from partial samples.

Minimal source paths, safe invocation/interface details, or short personally
owned nonconfidential examples can go in a **local-only appendix inside stack-analysis.md** when
needed to explain or revisit the stack, within the approved scope. Do not copy
whole implementations or settings simply to inventory a tool. Keep source paths
and implementation details out of the presentation by default. State, ledger,
appendix, analysis, and presentation all stay local; none is a share bundle.

Choose a capture folder outside source repositories and cloud-synced folders
and confirm the location with the participant. Do not change backup/sync
settings or promise they are disabled. The participant chooses which generated
local files to keep or delete. Do not delete original tools or histories.

## Finishing is not permission to send

Completing or approving the analysis document means it is ready for the participant to
use locally. Do not upload, submit, publish, fork, open a PR/issue/discussion,
email, DM, invite an account, call a submission API, or retry old transfers.
Do not discover GitHub identity or request sign-in for capture. Ignore legacy
`RETURN_REPO`, community destinations, consent files, and upload receipts as
authority to send. Do not reuse an old upload-capable script to bypass the
current disabled commands. Check a legacy capture's scope against this policy
before reading its evidence; do not ingest old confidential material to sanitize it.

Save `privacy_policy: local-only-v1` and `sharing: disabled` in capture state.
Missing policy fields require a scope review before reading evidence. Older
instructions and approval records do not authorize sending. A safe existing
capture may continue under the reviewed scope; a capture containing company
secrets must not supply evidence for this analysis. Use generic participant
descriptions instead and leave excluded original material untouched.

Any future sharing needs a separate, explicit step outside this flow. The
author would choose a deliberately nonconfidential summary and decide which
owned tool names to keep or alias; private paths and implementation details
must never be shared automatically. This future step is not implemented here.
The kit does not guarantee anonymity or secret-free output; privacy depends
on source selection, appropriate processing authority, and minimizing detail.
