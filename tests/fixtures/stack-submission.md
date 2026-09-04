---
name: "Example Builder"
oneLiner: "Small plans, one working branch, and a test before each handoff."
tags: ["AI coding", "Small batches", "Human review"]
harness: "One coding agent handles implementation. I choose the model manually."
agents: "I ask a second agent to inspect risky diffs; no scheduled agents were observed."
review: "I read the changed behavior and run the app. Critical paths get line-by-line review."
versionControl: "One branch per change. Parallel edits use separate worktrees."
qualityControl: "Run the focused regression check, then inspect the running result."
contextMemory: "Project rules contain stable decisions. Session notes carry short-lived context."
spend: "Prefer not to share."
gems:
  - "Write the success check before asking the agent to implement."
  - "Keep one concrete task per working branch."
failureStory: "An agent changed an unrelated route. Now I inspect the diff scope before committing."
weirdThing: "I keep a tiny list of decisions the agent should challenge again next week."
links: {}
evidence:
  mode: "scan-assisted"
  summary: "An approved project scan and a short author interview."
  sources:
    - "Two project rule files and one test configuration."
    - "Five historical prompt excerpts selected by the author."
  limitations:
    - "These were selected sources, not a complete activity log."
slides:
  harness:
    type: flow
    why: "Make the expected result clear before changing code."
    notes: "Start with one recent feature and walk through these three steps."
    nodes:
      - {label: "Define the check", sub: "Write down what success looks like"}
      - {label: "Build a slice", sub: "Keep the diff small enough to inspect"}
      - {label: "Run and review", sub: "Verify behavior before the handoff"}
  agents:
    type: roster
    why: "A second perspective helps on risky changes."
    items:
      - {label: "Builder", sub: "Implements the agreed task", meta: "Per task"}
      - {label: "Reviewer", sub: "Looks for regressions and omissions", meta: "As needed"}
  review:
    type: flow
    why: "Check the result in context."
    nodes:
      - {label: "Read the diff", sub: "Confirm the scope and intent"}
      - {label: "Use the app", sub: "Follow the changed user path"}
      - {label: "Inspect the risk", sub: "Read critical sections line by line"}
  versionControl:
    type: tiles
    why: "Independent tasks should remain easy to undo."
    items:
      - {label: "One task", sub: "Keep each branch focused"}
      - {label: "Separate worktrees", sub: "Keep concurrent edits apart"}
  qualityControl:
    type: flow
    why: "Behavior is the acceptance condition."
    nodes:
      - {label: "Regression check", sub: "Exercise the behavior that changed"}
      - {label: "Visual check", sub: "Inspect the running result"}
  contextMemory:
    type: tiles
    why: "Stable rules and temporary notes age differently."
    items:
      - {label: "Project rules", sub: "Store decisions that should persist"}
      - {label: "Session notes", sub: "Record context for the next handoff"}
  spend:
    type: lines
    why: "The author chose to keep costs private."
    lines: ["Spend: not shared."]
  failureStory:
    type: lines
    why: "Every failure should leave a useful rule."
    lines: ["An unrelated route changed.", "Now I check diff scope before committing."]
  weirdThing:
    type: lines
    why: "A decision should survive another look."
    lines: ["A short list of decisions to challenge next week."]
---

This is a synthetic example for renderer and submission tests, not a real
participant profile. No claims about a real builder's workflow are made here.
