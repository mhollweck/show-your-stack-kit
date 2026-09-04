#!/usr/bin/env python3
"""Render a local presentation. Capture data and presentations stay on this device."""

import argparse
import html
from pathlib import Path
import sys

LOCAL_ONLY_POLICY = (
    "Show Your Stack is local-only. Sharing approval and submission are disabled. "
    "Keep capture files and presentations on this device and review them locally. "
    "Existing consent, RETURN_REPO, and legacy flags cannot enable export."
)

# Old executable invocations fail closed even if the rendering dependency is
# missing; they never reach profile parsing, authentication, or consent handling.
if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] in ("approve", "submit"):
    print(f"Stopped: {LOCAL_ONLY_POLICY}", file=sys.stderr)
    sys.exit(1)

try:
    import yaml
except ImportError:
    raise SystemExit("Install dependencies: python3 -m venv .venv; .venv/bin/python -m pip install -r requirements.txt")

MAX_FILE_BYTES = 1_000_000
KIT_ROOT = Path(__file__).resolve().parent.parent
SECTIONS = {
    "harness": "The stack", "agents": "The crew", "review": "How I review",
    "versionControl": "How work stays organized", "qualityControl": "How I know it works",
    "contextMemory": "Context and memory", "spend": "What it costs",
    "failureStory": "The failure and the rule", "weirdThing": "The unusual part",
}


class KitError(Exception):
    pass


def require(condition, message):
    if not condition:
        raise KitError(message)


def read_file(path):
    require(not path.is_symlink() and path.is_file(), f"Expected a regular file: {path.name}")
    require(0 < path.stat().st_size <= MAX_FILE_BYTES, f"{path.name} must be 1 to {MAX_FILE_BYTES} bytes.")
    data = path.read_bytes()
    require(0 < len(data) <= MAX_FILE_BYTES, f"{path.name} must be 1 to {MAX_FILE_BYTES} bytes.")
    return data


class UniqueLoader(yaml.SafeLoader):
    """Reject ambiguous YAML instead of silently accepting duplicate keys."""


def unique_mapping(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            require(key not in mapping, f"Duplicate YAML key: {key}")
            mapping[key] = loader.construct_object(value_node, deep=deep)
        except TypeError as exc:
            raise KitError("YAML mapping keys must be scalar strings.") from exc
    return mapping


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def parse_profile(data):
    try:
        source = data.decode("utf-8")
    except UnicodeError as exc:
        raise KitError("Profile must be UTF-8.") from exc
    lines = source.splitlines()
    require(lines and lines[0] == "---", "Profile needs YAML frontmatter starting with ---.")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise KitError("Profile frontmatter must end with ---.") from exc
    try:
        p = yaml.load("\n".join(lines[1:end]), Loader=UniqueLoader)
    except yaml.YAMLError as exc:
        raise KitError("Invalid YAML in profile.") from exc
    require(isinstance(p, dict), "Frontmatter must be an object.")
    for field in ["name", "oneLiner", *SECTIONS]:
        require(isinstance(p.get(field), str) and p[field].strip(), f"Missing text field: {field}")
    for field in ("tags", "gems"):
        minimum = 0 if field == "gems" else 1
        require(isinstance(p.get(field), list) and minimum <= len(p[field]) <= 8, f"{field} needs {minimum} to 8 items.")
        require(all(isinstance(item, str) and item.strip() for item in p[field]), f"{field} items must be nonempty text.")
    require(isinstance(p.get("links", {}), dict), "links must be an object.")
    slides = p.get("slides")
    require(isinstance(slides, dict), "A final presentation needs a slides block ({} is allowed).")
    require(set(slides) <= set(SECTIONS), "slides contains an unknown section.")
    for key, spec in slides.items():
        require(isinstance(spec, dict), f"slides.{key} must be an object.")
        kind = spec.get("type")
        require(kind in ("flow", "roster", "tiles", "lines"), f"Unknown slide type for {key}.")
        require(isinstance(spec.get("why"), str) and spec["why"].strip(), f"slides.{key} needs why.")
        require(isinstance(spec.get("notes", ""), str), f"slides.{key}.notes must be text.")
        items = spec.get("nodes" if kind == "flow" else "lines" if kind == "lines" else "items")
        maximum = 5 if kind == "flow" else 3 if kind == "lines" else 8
        require(isinstance(items, list) and 1 <= len(items) <= maximum, f"slides.{key} needs 1 to {maximum} items.")
        for item in items:
            if kind == "lines":
                require(isinstance(item, str) and item.strip(), f"slides.{key}.lines items must be text.")
            else:
                require(isinstance(item, dict) and isinstance(item.get("label"), str) and item["label"].strip(), f"slides.{key} items need labels.")
                require(all(isinstance(item.get(f, ""), str) for f in ("sub", "meta")), f"slides.{key} sub/meta must be text.")
                require(len(item["label"].split()) <= 4 and len(item.get("sub", "").split()) <= 8, f"slides.{key}: shorten labels to 4 words and subtext to 8 words; put detail in notes.")
    evidence = p.get("evidence", {})
    require(isinstance(evidence, dict), "evidence must be an object.")
    for key in ("mode", "summary"):
        require(isinstance(evidence.get(key, ""), str), f"evidence.{key} must be text.")
    for key in ("sources", "limitations"):
        require(isinstance(evidence.get(key, []), list) and all(isinstance(x, str) for x in evidence.get(key, [])), f"evidence.{key} must be a list of text.")
    return p


CSS = """
:root{color-scheme:dark;--bg:#101411;--fg:#f2f2e7;--muted:#a2b3a7;--accent:#bcf378;--line:#3e5141}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font-family:ui-sans-serif,system-ui,sans-serif}
main{max-width:1440px;margin:auto}.slide{min-height:100svh;padding:clamp(28px,6vw,90px);display:flex;flex-direction:column;justify-content:center;border-bottom:1px solid var(--line);scroll-margin:0}
.eyebrow{font-size:14px;text-transform:uppercase;letter-spacing:.16em;color:var(--accent)}h1{font-size:clamp(48px,8vw,110px);line-height:1.02;letter-spacing:-.05em;margin:26px 0}h2{font-size:clamp(34px,5vw,68px);line-height:1.08;letter-spacing:-.035em;margin:20px 0 40px}.lead,.why{font-size:clamp(20px,2.5vw,32px);max-width:1000px;line-height:1.4}.why{color:var(--muted);margin-bottom:0}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(220px,100%),1fr));gap:18px}.card{border:1px solid var(--line);border-radius:16px;padding:24px;min-width:0}.card strong{font-size:clamp(22px,2.5vw,34px);display:block;overflow-wrap:anywhere}.card p{color:var(--muted);font-size:20px;line-height:1.45;margin:14px 0 0}.chip{display:inline-block;padding:6px 10px;color:var(--accent);background:#253420;border-radius:30px;font-size:13px;margin:0 4px 18px 0}.flow .card{border-top:3px solid var(--accent)}.step{font-size:13px;color:var(--accent);display:block;margin-bottom:16px}
.punch{font-size:clamp(26px,4vw,48px);line-height:1.25;margin:20px 0;max-width:1100px}li{font-size:clamp(20px,2vw,28px);margin:20px 0;line-height:1.4}.notes{display:none;background:#1b271d;border-radius:12px;padding:20px;margin-top:30px;white-space:pre-wrap;font-size:18px;line-height:1.5;color:var(--muted)}body.show-notes .notes{display:block}
nav{position:fixed;bottom:16px;right:16px;display:flex;gap:8px;align-items:center;background:#101411ef;padding:10px;border:1px solid var(--line);border-radius:12px}button{background:#26372b;color:var(--fg);border:1px solid var(--line);border-radius:6px;padding:8px 12px;cursor:pointer;font:inherit}button:focus-visible{outline:3px solid var(--accent)}.progress{font-size:13px;color:var(--muted);min-width:42px;text-align:center}.hint{font-size:14px;color:var(--muted)}
@media(max-width:640px){.slide{min-height:100svh;padding-bottom:110px}.cards{grid-template-columns:1fr}nav{left:12px;right:12px;justify-content:center}button{font-size:13px;padding:8px}.hint{font-size:12px}}
@media print{@page{size:landscape;margin:12mm}:root{color-scheme:light;--bg:white;--fg:#111;--muted:#405044;--accent:#285a14;--line:#9ca99e}body{background:white;color:#111}.slide{min-height:0;height:auto;break-after:page;page-break-after:always;padding:16mm 8mm;border:0}.slide:last-child{break-after:auto}h1{font-size:58pt}h2{font-size:36pt;margin:10px 0 28px}.lead,.why{font-size:18pt}.card{padding:16px}.card strong{font-size:21pt}.card p,li{font-size:15pt}.chip{background:#edf5e7}.punch{font-size:25pt}.notes,body.show-notes .notes,nav,.hint{display:none}}
"""
JS = """
const slides=[...document.querySelectorAll('.slide')]; let current=0;
function show(n){current=Math.max(0,Math.min(slides.length-1,n));slides[current].scrollIntoView({behavior:'instant'});update();}
function update(){document.getElementById('progress').textContent=`${current+1} / ${slides.length}`;}
function notes(){document.body.classList.toggle('show-notes');document.getElementById('notes').setAttribute('aria-pressed',document.body.classList.contains('show-notes'));}
document.getElementById('prev').onclick=()=>show(current-1);document.getElementById('next').onclick=()=>show(current+1);document.getElementById('notes').onclick=notes;document.getElementById('print').onclick=()=>window.print();
document.addEventListener('keydown',e=>{if(e.target instanceof HTMLButtonElement&&[' ','Enter'].includes(e.key))return;if(['ArrowRight','ArrowDown','PageDown',' '].includes(e.key)){e.preventDefault();show(current+1);}else if(['ArrowLeft','ArrowUp','PageUp'].includes(e.key)){e.preventDefault();show(current-1);}else if(e.key==='Home'){e.preventDefault();show(0);}else if(e.key==='End'){e.preventDefault();show(slides.length-1);}else if(e.key.toLowerCase()==='n'){notes();}});
let scheduled=false;window.addEventListener('scroll',()=>{if(scheduled)return;scheduled=true;requestAnimationFrame(()=>{scheduled=false;const top=window.innerHeight*.4;let closest=Infinity;slides.forEach((s,i)=>{const r=s.getBoundingClientRect();const d=r.top<=top&&r.bottom>=top?0:Math.min(Math.abs(r.top-top),Math.abs(r.bottom-top));if(d<closest){closest=d;current=i;}});update();});},{passive:true});update();
"""


def render(data):
    p = parse_profile(data)
    esc = lambda value: html.escape(str(value), quote=True)
    sections = []

    def slide(title, content, why="", notes=""):
        number = len(sections) + 1
        sections.append(f'<section class="slide" id="slide-{number}" aria-label="{esc(title)}"><p class="eyebrow">Show Your Stack</p><h2>{esc(title)}</h2>{content}' + (f'<p class="why">{esc(why)}</p>' if why else "") + (f'<aside class="notes" aria-label="Speaker notes">{esc(notes)}</aside>' if notes else "") + '</section>')

    tags = " ".join('<span class="chip">' + esc(x) + '</span>' for x in p["tags"])
    sections.append(f'<section class="slide" id="slide-1" aria-label="Introduction"><p class="eyebrow">Show Your Stack / A builder\u2019s field notes</p><h1>{esc(p["name"])}</h1><p class="lead">{esc(p["oneLiner"])}</p><p>{tags}</p><p class="hint">Arrow keys to move / N for speaker notes / Print to save a PDF</p></section>')
    for key, title in SECTIONS.items():
        spec = p["slides"].get(key)
        if not spec:
            slide(title, f'<p class="lead">{esc(p[key])}</p>', notes=p[key])
            continue
        kind = spec["type"]
        if kind == "lines":
            content = "".join(f'<p class="punch">{esc(line)}</p>' for line in spec["lines"])
        else:
            items = spec["nodes" if kind == "flow" else "items"]
            cards = []
            for i, item in enumerate(items, 1):
                cards.append('<div class="card">' + (f'<span class="step">{i:02d} /</span>' if kind == "flow" else "") + (f'<span class="chip">{esc(item["meta"])}</span>' if item.get("meta") else "") + f'<strong>{esc(item["label"])}</strong><p>{esc(item.get("sub", ""))}</p></div>')
            content = f'<div class="cards {kind}">{"".join(cards)}</div>'
        slide(title, content, spec["why"], spec.get("notes") or p[key])
    evidence = p.get("evidence", {})
    facts, limits = evidence.get("sources", []), evidence.get("limitations", [])
    evidence_text = evidence.get("summary") or "This profile combines the author\u2019s account and the sources they approved. Observation coverage was not specified."
    content = f'<p class="lead">{esc(evidence_text)}</p>'
    if facts:
        content += '<ul>' + ''.join(f'<li>{esc(x)}</li>' for x in facts) + '</ul>'
    if limits:
        content += '<p class="why">Limitation: ' + esc(limits[0]) + '</p>'
    slide("What this is based on", content, "Mode: " + evidence.get("mode", "author account; coverage unspecified"), "Limitations:\n" + "\n".join(limits) if limits else "Limitations were not specified. Do not infer population totals from selected samples.")
    if p["gems"]:
        slide("Try this in your own stack", '<ul>' + ''.join(f'<li>{esc(x)}</li>' for x in p["gems"]) + '</ul>', "A few practices worth taking home.")
    return ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="referrer" content="no-referrer"><meta http-equiv="Content-Security-Policy" content="default-src \'none\'; style-src \'unsafe-inline\'; script-src \'unsafe-inline\'; base-uri \'none\'; form-action \'none\'"><title>' + esc(p["name"]) + ' / Show Your Stack</title><style>' + CSS + '</style></head><body><main>' + ''.join(sections) + '</main><nav aria-label="Presentation controls"><button id="prev" aria-label="Previous slide">\u2190</button><span id="progress" class="progress" aria-live="polite"></span><button id="next" aria-label="Next slide">\u2192</button><button id="notes" aria-pressed="false">Notes</button><button id="print">Print / PDF</button></nav><script>' + JS + '</script></body></html>\n').encode('utf-8')


def approve(args=None):
    """Retired sharing-consent entry point. Never inspect the supplied arguments."""
    raise KitError(LOCAL_ONLY_POLICY)


def submit(bundle=None, gh=None):
    """Retired export entry point. Never read a bundle or touch authentication."""
    raise KitError(LOCAL_ONLY_POLICY)


def main(argv=None):
    arguments = list(sys.argv[1:] if argv is None else argv)
    # Reject old invocations before argument conversion, file access, or imports
    # of any optional export dependency. Old consent and override flags are inert.
    if arguments and arguments[0] in ("approve", "submit"):
        print(f"Stopped: {LOCAL_ONLY_POLICY}", file=sys.stderr)
        return 1
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    renderer = commands.add_parser("render", help="Build a local presentation from an explicitly selected profile.")
    renderer.add_argument("profile", type=Path)
    renderer.add_argument("--output", type=Path, required=True)
    commands.add_parser("approve", help="Disabled: sharing consent is unavailable under the local-only policy.")
    commands.add_parser("submit", help="Disabled: capture export is unavailable under the local-only policy.")
    args = parser.parse_args(arguments)
    try:
        output = args.output.expanduser().absolute()
        require(output != args.profile.expanduser().absolute() and not output.is_symlink(), "Output must be a separate regular file.")
        output.write_bytes(render(read_file(args.profile.expanduser())))
        print(f"Local presentation ready for review: {output}")
    except (KitError, OSError) as exc:
        print(f"Stopped: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
