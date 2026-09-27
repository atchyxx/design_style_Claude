#!/usr/bin/env python3
"""Copy DADS React code-snippet components (plus their dependencies) into a project.

Usage:
  python add_components.py Button Checkbox --dest src/components/dads
  python add_components.py --list

Sources are bundled as one Markdown file per component (assets/components/<Name>.md);
this script unpacks each file block back into its original path.

Options:
  --dest DIR        Destination folder (default: src/components/dads)
  --force           Overwrite files that already exist
  --dry-run         Show what would be copied without writing
"""
import argparse
import json
import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
ASSETS = SKILL_DIR / "assets"
COMPONENTS = ASSETS / "components"
MANIFEST = {r["dir"]: r for r in json.loads((ASSETS / "manifest.json").read_text())}
BLOCK = re.compile(r"<!-- file: (?P<path>[^ ]+) -->\n````[a-z]*\n(?P<body>.*?)````\n", re.S)


def unpack(key: str) -> dict:
    text = (COMPONENTS / f"{key.replace('/', '-')}.md").read_text()
    return {m["path"]: m["body"] for m in BLOCK.finditer(text)}


def resolve(name: str) -> str:
    for key in MANIFEST:
        if key.lower() == name.lower() or key.split("/")[-1].lower() == name.lower():
            return key
    sys.exit(f"Unknown component: {name}. Run with --list to see available names.")


def collect(names):
    ordered, seen = [], set()

    def visit(key):
        if key in seen:
            return
        seen.add(key)
        for dep in MANIFEST[key]["deps"]:
            visit(resolve(dep))
        ordered.append(key)

    for n in names:
        visit(resolve(n))
    return ordered


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("names", nargs="*")
    ap.add_argument("--dest", default="src/components/dads")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()

    if args.list or not args.names:
        for key, r in MANIFEST.items():
            tag = " (examples only, not bundled)" if r.get("story_only") else ""
            print(f"{key}{tag}  deps={','.join(r['deps']) or '-'}")
        return

    keys = collect(args.names)
    dest = Path(args.dest)
    npm = set()
    skipped = []
    for key in keys:
        r = MANIFEST[key]
        if r.get("story_only"):
            continue
        npm.update(r["external"])
        # Place deprecated components flat so that '../Slot'-style imports keep working.
        out_dir = dest / key.split("/")[-1]
        for rel, body in unpack(key).items():
            target = out_dir / rel
            if target.exists() and not args.force:
                skipped.append(str(target))
                continue
            print(("would write " if args.dry_run else "write ") + str(target))
            if not args.dry_run:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(body)

    print(f"\nComponents: {', '.join(keys)}")
    if skipped:
        print(f"Skipped {len(skipped)} existing file(s) (use --force to overwrite):")
        for s in skipped:
            print(f"  {s}")
    story_only = [k for k in keys if MANIFEST[k].get("story_only")]
    if story_only:
        print(f"Note: {', '.join(story_only)} exist upstream only as Storybook examples and are not bundled. "
              "See https://design.digital.go.jp/dads/react/ and build your own from the dependencies copied above.")
    base = ["@digital-go-jp/tailwind-theme-plugin"]
    if "Carousel" in keys:
        base.append("@tailwindcss/container-queries")
    print("npm packages needed: " + " ".join(sorted(set(base) | npm)))


if __name__ == "__main__":
    main()
