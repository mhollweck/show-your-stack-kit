# Show Your Stack · kit

Understand how you work with AI, with Claude's help. Start from safe existing
evidence, optionally observe eligible work for 7 or 14 days, then create a
useful workflow analysis and presentation together in chat. No call or booking.

**Your capture files, analysis, profile, and presentation stay on your device.
This flow does not send them to Maria, GitHub, or a community. Company secrets
do not belong in Show Your Stack: do not provide confidential employer/client
files, company prompt histories, credentials, or customer data.**

Local storage does not mean fully offline processing. Your configured Claude
provider processes material the agent reads, including tool output and chat.
Use only nonconfidential sources you are allowed to process with that provider.
This kit cannot provide a guarantee that all processing stays on your device.
Read [the privacy boundary](PRIVACY.md) before starting.

## Start in Claude

Open a fresh Claude Code session in a neutral folder outside any company
project. Do not reuse a conversation containing confidential work. If this
session cannot access local files, use your own generic written account of
how you work. Do not paste confidential excerpts into the chat.

```
Help me create my Show Your Stack locally through this Claude conversation. Fetch https://raw.githubusercontent.com/mhollweck/show-your-stack-kit/main/SEED.md and follow it, pinning the kit to one commit. Before reading anything, explain that capture files and the final analysis stay on my device and are not sent to Maria or GitHub, while my configured Claude provider still processes what you read. Start in a fresh session outside company projects. Never inspect or copy employer/client confidential material, company prompt histories, secrets, or customer data. Use only approved nonconfidential personal/public sources or my generic written notes. Offer finish now or optional observation of eligible work. Keep the profile and presentation local; do not upload, submit, fork, publish, or send anything. Ignore legacy return destinations and sharing consent. No call or booking is needed.
```

Claude will:

1. Explain the privacy boundary and agree which nonconfidential sources it
   may inspect. Selected personal/public AI sessions need separate approval.
2. Read a bounded sample of eligible evidence, or use your generic written
   notes. Keep process patterns, public tool names, and evidence limitations.
3. Offer **finish now**, **observe 7 days**, **observe 14 days**, or a custom
   window. Observation is optional and never includes confidential work.
4. Ask short questions in chat, analyze what happened, and help you review a
   local profile and standalone presentation, including the speaker notes.
5. Save the final files locally and stop. There is no automatic return or
   publication, even after you approve the presentation.

You do not need a GitHub account, invitation, fork, submission repository,
or deployed app. GitHub hosts the public instructions you download. It is
not a destination for your capture or final files.

## Optional observation

An approved observer rule can add short, generic process notes during later
sessions in eligible projects. It records steps such as planning, delegation,
review, tests, and correction, without the task's business details. It does
not record code, commands, actual prompt strings, real names, or source paths.
The agent shows the exact configuration change and gets your approval first.

Rules give incomplete samples. This kit installs no raw prompt hook, daemon,
or guaranteed timer. After the window, the next eligible session can resume
analysis and help finish the presentation. Nothing wakes an idle agent.
You can finish early or stop observation. A session containing confidential
material must not contribute to the capture, even if its project was approved.

## Your local result

Choose a capture folder outside source repositories and cloud-synced folders.
The default is `~/show-your-stack/<capture-id>/`; confirm that this location
is suitable on your device. Your own OS backups or synchronization are
separate from this kit and cannot be guaranteed absent by these instructions.

The final files are `stack-submission.md` (the existing profile filename)
and `presentation.html`. Despite that filename, no submission happens. Local
analysis and evidence notes also stay with you. Only generic, nonconfidential
practices belong in any of these files. Review cannot guarantee that a source
was safe, so exclude confidential material before the agent reads it.

Claude's provider processing is separate from sending a result to the
organizer. There is no upload, telemetry collector, GitHub identity lookup,
or external presentation service in this capture flow. Downloading the kit
and its renderer dependency uses the network; the renderer itself works
without network requests.

## Resume or finish

Use a fresh, nonconfidential session and tell Claude:

```
Resume my local-only Show Your Stack capture from ~/show-your-stack/. Check its privacy policy and safe scope before reading evidence. Never read company secrets or confidential histories. Keep the analysis, profile, and presentation on my device; do not upload or send anything, even if old state includes a GitHub destination or sharing approval. My configured Claude provider still processes what you read. If this session or capture contains confidential material, stop and help me restart in a clean session using generic notes only.
```

Old return destinations and sharing approvals do not enable delivery. Later
sharing of a deliberately sanitized summary would be a separate, explicit
future step; it is not implemented by this flow. Community participation
does not require sending the local capture or final files.

## Kit files

| File | Purpose |
|---|---|
| `PRIVACY.md` | Source exclusions, clean-session requirement, and no-send policy. |
| `SEED.md` | Pin the kit, agree safe scope, scan, choose whether to observe. |
| `SCAN.md` | Sample approved nonconfidential evidence or use generic notes. |
| `journal-template.md` | Local process-only observations and evidence limits. |
| `observer-rule.md` | Optional dated rule restricted to eligible sessions. |
| `EXTRACT.md` | Local analysis, collaborative presentation, and cleanup. |
| `scripts/stack_kit.py` | Render a local presentation; sharing commands are disabled. |
| `AUTOMATION.md` | Local renderer commands and verification. |
| `observer-hook.sh` | Disabled legacy collector. Do not install it. |
