# Show Your Stack · targeted local observations

capture_id: CAPTURE_ID
kit_commit: KIT_COMMIT
privacy_policy: local-only-v1
sharing: disabled
analysis_format: stack-dossier-v1
start_utc_inclusive: START_UTC
end_utc_exclusive: END_UTC
timezone: TIMEZONE
coverage: sampled eligible events; not a complete activity log
observer_validation: unverified

This optional journal supports the one working document, stack-analysis.md.
It is not a second final deliverable. Both stay with the participant; neither
is sent to Maria, GitHub, or a community. Claude's provider processes what it
reads, so local storage is not fully offline processing.

## Questions this observation should answer

<Copy the specific unresolved questions chosen in SEED.md, with stable Q-IDs,
relevant tool IDs, existing evidence, and what an observable answer would be.
For example: Q-1: Is tool-2's evidence handoff consumed by a human before merge?
A configured review gate does not answer that; an eligible observed human
review or a separately labeled participant confirmation might.>

Do not collect an indiscriminate diary. A useful sample resolves or narrows a
question about cadence, an invocation condition, a missing handoff, a human
gate, bypass behavior, failure/recovery, or whether a tool is actually adopted.
Do not manufacture failures, execute a discovered tool, or alter the workflow
for a sample.

## Before logging

Require the current privacy policy, approved source/name scope, a saved question,
known current time, and a valid UTC window. Write nothing before start, at/after
end, with invalid dates, outside eligible roots, after stop/cancellation, or once
the document is complete-local. Never inspect old histories through this rule.

Personally owned private/unpublished tools are eligible within scope. Use their
actual names locally if approved, otherwise the participant's aliases. Existing
relevant authorized context can interpret a safe event; do not force a blank
session or reread sources unnecessarily. Recalled context and configuration
are leads, not observed events or proof of current usage.

Company/client confidential material and credentials remain excluded. Do not
copy or paraphrase confidential business content from a mixed session. If safe
process facts cannot be separated confidently, pause capture and ask for a
participant description or use a neutral session. Label descriptions SELF;
they do not become OBS just because they were supplied during the window.

## Keep bounded, useful evidence

Only the coordinating agent writes local entries. Do not distribute capture
evidence to additional agents/services. Assign synthetic sample IDs and reuse
the dossier's canonical tool IDs so aliases do not become duplicate tools.
Do not use raw host session IDs or copy logs. Prefer one compact sample per
participating session; distinct events answering different questions may have
separate samples. Update an existing sample when more eligible evidence arrives
instead of counting the same event twice. Concurrent sessions may use separate
local sample files for a safe merge; never overwrite another session's notes.

Aim for 100 to 250 words per sample, with only fields relevant to its questions.
Keep a meaningful checkpoint rather than pretending it proves a session ended.
Preserve actual invocation conditions, input/output categories, decision rules,
handoffs, human control, and observed results. A useful note says which tool
prepared which evidence category, what blocked progress, who acted next, and
what remains unknown; "uses tools and runs checks" loses the mechanism.

Do not record raw prompts, code/config fragments, command payloads, source
screenshots, logs, credentials, customer/business details, or confidential work
products. Safe owned-tool names, public tool names, tool IDs, artifact categories,
and plain-language interface behavior may be recorded. Necessary private paths
or exact owned interfaces belong only in stack-analysis.md's local evidence
appendix, within approved scope, rather than copied throughout the journal.

## Entry format

### OBS-001 · YYYY-MM-DD · approved project/tool alias or local name
- sample_key: locally generated synthetic ID
- questions: Q-ID(s) this sample helps answer
- tool_ids: canonical IDs from the working stack map
- coverage: partial checkpoint or supported completed-session summary; what
  was visible, where the trace ends, and missing context
- trigger_and_actor: who/what started the action and its actual condition;
  mark requested/configured behavior separately
- input_decision_output: input category -> tool/routing/decision -> observed
  artifact or state change; no private payloads or copied implementation
- handoff_and_human_gate: downstream consumer, approval/override point, and
  evidence of action; ready-for-review does not mean reviewed
- failure_recovery_or_bypass: what stopped/changed, retry/fallback/manual
  intervention observed, or unknown/not applicable
- result_for_question: answered, narrowed, or still unknown; evidence and
  any competing explanation

Do not fill unseen fields with assumptions. No incident needs to occur merely
to fill the failure field. Keep participant explanations marked SELF and prior
context/configuration marked CTX/CFG when interpreting an OBS event.

For any count, state numerator, denominator, unknowns, and sampling scope.
Do not infer a person reviewed from an agent's diff command, deployment from
a passing test, or complete cadence from a few samples. Time/cost benefits
remain self-report without supporting measurements. No company performance
metrics or unsupported whole-window rates belong in the record.

## Check-ins, integration, and finish

At an eligible natural boundary, ask a targeted follow-up only if the answer
would resolve a saved question. An optional progress check-in is at most once
per seven-day period; save that state without repeating the journal. Do not
require a failure story, surprising insight, or measurable productivity claim.
If questions are already resolved, offer finishing early instead of collecting
more notes for their own sake. Window changes require participant direction.

At/after the exclusive end, stop logging. On the next eligible session, give
the one-time notice and resume pinned EXTRACT.md. Integrate supported findings
and question status into the same stack-analysis.md: tool cards, task traces,
workflow improvement loop, and evidence appendix. Keep corrections alongside
claims and preserve uncertainty. Do not produce competing inventories, flow
reports, a profile, or a deck as additional required outcomes.

No active session means no instant reminder. Finish with local document review;
no upload, account lookup, return, community import, or publication follows.
The participant chooses whether to keep/delete generated notes. The dossier
can later supply selected reviewed sections for locally prepared assets, if
requested, while its private appendix remains excluded from asset preparation.

## Scope and baseline

<Approved tool IDs and local-name/alias preferences; relevant CTX/CFG/HST/SELF
IDs and question status. Scope paths stay in state or the dossier appendix.
No new source access is granted by listing a name here.>

## Entries
