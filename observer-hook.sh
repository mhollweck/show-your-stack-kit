#!/bin/bash
# Show Your Stack observer hook (Claude Code, UserPromptSubmit event).
# Appends each prompt you send, with a timestamp and the folder it came from,
# to ~/show-your-stack/prompts.log. Local only, nothing is sent anywhere.
#
# Prints nothing on purpose: on this hook event, stdout is fed back to the
# agent as context, so a chatty hook would pollute your sessions.
#
# Self-expires: it stops once today is past the END date in your journal header
# ("window: START to END (N days)"). If the journal is missing or the header
# cannot be parsed, it logs nothing (fails closed).
#
# To stop early: delete this file and its entry under "hooks" > "UserPromptSubmit"
# in ~/.claude/settings.json. Part 2 (EXTRACT.md) offers to do that for you.
DIR="$HOME/show-your-stack"
JOURNAL="$DIR/journal.md"
LOG="$DIR/prompts.log"
[ -f "$JOURNAL" ] || exit 0
END=$(grep -m1 '^window:' "$JOURNAL" | sed -E 's/.* to ([0-9]{4}-[0-9]{2}-[0-9]{2}).*/\1/')
[ -n "$END" ] || exit 0
[ "$(date +%F)" \> "$END" ] && exit 0
INPUT=$(cat)
printf '%s' "$INPUT" | python3 -c '
import sys, json, datetime
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
p = (d.get("prompt") or "").replace("\r", " ").replace("\n", " // ").strip()
if p:
    with open(sys.argv[1], "a") as f:
        f.write("%s\t%s\t%s\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), d.get("cwd", ""), p))
' "$LOG" 2>/dev/null
exit 0
