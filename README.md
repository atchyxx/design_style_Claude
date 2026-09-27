# design_style_Claude

Claudeで使うデザイン関連のスキル集。

## スキル一覧

| スキル | 内容 |
|---|---|
| [`dads-react-components`](skills/dads-react-components/SKILL.md) | デジタル庁デザインシステム（DADS）の公式コードスニペット（React版）を同梱し、React + Tailwind CSS で画面・フォーム・部品を実装する |

## dads-react-components

[デジタル庁デザインシステム コードスニペット（React版）](https://github.com/digital-go-jp/design-system-example-components-react)（v2.7.0、2026-09-09）を、Claudeのスキルとしてまとめたもの。

- 45部品のソース（`.tsx` / `.ts` / `.css`）。アップロードできる容量に収めるため、部品ごとに1つのMarkdownにまとめ、Storybookのストーリーや画像は含めていない
- 部品の一覧（用途、DADS公式ページとの対応、依存関係、必要なnpmパッケージ）
- 導入手順、デザイントークンとアクセシビリティの規則
- 部品を依存関係ごと、元のファイル構成に展開してプロジェクトに書き出すスクリプト（`scripts/add_components.py`）

### 使い方

- **Claudeアプリ（claude.ai）**：`skills/dads-react-components` フォルダをZIPにして、設定の「スキル」からアップロードする。
- **Claude Code（全プロジェクト共通）**：`skills/dads-react-components` を `~/.claude/skills/` にコピーする。
- **Claude Code（特定のプロジェクトだけ）**：そのプロジェクトの `.claude/skills/` にコピーする。

入れた後は、「DADSのコンポーネントで提出フォームを作って」のように頼むと、スキルが使われる。

### 公式サンプルの更新を取り込む

```bash
git clone --depth 1 https://github.com/digital-go-jp/design-system-example-components-react /tmp/dads-react
python tools/build_skill.py /tmp/dads-react
```

`assets/` と `references/catalog.md` を作り直す。新しい部品が増えた場合は、スクリプトが知らせるので、`tools/purposes.json` に用途を、`tools/dads_slugs.json` にDADS公式ページとの対応を書き足してから、もう一度実行する。`SKILL.md` とほかの `references/` は手で直す。

## ライセンス・出典

- 同梱しているコードスニペットは、デジタル庁による MIT ライセンスのコード（[`LICENSE`](skills/dads-react-components/assets/LICENSE)）。
- このリポジトリは、デジタル庁の公式のものではない。

出典：デジタル庁デザインシステムウェブサイト https://design.digital.go.jp/dads/ およびデジタル庁GitHub https://github.com/digital-go-jp
