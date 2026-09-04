# Show Your Stack · kit

Show Your Stack is an invite-only group of builders who document how they
REALLY build with AI: the prompting, the delegation, the review habits, the
scars. Memory lies about this stuff. So instead of a questionnaire, your own
agent keeps a quiet journal of how you actually work for one or two weeks,
then turns it into a written profile you approve line by line.

This repo is the whole kit. Your agent reads it from here; you never copy
anything by hand.

**No company secrets, ever.** Employer and client material is out of scope
before anything is read: no company repos, client code, internal docs, work
chat, customer data. If your day job lives in a company codebase, the journal
records how you work (prompting, delegation, review, verification), never
what the code, product, or client is. Your agent asks you to mark that scope
before it reads a single file.

## Start (10 minutes, today)

Open a fresh Claude Code session in your home directory and paste:

```
I'm taking part in Show Your Stack. Fetch
https://raw.githubusercontent.com/mhollweck/show-your-stack-kit/main/SEED.md
and follow it step by step. Ask before reading any of my files, and nothing
leaves this machine.
```

Works with Cursor, Codex and Gemini CLI too. SEED.md tells your agent where
its rules file lives.

Your agent will ask you five things: how long the window should be (1 week,
2 weeks, or custom), your own 3-line prediction of your workflow, which
folders are company or client work (excluded from every read), which personal
project names may appear in the journal, and an OK for a names-only baseline
of your setup. Then it installs a small observer rule (and, if you say yes, a
local prompt log) and gets out of the way.

## The window (1 to 2 weeks, 0 minutes)

You work like normal. Once per session your agent appends one short entry to
`~/show-your-stack/journal.md`: what you asked for, how you phrased it, what
it delegated, whether you reviewed the diff, how you checked the result. It
asks you one question per week, max. When the window closes it reminds you
once.

## Extract (20 minutes, after the window)

Fresh session, home directory, paste:

```
My Show Your Stack window is over. Fetch
https://raw.githubusercontent.com/mhollweck/show-your-stack-kit/main/EXTRACT.md
and follow it step by step. Ask before reading any of my files; nothing
leaves this machine except the one file I approve.
```

Your agent analyzes the journal (real numbers: prompts per day, review rate,
what you delegated), compares it with your prediction, interviews you only
for the gaps, drafts your profile with a slide spec for your stage talk, and
shows you a redaction report. You approve the file, then your agent opens a
pull request with that one file into Maria's private community repo
(`mhollweck/show-your-stack-community`). You need a GitHub account with the
`gh` CLI logged in, and Maria's collaborator invite accepted; if that fails,
you send Maria the file instead. Maria's merge makes your profile visible to
the members of that private repo, nobody else. The agent also offers to
remove the observer rule and the hook.

## Privacy, in four lines

- No company secrets. Company and client scope is excluded before any read,
  and workflow patterns are all that gets written about work sessions.
- Nothing leaves your machine during the window. Everything lives in
  `~/show-your-stack/`. The only thing that ever moves is the one profile you
  approve, as a pull request you read before it opens.
- Patterns, not contents. The journal holds paraphrases and counts. Never
  code, never secrets, never names you did not allowlist.
- You hold the knife. Every file read and every config change asks first.
  Open the journal any time and delete lines you dislike.
- Remove it in one step. Part 2 offers to strip the rule and the hook, or
  delete the block between the `show-your-stack:observer` markers yourself.

Calls, recordings and profiles never publish without the author's OK.

## Files

| File | What it is |
|---|---|
| `SEED.md` | Part 1. Sets up the window, the journal, the observer rule, the optional prompt log. |
| `journal-template.md` | The journal header and the entry format your agent follows. |
| `observer-rule.md` | The block that goes at the end of your global rules file, with start and end dates. |
| `observer-hook.sh` | Optional Claude Code hook: appends each prompt to a local log, prints nothing, self-expires. |
| `EXTRACT.md` | Part 2. Flow analysis, inventory, short interview, profile draft, redaction report, pull request into the private community repo, cleanup. |

## What an entry looks like

```
## 2026-09-09 (Tue) · project: kappibara
- task: rebuild onboarding; shipped 2 screens
- prompting: 4 prompts; opened with a 12-line spec incl. acceptance criteria; plan mode: yes
- workflow: plan > 2 builder subagents in worktrees > main-thread review > tests > commit
- delegation: 2 subagents (Sonnet), 1 background job; kept the schema decision in main
- review: read the diff line by line for the API change, skimmed the rest
- verification: test suite + manual check in the simulator
- vcs: worktree per lane, small commits, no push
- corrections: "never use the native date picker"; rule candidate
- tools: plan mode, worktrees, /code-review, Xcode MCP
- notable: asked for the rule to go into CLAUDE.md right after the correction
```

Questions, or want out at any point? Tell Maria.
