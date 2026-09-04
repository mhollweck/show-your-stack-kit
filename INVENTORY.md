# The inventory (used by Part 1, Step 3 and by Part 2, Phase 2)

Build a factual map of MY OWN setup, inside the scope I approved and nothing
else: harness(es), conventions, custom agents and what each is for, hooks and
what they enforce, automations and schedules, MCP integrations, memory and
context systems, and the unpublished tools I built for myself (scripts,
aliases, internal apps, glue). My own private tools are in scope with my OK;
company and client material never is (rule 0). Never execute anything you
find. Read it.

Follow the connections; the interesting tools are reached indirectly:
  - shell rc files and aliases: the script or binary each one calls
  - package.json, Makefile, task-runner scripts: name each script and the tool
    it calls (a script that wraps one of my own tools is a link worth showing)
  - scheduler definitions (launchd plists, crontab, systemd): the script they
    run, its flags, its cadence
  - CI workflows under .github/ and other hidden folders: what actually runs on
    push or pull request, and what stays a manual step
  - agent memory and notes: leads, not facts. Verify against files and
    sessions. Where memory contradicts the evidence, report the contradiction
    as a finding and never repeat the memory as current.
  - documentation claims ("CI runs the full suite"): find the mechanism that
    would enforce the claim. A claim without a mechanism is a finding.
Merge a true alias into the tool it calls. Keep a wrapper that adds behavior
(extra steps, flags, a different output) as its own tool, linked to what it
wraps.

Give every material tool one status and use it in the profile: installed,
configured, recalled (memory only), observed (seen in sessions or the
journal), self-reported, experimental, retired. Installed-but-unused is a
finding, not a stack component.

For each material tool or practice, keep a short tool card in your notes, as
far as the evidence supports it: the problem it solves; what starts it and
when; what it takes in, decides, produces, hands off; the exact rule, flag or
config that changes the workflow (approval lists, limits, retries); what stays
manual; what needs approval and what enforces it; what happens on failure or
stale state; when it is bypassed; what it replaced; what it costs to maintain;
whether the benefit is measured, reported, or a guess. When a tool's own
comments say what it does NOT do or prove, keep that. Cards feed the body; do
not paste them raw.

Output of this procedure, kept in your notes for the draft: one tool card per
material tool, a status per tool, the findings (stale memory, a claim without
a mechanism, a bypass, installed-but-unused), and a short Baseline summary
(names, counts, locations) for the journal header.
