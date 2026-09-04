# Start: discover the full stack, then make one useful document

Help the participant understand their development stack and how it optimizes
their flow. Include personally owned unpublished tooling, scripts, wrappers,
custom agents/skills, schedules, and integrations alongside familiar products.
The output is one local stack-analysis.md, rich enough to support a later
community entry and presentation. No call, upload, or stack changes.

## 0. Explain privacy, pin the kit, and use existing knowledge

Before new source access explain: "Your analysis stays with you. I can study
your own unpublished tooling within the scope you approve. Company/client
secrets and credentials remain excluded. Claude's configured provider still
processes what I read, so local storage is not offline AI."

Read PRIVACY.md. Use relevant existing authorized context as discovery leads;
a blank session is not mandatory. Label recalled facts CTX and check their
currency. Do not reload all history or company memories just because the
agent can access them. If safe context cannot be separated from confidential
business material, use participant descriptions or a neutral session. Never
copy the confidential material into an analysis or ask to redact it afterward.

Resolve the public kit's main to one full Git commit, refetch these instructions
and PRIVACY.md from that SHA, and use that snapshot for all kit files. Fetch
DOSSIER.md, SCAN.md, and EXTRACT.md from the same commit. Read scripts before
executing any. Downloading public instructions does not permit uploading
participant data. No GitHub identity or private account access is needed.

For a new capture, select ~/show-your-stack/<capture-id>/ outside source repos
and cloud-sync folders. Confirm the local location, without changing backup
settings or promising backups are absent. Keep the kit in a pinned checkout
under kit/. Save minimal capture-state.json and the evolving stack-analysis.md.
An optional journal is supporting evidence, not another final deliverable.

For an existing capture, first read minimal policy/scope state and identify
which capture if ambiguous. Reuse eligible evidence and the person's prior
answers without restarting. Current no-send instructions override old return
settings. A change from the overly restrictive public/generic-only analysis
requires confirming any newly added read scope, not treating private tools
as company secrets or silently expanding access. Excluded legacy company
content is not evidence to ingest or summarize.

## 1. Agree source scope in one useful exchange

Show a preliminary candidate list from authorized context. Ask for the missing
scope, not a complete inventory the agent could discover itself:

- Which 1 to 3 representative projects and personally owned tooling folders
  may I inspect? Include unpublished scripts/repos, local tools, and workflow
  glue that would not show up in a public dependency list.
- May I read selected docs/entrypoints, safe manifest/config fields, aliases,
  agent/skill/hook definitions, scheduler/CI and infrastructure definitions,
  eligible design/task-planning artifacts, and small relevant
  functions or interfaces in that scope? Do not request secret values, whole
  settings dumps, or broad home-directory discovery.
- Which already relevant memory/context can I use, and which selected past
  sessions or safe exports may I sample? History reads need their own scope.
  Default to 30 days, up to 20 eligible samples, initially 2,000 characters of
  relevant process material per sample. Skip mixed company logs.
- Are personally owned tool names okay in the local document, or should I use
  aliases? Necessary exact paths/interfaces belong in its local-only appendix.

Record exclusions and optional declined sources. Private/unpublished ownership
is not public-sharing permission; it is also not a reason to ignore a relevant
owned tool. Company/client confidential material and credentials are excluded
before reading, including sensitive metadata. If a source cannot safely be
separated, ask for a behavior description. Reuse approved scope; ask only for
a real expansion or a material configuration change.

Save state atomically: capture/kit revision, privacy_policy local-only-v1,
sharing disabled, analysis_format stack-dossier-v1, phase, approved source
roots/categories, contextual leads, exclusions, history sample bounds, tool
name/alias preferences, document/review state, and observation details if used.
No return repo, GitHub identity, or transmission consent is required.

## 2. Discover and connect the stack

Follow SCAN.md. Update the same stack-analysis.md using DOSSIER.md: coverage
map, full tool inventory, deep cards for material custom tools, invocation and
handoff relationships, actual task traces, evidence appendix, and questions.

A bare tool list is insufficient. Identify triggers, inputs, outputs, routing,
human approval points, failure/retry behavior, and what the tool replaced when
known. Explain how private glue changes the workflow. Separate recalled,
configured, observed, participant-confirmed, experimental, and retired items.
Never run discovered scripts or alter the person's stack to understand it.

## 3. Finish now or observe specific unresolved behavior

Show the coverage and remaining questions. Finish now if enough evidence
supports the main story, even if honest unknowns remain. Offer 7 days, 14 days,
or a positive custom whole-day window only when it could resolve useful gaps
such as cadence, bypasses, review behavior, or whether a prototype is adopted.
Do not delay a sufficient analysis or require the participant to prove a
surprise, failure, or productivity benefit. Generic descriptions remain useful
when source access is declined; label them self-report.

For observation, record which questions it should answer, exact UTC start,
exclusive end, timezone, and approved roots. Validate parseable dates,
start < end, and future end. Invalid/missing time, before start, and at/after
end mean no logging. An observation sample cannot establish whole-window rates.
The participant can finish early or change the window explicitly.

## 4. Optional observer setup

Inspect how this host/version loads rules using official host documentation
and actual configuration. Prefer project-scoped rules; a global rule must
enforce the same approved scope. Show the exact path and proposed change,
get configuration approval, back up existing content, and update only this
capture's unique block. Fill all template placeholders from state.

Use observer-rule.md and journal-template.md from the pinned kit. The observer
may name eligible personal tools or aliases and describe invocation/handoff
behavior, but it never copies raw prompts, code, secrets, or company content.
Do not install the old hook, a raw collector, upload job, or daemon. Rules
provide samples, not a reliable census. Where rules cannot work, use requested
end-of-task summaries in eligible sessions.

Validate with approved non-sensitive tasks: an eligible session yields a
useful note and an excluded root yields none. Keep setup/tests out of ordinary
usage claims. Do not say the observer works before checking it. If unsafe
context cannot be separated, pause capture rather than copying it.

## 5. Continue and finish with the participant

For finish now, go directly to EXTRACT.md. Otherwise save phase observe and
explain local location, scoped questions, dates, tested status, and resume
instruction. At expiry the next eligible session can resume the document;
there is no exact-time callback or idle-agent wakeup. Keep notes local.

EXTRACT.md finishes stack-analysis.md, verifies the important mechanics with
the person, and prepares candidate community/deck sections inside that one
document. Asset rendering is later, if requested. Nothing is uploaded or
sent, and old consent/RETURN_REPO values do not change that boundary.
