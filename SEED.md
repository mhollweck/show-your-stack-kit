# Part 1 · Seed (run today)

You are setting up a Show Your Stack observation window for me. Show Your Stack
is an invite-only group of builders who document how they REALLY build with AI.
Instead of me describing my workflow from memory, you will quietly keep a
journal of how I actually work for the next 1 to 2 weeks. When the window
closes I run Part 2 (EXTRACT.md in this kit), which turns the journal into my
written stack profile.

Files in this kit, all in the same folder as this one:
- journal-template.md · the journal header and entry format (you copy it)
- observer-rule.md · the block that goes into my global rules file
- observer-hook.sh · optional prompt log for Claude Code (you download it)
- EXTRACT.md · Part 2, for later
Fetch them from the raw URL base of this file (curl -fsSL, or your web fetch
tool). Fetch a file only when the step below needs it.

Ground rules (non-negotiable):
0. No company secrets, ever. Employer and client material is out of scope
   BEFORE anything is read: no company repos, client code, internal docs, work
   chat, customer data. If my day job lives in a company codebase, the journal
   records my workflow patterns only (how I prompt, delegate, review, verify),
   never what the code, product, or client is. There is no after-the-fact
   redaction promise: what you never read cannot leak.
1. Nothing leaves this machine during the window. Everything you write lives in
   ~/show-your-stack/. The only thing that ever moves is the one profile I
   approve at the end of Part 2, as a pull request I read before it opens.
2. Ask before reading any of my files. Never read or reproduce .env files, keys,
   tokens, credentials, billing pages, or message history.
3. The journal records patterns and paraphrases. Never code, never file
   contents, never secrets, never names I have not allowlisted.
4. Every change to my config (rules file, settings) is shown to me in full and
   needs my OK before you write it.

Keep my side tiny: one choice for the window, one tick-list reply for scope,
three OKs (baseline, rule, hook). Do not ask me to describe how I work; that
is what the window is for.

Step 1 · Window. Ask me how long the window should be: 1 week, 2 weeks
(recommended), or a custom number of days. Compute START (today) and END
(START plus N days) as YYYY-MM-DD and echo both back to me.

Step 2 · Scope and allowlist, as a tick list, not an essay. Offer to list the
folder NAMES directly under my home directory and under my projects folder
(names only, nothing inside them) and wait for my OK. Then show the list and
ask me to mark three things: which folders are company or client work (those
are excluded from every read, and sessions in them are logged only as "work
project" with workflow patterns, nothing else), which personal projects may
appear in the journal by name (everything else is logged as "a private
project"), and any people, companies, or repos that must never appear at all.
One reply from me is enough. Write it into the Allowlist section of the
journal.

Step 3 · Baseline (ask first). If you already know my setup, pre-fill this
and have me confirm instead of asking cold. Propose a light inventory of MY
OWN setup (never a company machine's managed config) and wait for my OK:
which harness(es) I use, the size of my global rules file (line count, not
contents), and the NAMES of my custom agents, hooks, skills or commands, MCP
servers, scheduled jobs, and the unpublished tools I built for myself
(scripts, aliases, internal apps, glue), plus WHERE these live (rc file,
tooling folder, schedules folder, project folders) so Part 2 knows where to
look without asking again. Names, counts and locations only, no contents.
This is the "before" snapshot.

Step 4 · Journal. Fetch journal-template.md. Create ~/show-your-stack/journal.md
from it: replace START, END and N in the header, keep "How to log" exactly as
written, and fill in the Allowlist and Baseline sections. Leave "## Entries"
empty.

Step 5 · Observer rule. Fetch observer-rule.md, replace START and END, show me
the block, and ask for my OK. Then append it to the END of my global rules
file: ~/.claude/CLAUDE.md for Claude Code (create the file if it is missing).
For Cursor, Codex, Gemini CLI and others: the equivalent global rules file
(~/.cursor/rules, ~/.codex/AGENTS.md, ~/.gemini/GEMINI.md).

Step 6 · Prompt log (Claude Code only, optional, recommended). Offer me this:
a tiny hook that appends each prompt I send, with a timestamp and the folder
it came from, to ~/show-your-stack/prompts.log. It gives Part 2 real numbers
(prompts per day, prompt length, how often I start with a spec). It is local,
deterministic, prints nothing, and stops by itself after END (it reads END
from the journal header). If I say yes:
  a) download observer-hook.sh to ~/show-your-stack/observer-hook.sh and make
     it executable;
  b) show me this settings change, then add it to ~/.claude/settings.json
     under "hooks" > "UserPromptSubmit". Create the keys if they are missing
     and keep everything else in that file untouched. Use the absolute path
     to my home directory in the command:

  { "hooks": { "UserPromptSubmit": [ { "hooks": [ { "type": "command",
    "command": "/ABSOLUTE/PATH/TO/HOME/show-your-stack/observer-hook.sh" } ] } ] } }

Step 7 · Confirm. Show me a short summary: the journal path, where the rule
block was written, whether the prompt log is on, START and END, and this one
line to remember: "When the window closes your agent reminds you. Then run
Part 2 (EXTRACT.md from the kit)." Mention that Part 2 ends with a pull
request into Maria's private community repo, so I should send Maria my GitHub
login now (`gh api user --jq .login` shows it) and accept her invite when it
arrives (Part 1 itself needs no GitHub at all). Tell me I can open the
journal any time and delete lines I do not like. Then stop. Do not log an entry for this setup
session; the first real entry comes from my next session.
