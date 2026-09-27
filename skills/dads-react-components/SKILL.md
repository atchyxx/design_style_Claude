---
name: dads-react-components
description: デジタル庁デザインシステム（DADS）の公式コードスニペット（React版 / design-system-example-components-react、React + Tailwind CSS + TypeScript）を同梱し、それを使ってReactの画面・フォーム・部品を実装する。ボタン、インプット、チェックボックス、ラジオ、セレクト、日付ピッカー、ファイルアップロード、モーダル、タブ、アコーディオン、通知バナー、パンくず、ページネーション、ステップナビゲーション、テーブルなど約50部品のソース、依存関係、導入手順、トークン規則を持つ。「DADSのReactコンポーネント」「デジタル庁デザインシステムで画面を作りたい」「行政・学校・公共サービス向けのアクセシブルなフォームをReactで」「tailwind-theme-pluginの使い方」「DADS準拠のUIをNext.js/Viteで」など、DADSとReact/Tailwind/JSXが同時に関わる依頼では、コンポーネント名が出ていなくても必ずこのスキルを使う。DADSの考え方やガイドラインだけを聞かれた場合は、DADSドキュメント系のスキルを優先する。
---

# DADS React コンポーネント

デジタル庁が公開している**コードスニペット（React版）**を使って、アクセシブルなReactのUIを作るためのスキル。
ソース一式（v2.7.0、2026-09-09、MIT）を `assets/components/` に同梱している。出所は `assets/SOURCE.md` を参照。

コードスニペットはnpmパッケージではない。**必要な部品のソースをプロジェクトにコピーし、プロジェクト自身のコードとして使い、必要に応じて書き換える**、というのが公式の想定である。この前提を外すと（たとえば、存在しないnpmパッケージから `import` するコードを書くと）動かないコードになる。

## 同梱物

| パス | 内容 | 読むタイミング |
|---|---|---|
| `references/catalog.md` | 全コンポーネントの一覧（用途、DADS名、export、依存、必要なnpmパッケージ）と、React版がまだない部品 | 部品を選ぶとき。最初に読む |
| `references/setup.md` | 既存プロジェクトへの導入手順（Tailwindプラグイン、グローバルCSS、フォント、React 19、Tailwind v4、Next.js、キーカラーの変更） | プロジェクトにまだDADSが入っていないとき |
| `references/styling-rules.md` | トークン（色・文字・角丸・ブレークポイント）、フォーカス・無効・強制カラーの扱い、フォームの組み立て方、改造の考え方 | 部品を改造するとき、周りのレイアウトや部品を自作するとき |
| `assets/components/<Name>/` | 各部品の `.tsx` / `.ts` / `.css`、使い方の例 `*.stories.tsx`、設計メモ `component-spec.md`（一部の部品のみ） | 使う部品のpropsや組み立て方を確かめるとき |
| `scripts/add_components.py` | 部品を依存関係ごとプロジェクトにコピーし、必要なnpmパッケージを表示する | ファイルシステムのあるプロジェクトで作業するとき |
| `assets/LICENSE` | MITライセンス本文 | 配布・公開の相談があったとき |

## 進め方

### 1. 環境を確認する

プロジェクトがある場合は、`package.json` と Tailwind の設定を見て、次を確認する。

- React のバージョン（同梱コードは18向け。19でも使えるが、型エラーの修正が要ることがある）
- Tailwind のバージョン（v3向け。v4ならプラグインのv4用CSSを使う。`references/setup.md` 参照）
- `@digital-go-jp/tailwind-theme-plugin` がすでに入っているか
- 部品を置く場所（既存の `components/` の構成に合わせる。例：`src/components/dads/`）

プロジェクトがなく、チャットでコードだけを求められた場合は、4のコピーは行わない。同梱ソースをもとに、そのまま使えるコードを回答に書く。その際、前提になる導入手順（プラグインの設定など）も短く添える。

### 2. 部品を選ぶ

`references/catalog.md` を読み、依頼された画面を部品に分解する。

- 画面の目的に合う部品を選ぶ。たとえば、オン／オフを即座に反映するなら `Switch`、送信時にまとめて確定するなら `Checkbox`。
- 迷う場合や、使い方の規範（いつ使う／使わないか）が大事な場面では、DADSのガイドラインを確認する。DADSドキュメント系のスキルがあればそれを使い、なければ `https://design.digital.go.jp/dads/components/<slug>/` を参照する（slugは一覧の「DADS名 / slug」列）。
- `Card`、`Table`、`Drawer`、`Calendar` は、共通部品ではなく**作例集**（stories）として提供されている。作例から必要なマークアップを取り出して、プロジェクト用の部品にする。
- React版がまだない部品（メガメニュー、モバイルメニュー、目次など）は、そのことをユーザーに伝える。そのうえで、`references/styling-rules.md` に沿って自作する。

### 3. ソースを読んでから使う

使う部品ごとに `assets/components/<Name>/<Name>.tsx` と `<Name>.stories.tsx` を読む。

props の名前や値は、推測すると外れやすい。たとえば、Input の高さは `size` ではなく `blockSize`、Button の種類は `variant='solid-fill' | 'outline' | 'text'`、Switch は `SwitchOnOff` と `SwitchMode` の2つに分かれている。stories には、ラベル・補足テキスト・エラーの組み合わせ方や、`id` と `aria-describedby` による関連づけの実例があるので、組み立て方はそれに倣う。

### 4. プロジェクトにコピーする

```bash
python <このスキルのパス>/scripts/add_components.py Button Input Label ErrorText --dest src/components/dads
```

- 依存する部品（`Slot`、`Button`、`Disclosure` など）も一緒にコピーされる。既存のファイルは上書きしない（上書きするには `--force`）。
- コピーした部品同士は `../Slot` のような相対パスで参照し合うため、同じフォルダの下に並べたままにする。
- 表示された npm パッケージが未導入なら、インストールする。初回は `references/setup.md` の手順で Tailwind も設定する。
- Python が使えない環境では、`assets/components/<Name>/` から `.tsx`・`.ts`・`.css` を手でコピーする。`*.stories.tsx` と `component-spec.md` はコピーしない（Storybook の依存が入ってしまうため）。

### 5. 画面を組み立てる

- 部品は、children で中身を組み立てる前提で作られている（例：`<ModalDialog>` の中に `ModalDialogHeader`、`ModalDialogBody` を並べる）。
- 周りのレイアウトや、自作する部品には DADS のトークンを使う（`text-std-16N-170`、`text-solid-gray-900`、`rounded-8`、`desktop:` など）。素の Tailwind の色や文字サイズを混ぜると、DADS の段階からずれる。詳しくは `references/styling-rules.md`。
- 見出しの階層、ランドマーク（`header` / `nav` / `main` / `footer`）、フォームの `label` と `fieldset` / `legend` を正しく使う。部品が正しくても、組み合わせ方でアクセシビリティは損なわれる。
- 部品を改造する場合も、フォーカス・`aria-disabled`・エラー・`forced-colors:` のクラスは残す。これらは見た目の飾りではなく、キーボード利用者やハイコントラスト表示の利用者のためのものである。

### 6. 確かめる

- 可能なら、型チェックとビルド（`tsc --noEmit`、`npm run build` など）を実行して通ることを確かめる。
- Tailwind の `content` に、コピー先のフォルダが含まれているかを確かめる（含まれていないとスタイルが消える）。
- 確認できたこと（ビルドが通った、など）と、確認していないこと（スクリーンリーダーでの読み上げ、実機での表示など）を分けて報告する。**「DADS準拠」「アクセシビリティ適合」と断定しない。** 同梱コードは WCAG 2.2 AA を目標に作られているが、組み合わせた画面の適合は、別途検証が必要である。

## ライセンスと出典

- コードスニペットは MIT ライセンス。コピーした部品を配布するリポジトリには、`assets/LICENSE` の著作権表示を残す。
- DADS の利用上の注意では、**改変して使う場合は出典の表示は不要**、**改変せずにそのまま公開する場合は出典を表示する**、とされている。記載例：「出典：デジタル庁デザインシステムウェブサイト https://design.digital.go.jp/dads/ およびデジタル庁GitHub https://github.com/digital-go-jp」
- 作ったものを、デジタル庁が作成したもののように見せない。

## 最新版との違い

同梱しているのは 2026-09-09 時点のコード。ユーザーが「最新」を求めた場合や、同梱コードにない部品が必要な場合は、ネットワークが使えれば公式リポジトリ（https://github.com/digital-go-jp/design-system-example-components-react）と Storybook（https://design.digital.go.jp/dads/react/）を確認する。確認できない場合は、同梱版の時点の情報であることを伝える。
