# One working document: stack-analysis.md

The final deliverable for capture is one detailed Markdown document. It is
a source for a later community entry and presentation, not a slide deck
flattened into nine categories. Keep the document local. Supporting scope
state and an optional journal are operational files, not extra deliverables.

Use the sections below, adjusting length to actual evidence. Explain each
mechanism fully once; elsewhere point to its tool/evidence IDs instead of
repeating the whole card. Detail should make the account useful to read. An explicit
unknown/declined/not applicable is better than an invented detail. Do not
make a quota of tools, diagrams, failures, or clever insights. Personally
owned unpublished tools are first-class entries; visibility is not a reason
to omit them. Company/client secrets and credentials remain excluded.

## 0. Document status and short overview

Record date/version, scope, evidence mode, review status, and `sharing:
disabled`. Explain the person's main kinds of work at an appropriate level,
their development environment, and three or fewer distinctive supported
choices. Name the principal unknowns. Do not claim a full census.

## 1. Stack map and coverage

Inventory the full workflow across discovery/design/coordination, product
stack, infrastructure/environments, harness/models, custom tooling, context/
memory, delegation, repeated automation, quality/delivery/operations, and
feedback/optimization. Identify what each item does and what connects to
it. Separate development tools from AI used by the product at runtime.

| Tool ID / local name | Origin | Purpose | Trigger / cadence | Input -> output -> consumer | Status and evidence | Sharing treatment |
|---|---|---|---|---|---|---|

Origin: personally built, adapted, external, or unknown. Status: observed
current, participant-confirmed current, experimental, configured-only,
retired, or unknown. A dependency or alias alone is not observed current use.
Sharing treatment: candidate with approved name, candidate with alias,
local-only detail, or unresolved. These are editorial flags, not consent to
publish. Add a small relationship diagram or explicit edge table when it
makes handoffs easier to understand. Every material edge needs evidence or
an uncertainty label. Resolve true aliases to the same tool ID; keep material wrappers as separate
entries connected to the underlying tools they invoke.

## 2. Deep dives into the tools that change the workflow

Use this card for each material custom tool or non-obvious configuration.
Do not spend equal space on an ordinary editor and a bespoke orchestration
system. Names can be aliased later without losing the useful mechanics.

- **Identity and role:** local name, safe alias if wanted, owner/origin,
  current status, and the problem it addresses.
- **Entry point:** how the person or agent invokes it; triggering condition,
  schedule or manual cadence; where it sits in the task lifecycle.
- **Inputs:** categories/schema of information and upstream producer,
  without payloads, credentials, private business examples, or company code.
- **Logic and routing:** meaningful rules, model/agent roles, branching,
  thresholds if eligible for local inspection, concurrency/isolation, and why these choices exist.
- **Outputs and handoff:** concrete artifact or state change, downstream
  reader/tool, and how completion is recognized.
- **Human control:** approval points, edits, overrides, and actions the tool
  cannot perform. Separate documentation from observed behavior.
- **Failure and recovery:** stop/retry/fallback, how errors surface, and what
  manual action restores progress. Unknowns are explicit.
- **Benefit and cost:** observed effect, participant explanation, measurement
  limits, upkeep, complexity, and when using it is not worth the overhead.
- **Evidence and questions:** IDs supporting claims and targeted missing facts.

Safe personally owned snippets or exact interface details belong only when
they explain a useful mechanism and are approved for local inspection. Put
necessary private implementation/path references in the local appendix,
not into default community/deck candidates. Prefer a behavior description
or independent pseudocode to copying implementation.

## 3. Representative task walkthroughs

Show a supported routine path and, where available, a contrasting failed,
manual, or experimental path. For each step include: actor -> trigger/input
-> tool/decision -> result/artifact -> next actor, with evidence IDs.

Cover request framing, success criteria, plan/model routing, delegation,
work isolation, checks, review, correction, handoff, and delivery only as far
as evidence reaches. Include a supported monitoring/debugging/recovery loop
when relevant, or mark it outside the inspected scope. State exactly where the sample ends. A passing test is
not a deployment; an agent request for review is not a human review.

## 4. How this person improves their workflow

Describe the actual feedback loop: what pain or evidence triggers a change,
how they test an idea, decide to adopt/retire it, keep instructions current,
and notice drift. Identify model routing, context management, automation,
quality, or cost choices only when supported. Explain maintenance and cases
where the simpler manual path wins.

Separate **observed**, **participant-reported**, and **proposed experiment**.
Do not promote self-reported savings into measurements or infer causation
from the presence of sophisticated tooling. Optional proposed experiments
should specify a small reversible trial and a way to measure usefulness.
Do not make changes to the person's stack during analysis.

## 5. Details worth teaching another builder

For each supported candidate, write a compact adoption recipe:

1. The problem/situation where the practice helps.
2. Its mechanism: exact sequence, decision rules, and human checkpoint.
3. Minimum setup another builder could reproduce without private code.
4. Tradeoffs, failure conditions, and where it would not help.
5. Supporting evidence and what would need measurement.

Avoid vague claims such as "use agents" or "automate review." Preserve the
interesting mechanics of a private tool even if its name/code stays private.
Examples are independently written or explicitly approved personally owned
material, with any reconstructed example labeled. No company secrets become
eligible just because a story would benefit from them.

## 6. Unresolved questions and participant corrections

List material gaps, the evidence already available, the question that would
resolve each one, and whether it is unknown/declined/not applicable. Keep
corrections alongside the changed claim so stale memory does not win later.
Ask only for information that improves the analysis; no live call needed.

## 7. Preparation for later community entry and deck

Provide a candidate title, one-paragraph story, selected practices, and an
outline whose sections point to this document's claims/tool IDs. Mark which
names need aliasing, which details must be excluded, and which claims need
confirmation. The objective is to derive both assets from one reviewed
account, without rerunning the interview or sending the evidence appendix.

No deck/publication is required to complete this analysis. If the participant
later requests asset preparation, use only the selected reviewed sections,
show the result, and keep it local. Approval of a local document is not an
upload instruction. Existing export commands remain disabled.

## Appendix A. Local evidence and provenance (not for asset export)

| Evidence ID | Type/date | Local reference or safe description | Supports | Does not establish / uncertainty |
|---|---|---|---|---|

Use CTX, CFG, HST, OBS, and SELF consistently. This appendix can retain minimal
approved personal-tool paths/line references needed to audit claims, but no
credentials, confidential company material, raw histories, or whole code
files. Label the appendix local-only. Use a document-level sample statement
and per-claim denominators/unknowns for counts.

## Appendix B. Local disclosure review (not publication consent)

Check each proposed community/deck claim, name, snippet, and example. Record
whether it is a share candidate, needs an alias/rewrite, remains local-only,
or is excluded. Exclusion notes use categories and IDs, never the secret
itself. Confirm no private evidence is needed to understand the shareable
story. Leave audience and external sharing undecided unless the participant
separately chooses them; do not perform any transmission in this flow.
