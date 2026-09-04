# Show Your Stack · local process journal

capture_id: CAPTURE_ID
kit_commit: KIT_COMMIT
privacy_policy: local-only-v1
sharing: disabled
start_utc_inclusive: START_UTC
end_utc_exclusive: END_UTC
timezone: TIMEZONE
coverage: sampled eligible sessions; not a complete activity log
observer_validation: unverified

This journal stays on the participant's device. It is not sent to Maria,
GitHub, or a community. Claude's provider still processes material it reads.
Do not include employer/client confidential context, even as a paraphrase.
The scope/config paths are held separately in minimal local capture state.

## Before logging

Require the current privacy policy, confirmed nonconfidential session, approved
canonical roots, and valid UTC window. Write nothing before start, at/after
end, with unknown time or invalid dates, outside eligible roots, or after the
participant stops capture. If confidential context appears, stop without
writing a summary. Never inspect histories or company sources through this rule.

Use a meaningful task checkpoint; do not pretend it proves a session ended.
Only the coordinating agent writes local entries. Avoid distributing evidence
to extra agents or services for this capture. Assign a synthetic local sample
ID, not the host's real session identifier. Update the same sample only when
new eligible evidence warrants it. Do not collapse unrelated sessions or
count repeated references twice. Concurrent sessions may write separate local
sample files for a later safe merge; never overwrite another session's notes.

## What may be recorded

Generic process events, publicly known tool names, neutral aliases, synthetic
evidence IDs, bounded counts, and unknowns. Do not record real names, paths,
commands, code/config fragments, actual prompt strings, source screenshots,
raw session IDs, internal tool identifiers, customer/personal data, business
content, or original task descriptions. Use "a check ran; result passed",
without the command, work product, issue identifier, or company context.

## Entry format

### OBS-001 · YYYY-MM-DD · project-1
- sample_key: locally generated synthetic ID
- coverage: partial checkpoint or supported completed-session summary; gaps
- workflow: generic observed steps, with unfinished steps marked unknown
- framing: generic request shape; visible request count or unknown
- delegation: observed delegation pattern; public tool/model name if known
- review: evidence of human/agent review; unknown if unseen
- verification: generic check type and observed result; requested-only marked
- version_control: generic branch/worktree/commit practice or unknown
- correction: generic revision loop if observed; no business/task details

Counts apply only to these samples. Do not infer a person reviewed code from
an agent's diff command. Do not infer full-window rates, total sessions, time
saved, spend, company performance, or other unsupported metrics.

## Check-ins and finish

At a natural eligible task boundary, an optional check-in can ask whether the
sample missed a generic workflow habit. At most one per seven-day period;
record that state without repeating the journal. Do not require failure stories.

At/after the exclusive end, stop logging. On the next eligible session, resume
local analysis with the privacy-aware pinned EXTRACT.md and give the one-time
notice. No active session means no instant reminder. Final review is local;
no upload, return, identity lookup, or publication happens at completion.
The participant can stop early and choose whether to keep/delete local notes.

## Expectations (optional self-report)

<Generic expectations about planning, delegation, and review, if provided.>

## Scope aliases

<Neutral project-1 aliases only; no actual source paths or names.>

## Baseline

<Generic safe configuration evidence IDs; unknowns explicit.>

## Entries
