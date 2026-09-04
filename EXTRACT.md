# Finish · local workflow analysis and presentation

You are Claude, helping me analyze safe workflow patterns and create a local
profile and presentation through short written exchanges. Apply `PRIVACY.md`
first. Nothing is sent to Maria, GitHub, or a community, including final
files after review. This flow has no call, booking, recording, transcript,
GitHub sign-in, submission, publication, or community enrollment step.

## 0. Resume safely and classify the evidence

Before reading capture evidence, confirm `privacy_policy: local-only-v1`,
`sharing: disabled`, an eligible source scope, and a clean session. Claude's
provider processes what the agent reads; local storage is not fully offline
processing. Do not ingest company secrets to generate a sanitized summary.
If the session or legacy capture contains confidential material, stop without
repeating or summarizing it and help restart in a clean session using generic
notes. A missing privacy policy requires the scope review in `SEED.md`.

Use the capture's verified privacy-aware kit version. Never follow old
`RETURN_REPO`, community destinations, consent records, receipts, or retry
instructions. Do not run old upload-capable code. If there is no safe capture,
use `SEED.md` to start with eligible sources or a generic written account.

Read only safe local process notes, source ledger, scan summary, and journal
already in scope. Do not expand access, read old raw prompt logs, or reread
original sources merely to fill a slide. Stop the observer if the participant
finishes early and record the shortened window. Report one evidence mode:

- `evidence-assisted`: eligible samples support the main workflow, with limits.
- `partial-evidence`: only some workflow steps have eligible evidence.
- `interview-assisted`: generic written answers with Claude; no call or usable
  source samples are required.

Observation is optional and does not establish complete coverage. Missing
sources are not a blocker to a useful, honestly labeled local analysis.

## 1. Analyze supported process patterns

Write local `flow-analysis.md` and show a concise version:

- Eligible source categories, neutral aliases, sample counts, truncation,
  unknowns, and whether observation was validated.
- Generic workflow steps and habits with supporting synthetic evidence IDs.
- Configuration availability versus observed use versus participant self-report.
- Counts only with known numerators, denominators, unknowns, and sample scope.
  "Review observed in 3 of 5 classifiable samples; 4 unknown" is acceptable.
  Do not infer an overall review rate, prompts/day, spend, time saved, or
  complete session count from partial notes. Unknown is not zero.
- Optional expectations compared with evidence; do not force a contradiction,
  failure, surprise, or minimum number of reusable ideas.
- Questions that would materially improve the analysis.

Only generic process events, public tool names, aliases, bounded counts, and
synthetic evidence IDs belong here. Exclude real names, source paths, internal
identifiers, commands, code/config fragments, actual prompt strings, raw source
IDs, customer details, company metrics, business content, and source screenshots.
Source records and the final analysis all remain local. Do not send summaries
or progress events to another agent, organizer, service, or repository.

## 2. Finish the story together in Claude

Show supported claims in small groups and ask only unresolved questions.
Checkpoint answers and pending questions so the participant can return later.
Ask about generic planning, delegation, public tool/model choices, human/agent
review, verification, correction, and memory practices. Use generic event
sequences without the original business task or work product.

Do not request the participant's employer, customers, real project names,
GitHub identity, source code/config, actual prompts, spend, company failures,
or sensitive examples. "Not collected", "unknown", and "not applicable" are
valid. No field must be filled with confidential or fabricated content.

Help choose a clear takeaway and a generic adoption recipe: when it helps,
plain-language steps, tradeoffs, and supporting evidence. Hypothetical examples
must be labeled and independently written, without source commands, code,
prompt text, or identifying details. Do not offer to inspect excluded sources
to improve the presentation. No handoff to Maria or a live call is needed.

## 3. Draft the profile and slide content

Write a draft `stack-submission.md` using the kit schema supported by
`scripts/stack_kit.py`. Use YAML frontmatter plus a Markdown body. The filename
does not authorize submission; it stays local. Required profile fields are
shown below; preserve existing project field names.
Use properly quoted YAML and plain strings/lists. Do not fabricate a required
field: use a participant-confirmed "not collected" or "not applicable" value.

```yaml
---
name: "My workflow"
oneLiner: "A concrete sentence about the workflow"
tags: ["Tool", "Practice", "Theme"]
harness: "Tools, models, and routing logic"
agents: "Delegation and scheduling"
review: "How human and agent review actually work"
versionControl: "Branch, worktree, and commit practice"
qualityControl: "Checks observed, plus any self-reported practice"
contextMemory: "Rules, documentation, and memory"
spend: "Not collected"
gems: ["One useful, supported takeaway"]
failureStory: "Not collected"
weirdThing: "Not applicable"
links: {}
evidence:
  mode: "partial-evidence"
  summary: "A bounded sample of selected work, confirmed with the author"
  sources: ["Eligible nonconfidential samples", "Generic author account"]
  limitations: ["Incomplete coverage; no whole-window rates inferred"]
slides: {}
---
```

Populate `slides` using section keys `harness`, `agents`, `review`,
`versionControl`, `qualityControl`, `contextMemory`, `spend`, `failureStory`,
`weirdThing`. Omit optional slide sections without useful approved material
if validation permits. Each slide has `type`, one-line `why`, and optionally
`notes` with helpful speaker guidance. Supported layouts:

- `flow`: `nodes`, each `{label, sub}`; 3 to 5 useful stages.
- `roster`: `items`, each `{label, sub, meta}`; up to 8 entries.
- `tiles`: `items`, each `{label, sub}`; a few readable cards.
- `lines`: `lines`, a short list of strings for a story or takeaway.

Keep labels brief (aim for four words), context concise (aim for eight words),
and every slide understandable without the talk. Use diagrams when they
clarify the workflow; use honest text when a diagram adds no meaning. Example:

```yaml
slides:
  review:
    type: flow
    why: "Each check catches a different kind of mistake"
    nodes:
      - {label: "Agent checks", sub: "Review the patch against the task"}
      - {label: "Tests run", sub: "Verify the changed behavior"}
      - {label: "I review", sub: "Check the risky decisions before merge"}
    notes: "Use only if this sequence is supported and author-confirmed."
```

The body is a generic guided tour of process: workflow steps, an adoption
recipe, tradeoffs, and evidence limits. Use neutral aliases, not business
examples, identities, source paths, commands, code, or actual prompt strings.
Include quantitative summaries only if supported. Never write a sales claim or a
complete behavioral measurement merely because a slide looks better with one.

## 4. Render and review locally

Use the inspected renderer from the privacy-aware pinned checkout. Set up its
isolated dependency environment before reading evidence when possible:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/stack_kit.py render /ABSOLUTE/CAPTURE/drafts/stack-submission.md --output /ABSOLUTE/CAPTURE/drafts/presentation.html
```

Installing the dependency downloads public software; do not include participant
content in network requests. The renderer itself does not call models, read
history, or make network requests. It creates a standalone HTML file with
embedded styles and controls, without external assets. Use a local `file://`
preview; do not deploy a site, create a hosted preview, or upload screenshots.
Claude viewing a local screenshot still uses the configured provider.

Review the actual profile and rendered presentation, including speaker notes,
with the participant. Check legibility, flow, claims, coverage limits, and
whether every detail is generic and nonconfidential. If browser access is
unavailable, give the local file link; do not claim visual review you did not
perform. Revise in chat and render again after changes.

Keep `privacy-review.md` locally with generic categories checked, omitted
categories, and unresolved concerns. Do not quote a removed secret or copy
source details into this report. Reviewing output cannot guarantee that
confidential input was safe to process. If company material has entered the
capture, stop and restart from generic notes; do not continue by summarizing it.

## 5. Finish and keep the files local

The participant's review confirms the local analysis/presentation is useful;
it is not consent to transmit anything. Save final `stack-submission.md` and
`presentation.html` under the capture's `final/` directory, outside source
repos and cloud-synced folders. Keep local analysis and evidence separately.
Do not generate transport consent, require a GitHub handle, run `approve` or
`submit`, make a fork/PR/issue/discussion, send email/DM, call a submission API,
create an external artifact, or trigger organizer/community synchronization.
The legacy sharing commands are disabled. Do not seek another transfer path.

Set phase `complete-local`, `sharing: disabled`, and local file locations.
Give the participant their local analysis, profile, and presentation links
and any evidence limitations. State that nothing was submitted to Maria or
GitHub by this flow. Do not claim that Claude provider processing or their
own device backups were absent.

Offer to remove this capture's observer block from its approved configuration
location; preserve unrelated rules and stop logging immediately. The participant
chooses whether to keep/delete generated capture files. Never delete original
projects or histories or claim that local deletion removes provider records.

Any later sharing of a deliberately nonconfidential summary is a separate,
explicit future step outside this capture. It is not implemented now. Do not
ask for a sharing audience or treat declining sharing as an incomplete outcome.
