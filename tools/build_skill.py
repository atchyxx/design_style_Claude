"""Rebuild skills/dads-react-components from a clone of design-system-example-components-react.

Usage:
  git clone --depth 1 https://github.com/digital-go-jp/design-system-example-components-react /tmp/dads-react
  python tools/build_skill.py /tmp/dads-react

Regenerates assets/components, assets/manifest.json, assets/SOURCE.md, assets/LICENSE and
references/catalog.md. SKILL.md and the other references are maintained by hand.
Add a Japanese purpose to tools/purposes.json for any new component the script reports.
"""
import json
import sys
import re
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
if len(sys.argv) != 2:
    sys.exit(__doc__)
SRC = Path(sys.argv[1]).resolve()
OUT = HERE.parent / "skills/dads-react-components"
KEEP_EXT = {".tsx", ".ts", ".css", ".md"}

comp_root = SRC / "src/components"
dest_root = OUT / "assets/components"
if dest_root.exists():
    shutil.rmtree(dest_root)

# React component dir -> (DADS slug, Japanese title), taken from the DADS component pages
dads_map = {k: tuple(v) for k, v in json.loads((HERE / "dads_slugs.json").read_text()).items()}

comp_dirs = sorted(
    [d for d in comp_root.iterdir() if d.is_dir() and d.name != "deprecated"]
    + [d for d in (comp_root / "deprecated").iterdir() if d.is_dir()]
)

rows = []
for d in comp_dirs:
    rel = d.relative_to(comp_root)
    files = [
        f for f in d.rglob("*")
        if f.is_file() and f.suffix in KEEP_EXT and not f.name.endswith(".test.tsx") and not f.name.endswith(".test.ts")
    ]
    for f in files:
        target = dest_root / f.relative_to(comp_root)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, target)

    impl = [f for f in files if f.suffix in (".tsx", ".ts") and not f.name.endswith(".stories.tsx")]
    code = "\n".join(f.read_text() for f in impl)
    story_only = not re.search(r"export (?:const|function) [A-Z]", code)
    if story_only:
        code = "\n".join(f.read_text() for f in files if f.name.endswith(".stories.tsx"))
        code = re.sub(r"from '(@storybook|storybook)[^']*'", "", code)
    deps = sorted({m for m in re.findall(r"from '\.\./(?:\.\./)?([A-Z][A-Za-z]+)'", code) if m != d.name})
    ext = sorted({m for m in re.findall(r"from '([^'.][^']*)'", code) if m not in ("react", "react-dom")})
    exports = sorted(set(re.findall(r"export (?:const|function|type) ([A-Za-z]+)", code)))
    exports = [e for e in exports if not e.endswith("Props") and e[0].isupper()] or exports
    if story_only:
        exports = ["（作例のみ：stories を参照）"]
    slug, title = dads_map.get(str(rel), ("", ""))
    rows.append({
        "dir": str(rel),
        "title": title,
        "dads_slug": slug,
        "deps": deps,
        "external": ext,
        "has_spec": (d / "component-spec.md").exists(),
        "has_stories": any(f.name.endswith(".stories.tsx") for f in files),
        "exports": exports,
        "story_only": story_only,
    })

(OUT / "assets").mkdir(parents=True, exist_ok=True)
(OUT / "assets/manifest.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2))
shutil.copy2(SRC / "LICENSE", OUT / "assets/LICENSE")

commit = subprocess.check_output(["git", "-C", str(SRC), "rev-parse", "HEAD"], text=True).strip()
date = subprocess.check_output(["git", "-C", str(SRC), "log", "-1", "--format=%cs"], text=True).strip()
version = json.loads((SRC / "package.json").read_text())["version"]
(OUT / "assets/SOURCE.md").write_text(
    f"# 同梱ソースの出所\n\n"
    f"- リポジトリ: https://github.com/digital-go-jp/design-system-example-components-react\n"
    f"- バージョン: {version}\n- コミット: {commit}（{date}）\n- ライセンス: MIT（`LICENSE` 参照）\n\n"
    f"同梱しているのは `src/components/` 配下の実装（.tsx/.ts/.css）、Storybookのストーリー（`*.stories.tsx`、使い方の例として）、"
    f"`component-spec.md` です。画像・テスト・MDXは含めていません。\n"
)

# Catalog table (Japanese purpose column is maintained by hand in PURPOSES below)
PURPOSES = json.loads((HERE / "purposes.json").read_text())
lines = [
    "# コンポーネント一覧（React版コードスニペット）",
    "",
    f"同梱版: v{version}（{date}）。「依存」はコピー時に一緒に必要な同梱コンポーネント、「外部」はnpmパッケージ。",
    "DADSページは DADS公式サイト `https://design.digital.go.jp/dads/components/<slug>/` に対応。",
    "",
    "| コンポーネント（フォルダ） | DADS名 / slug | 用途 | 主なexport | 依存 | 外部 |",
    "|---|---|---|---|---|---|",
]
for r in rows:
    name = r["dir"]
    purpose = PURPOSES.get(name, "")
    dads = f"{r['title']} / `{r['dads_slug']}`" if r["dads_slug"] else "—"
    lines.append(
        f"| `{name}` | {dads} | {purpose} | {', '.join(r['exports'][:6])} | {', '.join(r['deps']) or '—'} | {', '.join(r['external']) or '—'} |"
    )
missing = [k for k in PURPOSES if k not in {r['dir'] for r in rows}]
lines += [
    "",
    "## React版がまだないDADSコンポーネント（2026-09時点で「提供予定」）",
    "",
    "チップタグ、コンボボックス、ヘッダーコンテナ、メガメニュー、モバイルメニュー、ノーティスブロック、テーブルコントロール、目次（TOC）。",
    "これらが必要なときは、DADSのガイドラインとHTML版（https://github.com/digital-go-jp/design-system-example-components-html）を参照して、",
    "既存コンポーネントのスタイル規則（`references/styling-rules.md`）に合わせて自作する。",
]
(OUT / "references").mkdir(parents=True, exist_ok=True)
(OUT / "references/catalog.md").write_text("\n".join(lines) + "\n")
print(f"{len(rows)} components; missing purposes: {[r['dir'] for r in rows if r['dir'] not in PURPOSES]}; stale: {missing}")
