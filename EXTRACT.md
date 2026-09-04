# Part 2 · Extract (run after your window)

You are helping me turn my Show Your Stack observation window into my stack
profile. Show Your Stack is an invite-only group of builders who document how
they REALLY build with AI. Your job: analyze the journal my agent kept,
inventory my actual setup, interview me only for what the journal cannot
answer, and produce ONE file, stack-submission.md, that I review. Then hand
it off.

If the organizer gave me three lines (SUBMIT_URL, SUBMIT_HANDLE, SUBMIT_TOKEN)
they are in my message together with this prompt. If not, Phase 7 hands the
file to me instead.

Ground rules (non-negotiable):
1. Ask before reading. List what you want to look at and wait for my OK:
   ~/show-your-stack/ (journal.md, prompts.log, flow-analysis.md if present),
   my global rules file, project rules files I pick, custom agents, hooks,
   skills or commands, settings permissions, scheduled jobs, MCP server list.
2. Never read or reproduce .env files, keys, tokens, credentials, billing
   pages, or message history. If a config file contains a secret inline,
   write [redacted] and note it in the redaction report.
3. Nothing leaves this machine except the one approved file, and only in
   Phase 7.
4. Raw prompts from prompts.log are evidence for numbers and patterns. Never
   quote one in the submission unless I approve that exact quote.

Phase 0 · Evidence. Ask to read ~/show-your-stack/. If there is no journal (I
skipped the window), say so and continue in cold mode: skip Phase 1 and ask
every interview question in Phase 3 instead of pre-filling.

Phase 1 · Flow analysis. Write ~/show-your-stack/flow-analysis.md and show it
to me:
  a) By the numbers: window length, days with activity, sessions logged,
     prompts total and per active day (from prompts.log if present), median
     prompt length in words, share of first prompts that were a spec vs a
     one-liner, plan mode uses, delegations (subagents, background,
     scheduled), sessions where I reviewed the diff, verification methods
     tally, corrections count, tools tally. Only numbers the evidence
     supports; write "not observed" otherwise.
  b) Patterns: 5 to 8 bullets, each with an evidence count ("asked for tests
     before commit in 9 of 12 sessions").
  c) Prediction vs observed: my 3 prediction lines, each paired with what
     actually happened. Be direct; the gap is the point.
  d) Corrections and the rules they imply, deduplicated.
  e) Gem candidates: 3 to 5 one-liners another builder could adopt tomorrow.
  f) Open questions: what the journal could not tell you.

Phase 2 · Inventory (after my OK): read the approved files and build a factual
map: harness(es), conventions, custom agents and what each is for, hooks and
what they enforce, automations and schedules, MCP integrations, memory and
context systems. Compare with the Baseline in the journal and note what
changed during the window.

Phase 3 · Interview. Pre-fill every answer you can from the journal and the
analysis, show me the full set, and have me confirm or correct. Ask cold only
the ones you cannot fill. One at a time, short answers welcome.
  1. Walk me through a typical day of the window: first prompt to last
     shipped thing.
  2. Agents: what runs in parallel, in the background, on a schedule? What do
     you delegate vs keep in the main thread?
  3. Code review: do you review AI code at all? How: line by line, diff level,
     vibes, AI reviews AI?
  4. Version control: worktrees? branch discipline? how do parallel agents not
     clobber each other?
  5. Quality control: how do you KNOW it works before you ship?
  6. Context and memory: how does your agent know your codebase and
     preferences?
  7. Spend: what do you pay monthly, and what is your model routing (cheap vs
     expensive tiers)? Share only what you are comfortable publishing.
  8. The failure story: worst thing an agent ever did to you, and the rule it
     produced. (Start from the week 2 check-in if there is one.)
  9. The gem: ONE thing you would tell every builder. (Start from the gem
     candidates.)
 10. The weird thing: something in your setup you suspect nobody else does.
 11. The gap: which prediction vs observed pair surprised you most, and what
     are you changing because of it?

Phase 4 · Draft stack-submission.md in exactly this shape:

---
name:            # how you want to be credited
oneLiner:        # your setup in one sentence
tags: []         # 3-5, e.g. [Claude Code, worktrees, cron agents]
harness:         # tools + models, and your routing logic
agents:          # what you delegate, parallelize, schedule
review:          # how AI code gets reviewed (or does not, and why)
versionControl:  # branch/worktree/commit discipline with agents
qualityControl:  # tests, checks, "how I know it works"
contextMemory:   # rules files, docs discipline, memory systems
spend:           # only what you are happy to publish; "prefer not" is fine
gems: []         # 3-5 one-liners, your gem from Q9 first
failureStory:    # the war story + the rule it produced
weirdThing:      # from Q10
links: {}        # site/GitHub/X, whatever you want shown
---

Also add a slides: block to the frontmatter. It powers my auto-generated stage
presentation. Rules:
  - GRAPHICS-FIRST: as many graphics as possible; plain lines are the last
    resort.
  - Every slide must be understandable on its own, without me narrating, but
    it stays a presentation, never a text wall.
  - Every node or item is an object { label: 4 words max, sub: 8 words max of
    context }. The label is what the audience reads first, the sub is what
    makes it make sense.
  - Every slide gets why: ONE line, the reason this setup choice exists.
Types:
  - type: flow    a pipeline: nodes: [3-5 {label, sub}]
                  (routing, review chains, context layers)
  - type: roster  a crew list: items: [up to 8 {label, sub, meta}] where meta
                  is a short chip, a model or a cadence: "Sonnet", "weekly",
                  "cron" (agents and automations)
  - type: tiles   a wall of rule cards: items: [4-8 {label, sub}]
                  (rules, tripwires, principles)
  - type: lines   2-3 big punch lines: lines: [strings] (stories; last resort)
Keys: harness, agents, review, versionControl, qualityControl, contextMemory,
spend, failureStory, weirdThing.
Example:
  harness:
    type: flow
    why: "route by job: the expensive model only thinks"
    nodes:
      - { label: "Fable", sub: "plans, reviews, debugs" }
      - { label: "Sonnet builders", sub: "execute written specs" }

Then the body, in my own voice: the guided tour of my setup, with real
(redacted) excerpts from my configs where they earn their place, and a
"By the numbers" block from Phase 1 (window length, sessions, prompts per
day, review rate, and the prediction vs observed pair from Q11). Numbers make
this profile different from a memory-based one; keep them.

Phase 5 · Redaction pass. Before showing me the final file, produce a
REDACTION REPORT: every place you removed or generalized something (keys,
client or employer names, private repo names, revenue, anything under NDA,
anything outside the journal allowlist), plus anything you are UNSURE about,
flagged for my call. Company names and numbers appear only if I typed them in
this conversation and confirm them.

Phase 6 · Show me the complete file. I approve or edit. Only then save
stack-submission.md in ~/show-your-stack/.

Phase 7 · Hand-off. If SUBMIT_URL, SUBMIT_HANDLE and SUBMIT_TOKEN were given:
POST JSON {"handle": SUBMIT_HANDLE, "token": SUBMIT_TOKEN, "markdown": <full
contents of stack-submission.md>} to SUBMIT_URL. A 200 {"ok":true} means it
is in; tell me, and remind me I will get a preview to approve before anything
publishes. If the lines were not given or the request fails: keep the file
local and tell me to send stack-submission.md to Maria directly. Never submit
before my Phase 6 approval, and never send anything anywhere except
SUBMIT_URL.

Phase 8 · Cleanup (ask first). Offer to remove the observer block (between the
show-your-stack:observer markers) from my rules file and the observer hook
from ~/.claude/settings.json. Keep ~/show-your-stack/ as it is: the journal
and the analysis are mine.
