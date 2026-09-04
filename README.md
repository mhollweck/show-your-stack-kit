# Show Your Stack · understand the workflow behind the tools

Your development stack includes the tools you built yourself: unpublished
scripts, agent wrappers, local apps, aliases, skills, integrations, and the
small automations that connect them. Claude should discover those alongside
the languages, frameworks, models, and services you use, then explain how
the whole workflow operates and improves.

The result is **one detailed local document, stack-analysis.md**: your stack
map, important custom tools, real task walkthroughs, decision rules, human
checks, failure/recovery paths, tradeoffs, and practices worth teaching.
It becomes the source for a later community entry and deck. No call needed.

**Your capture stays with you.** Nothing is uploaded to Maria or GitHub.
Personally owned private tooling can be included with your permission; company/
client secrets and credentials cannot. Claude's configured provider processes
what it reads, so local files do not mean offline AI. Read [PRIVACY.md](PRIVACY.md)
before choosing sources. You can explain a tool without exposing its code.

## Start with your agent's existing knowledge

Use Claude Code with relevant authorized context about your work. A fresh
blank conversation is not required when that context is safe. If Claude
cannot access files, it can work from your descriptions and mark what it
cannot verify. No public repository, GitHub identity, or invitation is needed.

```
Help me understand my full development stack, including personally owned unpublished tools, scripts, agents, and workflow glue. Fetch https://raw.githubusercontent.com/mhollweck/show-your-stack-kit/main/SEED.md and follow one pinned kit commit. Use relevant authorized context as leads, then inspect only sources I approve. Private does not mean ineligible; company/client secrets and credentials remain excluded, and my configured Claude provider processes what you read. Trace what invokes each important tool, its inputs, outputs, decisions, human gates, failures, and evidence of actual use. Ask focused questions about missing connections and why choices exist. Finish now or offer observation only for specific gaps. Consolidate everything in one local stack-analysis.md for later community/deck preparation. Do not upload or send anything, and do not change my stack. No call is needed.
```

Claude will:

1. Start from what it already knows, then agree a scope that includes your
   own tooling locations as well as selected projects and past sessions.
2. Follow approved references across aliases, scripts, safe configuration,
   skills/agents, schedules, checks, and handoff artifacts. It does not run
   discovered tools just to inspect them.
3. Separate actual use from installed, remembered, experimental, and retired
   tools. Trace representative work and keep unanswered questions visible.
4. Ask focused questions about intent, missing connections, manual decisions,
   maintenance, and what works or does not. Finish now, or optionally observe
   eligible work for 7 / 14 / custom days to resolve specific gaps.
5. Review one document with you. A local evidence appendix supports the story;
   selected reviewed sections can later become a community entry and deck.

For example, a useful finding explains how your task wrapper creates isolated
worktrees, stops on a failed check, and prepares evidence for a human before
merge, if those details are supported. "Uses AI agents and Git" misses the
mechanism. Names can be aliased later without removing that useful detail.

## What remains private

Scope, notes, evidence, document, and any later locally rendered asset stay
in your chosen folder outside Git checkouts and cloud-synced directories.
The main document labels what could be shared, what needs an alias, and what
must remain in its local-only appendix. Those labels are not sharing consent.
No raw histories, credentials, or company/client confidential material belong
in any section. Existing context or prior project access is not permission
to read additional sources. See PRIVACY.md for mixed/uncertain sources.

This kit installs no raw prompt hook, upload service, daemon, or guaranteed
timer. Observation is a partial sample. The next eligible session after the
window may resume analysis; an idle agent does not wake itself. The local
renderer makes no network/model calls; fetching the public kit or dependency
uses the network without participant data attached.

## Resume

```
Resume my local Show Your Stack analysis. Fetch https://raw.githubusercontent.com/mhollweck/show-your-stack-kit/main/SEED.md and follow one pinned kit commit. Check minimal saved policy and scope before reading stack-analysis.md or any evidence; reuse eligible work and ask only for missing scope. Use relevant authorized context and help close important gaps about my tools and workflow, including personally owned unpublished tooling. Keep company/client secrets out, distinguish remembered/configured/observed facts, and keep everything local. Do not upload or reuse old sharing consent. My configured Claude provider still processes what you read.
```

Legacy RETURN_REPO, sharing consent, and receipts do not enable export. The
old approve/submit commands remain disabled. Creating a local document or deck
does not send it. A future community-sharing step needs a separate decision.

## Kit files

| File | Purpose |
|---|---|
| SEED.md | Agree scope, use existing context, pin the kit, choose finish/observe. |
| SCAN.md | Discover the full stack and inspect the mechanics of custom tooling. |
| DOSSIER.md | Structure the one working document and its evidence appendix. |
| EXTRACT.md | Close gaps, review the full account, prepare later asset candidates. |
| PRIVACY.md | Private owned tools versus company secrets; local capture boundary. |
| observer-rule.md / journal-template.md | Optional targeted observations. |
| AUTOMATION.md / scripts/stack_kit.py | Local renderer for a later derived profile; export disabled. |
| observer-hook.sh | Disabled legacy raw-prompt collector. |
