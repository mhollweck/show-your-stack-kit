# Local analysis first; optional asset rendering later

The participant's agent follows SEED.md, SCAN.md, DOSSIER.md, and EXTRACT.md
to discover the stack and produce one detailed stack-analysis.md. That file
contains the inventory, custom-tool mechanics, task traces, optimization loop,
questions, and local evidence/disclosure appendices. No script can replace
that interpretation or prove that the agent found every private tool.

Personally owned unpublished tooling is eligible within approved scope.
Company/client secrets and credentials remain excluded; read PRIVACY.md.
Existing relevant context is useful evidence of recollection, not proof of
current use. Capture and final documents are not sent anywhere by this kit.

## Optional later deck

When the participant asks for a local presentation, derive a compatible
stack-submission.md profile from the reviewed dossier sections. Exclude local
private appendices and unselected details. The renderer supports the existing
site schema and has no network/model calls. It does not consume the dossier
format directly; this editorial conversion preserves the distinction between
a detailed working account and a readable deck.

Requires Python 3.10+ and PyYAML. In the pinned kit checkout:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/stack_kit.py render /ABSOLUTE/CAPTURE/derived/stack-submission.md --output /ABSOLUTE/CAPTURE/derived/presentation.html
```

Dependency installation fetches public software without participant data.
Open the deck locally, review every slide and speaker note, and keep it on
the participant's device. Arrow keys navigate, N toggles notes, and Print
saves a landscape PDF. Existing approved scope applies to any preparation;
rendering or approval does not grant permission to transmit the asset.

The old approve/submit commands are disabled before file reads or network
actions. Old arguments, consent, and RETURN_REPO cannot enable them. The
legacy observer-hook.sh is inert. Never substitute a different upload path.

## Verification

```sh
.venv/bin/python -m unittest discover -s tests -v
```

These checks cover local rendering and blocked export, not quality of stack
understanding. Prompt quality needs behavioral evaluation with a known stack:
private tools, undocumented script interfaces, alias/scheduler connections,
current versus retired/prototype/dependency-only items, missing source evidence,
and self-reported versus measured benefit. Assess source-linked explanations
and unresolved questions, not a keyword count or a polished slide alone.
