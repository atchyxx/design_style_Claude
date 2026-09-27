#!/usr/bin/env python3
"""Copy DADS React code-snippet components (plus their dependencies) into a project.

Usage:
  python add_components.py Button Checkbox --dest src/components/dads
  python add_components.py --list

Options:
  --dest DIR        Destination folder (default: src/components/dads)
  --with-stories    Also copy *.stories.tsx (usage examples for Storybook users)
  --force           Overwrite files that already exist
  --dry-run         Show what would be copied without writing
"""
import argparse
import json
import shutil
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
ASSETS = SKILL_DIR / "assets"
COMPONENTS = ASSETS / "components"
MANIFEST = {r["dir"]: r for r in json.loads((ASSETS / "manifest.json").read_text())}


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
    ap.add_argument("--with-stories", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()

    if args.list or not args.names:
        for key, r in MANIFEST.items():
            tag = " (stories only)" if r.get("story_only") else ""
            print(f"{key}{tag}  deps={','.join(r['deps']) or '-'}")
        return

    keys = collect(args.names)
    dest = Path(args.dest)
    npm = set()
    skipped = []
    for key in keys:
        r = MANIFEST[key]
        npm.update(r["external"])
        src_dir = COMPONENTS / key
        # Place deprecated components flat so that '../Slot'-style imports keep working.
        out_dir = dest / key.split("/")[-1]
        for f in sorted(src_dir.rglob("*")):
            if not f.is_file() or f.name == "component-spec.md":
                continue
            if f.name.endswith(".stories.tsx") and not args.with_stories:
                continue
            if r.get("story_only") and not args.with_stories:
                continue
            target = out_dir / f.relative_to(src_dir)
            if target.exists() and not args.force:
                skipped.append(str(target))
                continue
            print(("would copy " if args.dry_run else "copy ") + str(target))
            if not args.dry_run:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, target)

    print(f"\nComponents: {', '.join(keys)}")
    if skipped:
        print(f"Skipped {len(skipped)} existing file(s) (use --force to overwrite):")
        for s in skipped:
            print(f"  {s}")
    story_only = [k for k in keys if MANIFEST[k].get("story_only")]
    if story_only:
        print(f"Note: {', '.join(story_only)} ship only as story examples, so nothing was copied for them. "
              f"Read {COMPONENTS}/<Name>/<Name>.stories.tsx and move the markup you need into your own component; "
              "their dependencies above were copied.")
    base = ["@digital-go-jp/tailwind-theme-plugin"]
    if "Carousel" in keys:
        base.append("@tailwindcss/container-queries")
    print("npm packages needed: " + " ".join(sorted(set(base) | npm)))


if __name__ == "__main__":
    main()
