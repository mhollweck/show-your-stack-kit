<!-- show-your-stack:observer:CAPTURE_ID:start -->
## Show Your Stack observer · CAPTURE_ID

I opted into local-only process observation of eligible nonconfidential work.
State: CAPTURE_DIR/capture-state.json
Journal: CAPTURE_DIR/journal.md
Privacy policy: CAPTURE_DIR/kit/PRIVACY.md
Pinned kit: CAPTURE_DIR/kit/ (commit KIT_COMMIT)
Window: START_UTC inclusive to END_UTC exclusive.

At a task boundary, check minimal policy/scope fields before reading the
journal. Require privacy_policy local-only-v1, sharing disabled, approved
nonconfidential canonical roots, valid UTC dates, and a known current time.
Missing fields, an unresolved root, or a time before START_UTC mean no logging.
Never read outside approved roots or follow a symlink into an excluded root.
Aliases and legacy read/sharing consent do not grant access.

Only eligible personal/public nonconfidential sessions may contribute.
If the session contains employer/client confidential context, stop capture
there without copying, paraphrasing, or summarizing that context. Do not read
company history, code, private configs, business/customer data, or secrets to
learn the workflow. Give the clean-session/generic-notes path when appropriate.
An observer rule is not a secret detector or a guarantee of private processing.
Claude's provider processes inputs even when capture files are stored locally.

Inside the window, write one short process-only sample per participating
eligible session as directed in the journal. Use synthetic sample IDs, neutral
aliases, public tool names, generic steps, bounded counts, and unknowns. Never
record real names, source paths, commands, code, actual prompts, raw session
IDs, internal identifiers, or business/task details. Do not inspect histories,
install hooks, transmit progress, or announce routine entries. Update a sample
only when new eligible evidence warrants it; do not claim complete coverage.

At/after END_UTC stop logging. At a suitable task boundary in an eligible
session, resume the privacy-aware pinned EXTRACT.md from saved state. Explain
once that the window ended and analysis can finish locally; record the notice.
Do not claim a draft is ready before creating it. Do not broaden read scope.
If extraction is in progress, resume its saved phase. If complete-local or
cancelled, do nothing. Missing kit/state means explain the issue once; do not
fetch or execute a different legacy version to continue automatically.

Never upload, submit, publish, fork, open a PR, send a message, or synchronize
capture data or final files, even with saved sharing approval or RETURN_REPO.
The next session may be after the end date; this rule does not wake an idle
agent or promise exact-time execution. The participant can stop capture at any
time and choose what generated local files to keep or delete.
<!-- show-your-stack:observer:CAPTURE_ID:end -->
