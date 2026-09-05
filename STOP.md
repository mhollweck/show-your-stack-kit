# Stop and reverse (any time, no questions asked)

You are removing Show Your Stack from my machine. Show me the plan below with
the exact paths you found, wait for my one OK, then do all of it. Nothing
leaves this machine during any of this.

1. Observer rule. Find the block between
   `<!-- show-your-stack:observer:start -->` and
   `<!-- show-your-stack:observer:end -->` in my global rules file:
   ~/.claude/CLAUDE.md, and also check ~/.cursor/rules, ~/.codex/AGENTS.md,
   ~/.gemini/GEMINI.md. Remove the block and nothing else in those files.
2. Prompt-log hook. In ~/.claude/settings.json, under "hooks" >
   "UserPromptSubmit", remove only the entry whose command ends in
   observer-hook.sh. Keep every other hook. The file must stay valid JSON;
   if "UserPromptSubmit" ends up empty, remove the key.
3. Local files. Delete the Show Your Stack folder: ~/show-your-stack/
   (journal.md, prompts.log, flow-analysis.md, stack-submission.md, deck.html,
   observer-hook.sh, and the community/ clone if present). If the hook
   command or the rule block pointed at a different folder, that folder is
   the one to delete; show me the path before deleting.
4. Already shared? If I opened a pull request or my profile was merged into
   the community repo, nothing on this machine undoes that. Tell me to send
   Maria one line ("please remove my stack") and she deletes it from the
   community repo and the members' site. Do not push, close, or edit anything
   on GitHub yourself.
5. Confirm in three lines: what was removed, what was kept (nothing), and
   that nothing was sent anywhere.
