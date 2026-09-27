# スタイルと実装の規則

同梱コンポーネントを**改造するとき**、また周りのレイアウトや**React版がない部品を自作するとき**に読む。
この規則は、上流リポジトリの開発方針（`development-policy.mdx`）と開発者向けルール（`component-rules`）から、利用する側に関係する部分を抜き出したもの。守ると、同梱コンポーネントと見た目・ふるまいがそろう。

## トークン（@digital-go-jp/tailwind-theme-plugin v1.0.1）

素の Tailwind の値ではなく、DADSのトークンを使う。素の値を混ぜると、色・文字・角丸がDADSの段階からずれる。

### 色

| 用途 | クラス例 |
|---|---|
| 本文の文字 | `text-solid-gray-900`（本文）、`text-solid-gray-800` / `text-solid-gray-700`（補足） |
| 背景・区切り | `bg-white`、`bg-solid-gray-50`、`border-solid-gray-420`、`border-solid-gray-536` |
| キーカラー（操作・強調） | `key-50` 〜 `key-1200`（ボタンは `bg-key-900`） |
| 状態 | `success-1/2`、`error-1/2`、`warning-yellow-1/2`、`warning-orange-1/2` |
| フォーカス | `focus-yellow`、`focus-blue` |
| 色相パレット | `blue` `light-blue` `cyan` `green` `lime` `yellow` `orange` `red` `magenta` `purple`（各 50〜1200） |
| グレー | `solid-gray-*`（50,100,200,300,400,420,500,536,600,700,800,900）、`opacity-gray-*` |

`text-blue-500` のような素の Tailwind の色は使わない（`white` と `black` は例外）。

### 文字（1つのクラスで、サイズ・太さ・行の高さ・字間がまとめて決まる）

書式は `text-{種類}-{サイズ}{N=通常 | B=太字}-{行の高さ×100}`。

- `std-*`：標準の本文・見出し。例：`text-std-16N-170`（本文）、`text-std-24B-150`（見出し）
- `dns-*`：詰めた表示（表やUI部品の中）。例：`text-dns-16N-130`
- `oln-*`：1行のラベル（ボタンなど）。例：`text-oln-16B-100`
- `mono-*`：等幅
- `dsp-*`：ディスプレイ用の大きな見出し

`text-lg` や `leading-[1.3]` のような素の値は使わない。行の高さだけを変えたいときは `leading-100` 〜 `leading-175` を使う。

### そのほか

- 角丸：`rounded-4` `rounded-6` `rounded-8` `rounded-12` `rounded-16` `rounded-24` `rounded-32` `rounded-full`（`rounded-md` などは使わない）
- 影（エレベーション）：`shadow-1` 〜 `shadow-8`
- ブレークポイント：`desktop:`（48em 以上）、`desktop-admin:`（62em 以上）。スマホの画面を基準に書き、広い画面向けの指定を `desktop:` で足していく
- 余白：Tailwind 標準の間隔（`p-4`、`gap-6` など）を使ってよい。同梱コードでは、細かい値を `calc(n/16*1rem)` の形で書いている

## ふるまいとアクセシビリティ

- **ネイティブのHTMLを優先する**：`<button>`、`<a>`、`<input>`、`<select>`、`<dialog>`、`<details>` などをまず使い、ARIAは最小限にする。`<div onClick>` をボタン代わりに使わない。
- **フォーカスの見た目**：同梱コードでは次の形にそろえている。自作する部品もこれに合わせる。
  `focus-visible:outline focus-visible:outline-4 focus-visible:outline-black focus-visible:outline-offset-[calc(2/16*1rem)] focus-visible:ring-[calc(2/16*1rem)] focus-visible:ring-yellow-300`
- **無効状態**：同梱コードは、`disabled` 属性ではなく `aria-disabled="true"` を使う場面が多い（フォーカスでき、読み上げで理由が伝わるため）。無効にするときは `aria-disabled` を使う。`Checkbox` や `Radio` のように、自分でクリックを止める部品もある。止めない部品（`Button` など）では、呼び出す側の `onClick` で処理しないようにする。
- **強制カラーモード**（Windowsのハイコントラストなど）：同梱コードの `forced-colors:` クラスは消さない。自作する部品で色だけで状態を表す場合は、`forced-colors:border-[ButtonText]` などを足す。
- **視覚効果を減らす設定**：アニメーションを付けるときは `motion-reduce:` で止める。
- **文字サイズ**：`px` で固定せず、`rem` を使う。ブラウザで文字を大きくする設定を尊重するため。
- **状態は `data-*` 属性で表す**：同梱コードは `data-size`、`data-error` などを要素に付け、`data-[error]:border-error-1` のように見た目を切り替えている。改造するときも、JavaScriptで `className` を分岐させるよりこの形にそろえる。

## フォームを組み立てるときのパターン

フォームの部品は、ラベル・補足・エラーが別々の部品になっている。組み合わせるときは、要素同士を `id` で関連づける。

```tsx
<div className='flex flex-col gap-2'>
  <Label htmlFor='name' size='md'>
    氏名 <RequirementBadge>※必須</RequirementBadge>
  </Label>
  <SupportText id='name-support'>全角で入力してください</SupportText>
  <Input
    id='name'
    aria-describedby={hasError ? 'name-support name-error' : 'name-support'}
    isError={hasError}
    blockSize='lg'
  />
  {hasError && <ErrorText id='name-error'>＊氏名を入力してください</ErrorText>}
</div>
```

`Input` は `isError` を渡すと `aria-invalid` を自動で付ける。props の正確な名前（`isError`、`blockSize`、`size`、`RequirementBadge` の `isOptional` など）は、コピーした `.tsx` の型で確認する。ラジオボタンやチェックボックスをまとめるときは、`<fieldset>` と `Legend` を使う。

## 改造の考え方

- 公式は、**コピーしたコードを直接書き換える**ことを前提にしている。カスタマイズ用の特別な仕組みはない。
- コンポーネント同士の共通化（`BaseButton` のような基底部品）は作らない。プロジェクトごとに要件がずれて、かえって扱いにくくなるため。
- 変えるのは、必要なクラスとpropsだけにする。フォーカス・無効・エラー・強制カラーのクラスは、見た目を変える場合でも残す。
