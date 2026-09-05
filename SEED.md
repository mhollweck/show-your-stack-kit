# Part 1 · Seed (run today)

You are setting up a Show Your Stack observation window for me. Show Your Stack
is an invite-only group of builders who document how they REALLY build with AI.
Instead of me describing my workflow from memory, you will quietly keep a
journal of how I actually work for the next 1 to 2 weeks. When the window
closes I run Part 2 (EXTRACT.md in this kit), which turns the journal into my
written stack profile.

Files in this kit, all in the same folder as this one:
- INVENTORY.md · how to map my setup (Step 3)
- EXTRACT.md · Part 2; its Phase 4 defines the exact shape of the profile (Step 5 uses it)
- deck-template.html · the presentation renderer (Step 5 fills it)
- journal-template.md · the journal header and entry format (you copy it)
- observer-rule.md · the block that goes into my global rules file
- observer-hook.sh · optional prompt log for Claude Code (you download it)
- STOP.md · how to remove all of this again, any time
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
   ~/Projects/stack-journal/. The only thing that ever moves is the one profile I
   approve at the end of Part 2, as a pull request I read before it opens.
2. Ask before reading any of my files. Never read or reproduce .env files, keys,
   tokens, credentials, billing pages, or message history.
3. The journal records patterns and paraphrases. Never code, never file
   contents, never secrets, never names I have not allowlisted.
4. Every change to my config (rules file, settings) is shown to me in full and
   needs my OK before you write it.

Keep my side tiny: one choice for the window, one tick-list reply for scope,
three OKs (inventory, rule, hook). Do not ask me to describe how I work; that
is what the window is for. You do the work: by the end of this session I have
a first draft of my profile and a presentation I can open, both local.

Step 0 · Already started? If ~/Projects/stack-journal/journal.md exists from an
earlier Part 1, keep it, reuse its window and Allowlist, and do only Step 3
(deep dive) and Step 5 (draft and deck). Then stop.

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

Step 3 · Deep dive (ask first). Propose what you will read, inside the scope
from Step 2 only: my global rules file, project rules files in the personal
projects I named, custom agents, hooks, skills or commands, settings, MCP
list, scheduler definitions, shell rc files, and the folders where my own
tools live. Wait for my one OK, then fetch INVENTORY.md and follow it: follow
the connections, label every tool's status, keep a tool card per material
tool, record findings. If you already know my setup, start from what you know
and verify it against the files. Never execute anything. Summarize the
result for the journal as the Baseline (names, counts, locations).

Step 4 · Journal. Everything Show Your Stack writes lives in ONE folder:
~/Projects/stack-journal/. If I keep my projects somewhere else, ask me once
and use <that folder>/stack-journal/ everywhere below (and set the DIR default
at the top of observer-hook.sh to match). Fetch journal-template.md. Create
~/Projects/stack-journal/journal.md from it: replace START, END and N in the header, keep "How to log" exactly as
written, and fill in the Allowlist and Baseline sections. Leave "## Entries"
empty.

Step 5 · First draft and deck. Fetch EXTRACT.md and use its Phase 4 shape and
slides rules. Write ~/Projects/stack-journal/stack-submission.md as draft v0 from the
inventory alone: fill harness, agents, contextMemory, qualityControl and
versionControl with what the files show (with status labels and the findings),
leave review, spend, failureStory, weirdThing and gems as "not yet: the window
fills this in" unless a rules file states them outright, and build slides only
for the fields that have content. Body: two lines saying this is the day-one
draft from the inventory and that the behavior fields arrive after END. Then
render the deck: copy deck-template.html to ~/Projects/stack-journal/deck.html and
replace {{STACK_JSON}} (every occurrence) with the frontmatter as JSON (escape
any "</script" inside strings). Tell me to open ~/Projects/stack-journal/deck.html.

Step 6 · Observer rule. Fetch observer-rule.md, replace START and END, show me
the block, and ask for my OK. Then append it to the END of my global rules
file: ~/.claude/CLAUDE.md for Claude Code (create the file if it is missing).
For Cursor, Codex, Gemini CLI and others: the equivalent global rules file
(~/.cursor/rules, ~/.codex/AGENTS.md, ~/.gemini/GEMINI.md).

Step 7 · Prompt log (Claude Code only, optional, recommended). Offer me this:
a tiny hook that appends each prompt I send, with a timestamp and the folder
it came from, to ~/Projects/stack-journal/prompts.log. It gives Part 2 real numbers
(prompts per day, prompt length, how often I start with a spec). It is local,
deterministic, prints nothing, and stops by itself after END (it reads END
from the journal header). If I say yes:
  a) download observer-hook.sh to ~/Projects/stack-journal/observer-hook.sh and make
     it executable;
  b) show me this settings change, then add it to ~/.claude/settings.json
     under "hooks" > "UserPromptSubmit". Create the keys if they are missing
     and keep everything else in that file untouched. Use the absolute path
     to my home directory in the command:

  { "hooks": { "UserPromptSubmit": [ { "hooks": [ { "type": "command",
    "command": "/ABSOLUTE/PATH/TO/HOME/Projects/stack-journal/observer-hook.sh" } ] } ] } }

Step 8 · Confirm. Show me a short summary: the journal path, the draft and
deck paths, where the rule block was written, whether the prompt log is on,
START and END, and this one line to remember: "When the window closes your agent reminds you. Then run
Part 2 (EXTRACT.md from the kit)." Mention that Part 2 ends with a pull
request into Maria's private community repo, so I should send Maria my GitHub
login now (`gh api user --jq .login` shows it) and accept her invite when it
arrives (Part 1 itself needs no GitHub at all). Tell me I can open the
journal any time and delete lines I do not like, and that one line stops
everything and removes it from my machine: "Fetch STOP.md from the Show Your
Stack kit and follow it." Then stop. Do not log an entry for this setup
session; the first real entry comes from my next session.
