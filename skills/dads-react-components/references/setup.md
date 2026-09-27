# 導入手順（既存のReactプロジェクトへ）

公式の「導入方法」に、同梱コードを実際に動かすときに必要な点を補って書いている。
コードスニペットは**npmパッケージではない**。必要なコンポーネントのソースをプロジェクトにコピーして、プロジェクト自身のコードとして扱う。コピーした後に上流の更新を自動で取り込む仕組みはない。

## 前提

| 項目 | 同梱コードが想定している環境 | 補足 |
|---|---|---|
| React | v18 | v19でも動くが、`forwardRef` や `ComponentProps` まわりで軽い型エラーが出ることがある。その場合は該当箇所を直す |
| Tailwind CSS | v3 | v4の場合は下の「Tailwind v4 の場合」を参照 |
| TypeScript | あり | JSのプロジェクトなら、型注釈を外して `.jsx` にする |

## 1. パッケージを入れる

```bash
npm install @digital-go-jp/tailwind-theme-plugin
# Carousel を使う場合だけ
npm install -D @tailwindcss/container-queries
# Calendar の作例（react-aria-components 版）を使う場合だけ
npm install react-aria-components @internationalized/date
```

`scripts/add_components.py` は、コピーした組み合わせで必要になるパッケージを最後に表示する。

## 2. Tailwind を設定する（v3）

```js
// tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: { extend: {} },
  plugins: [
    require('@digital-go-jp/tailwind-theme-plugin'),
    // require('@tailwindcss/container-queries'), // Carousel を使う場合
  ],
};
```

`"type": "module"` のプロジェクトで `require` が使えない場合は、`import dadsTheme from '@digital-go-jp/tailwind-theme-plugin'` と書いて `plugins: [dadsTheme]` にする。

`content` に、**コンポーネントをコピーした先のフォルダが含まれている**ことを確認する。含まれていないとクラスが生成されず、スタイルが消える。

### Tailwind v4 の場合

プラグインはv4用のCSSも提供している。

```css
@import 'tailwindcss';
@import '@digital-go-jp/tailwind-theme-plugin/v4';
```

ただし、同梱コンポーネントはv3で書かれている。v4では一部のユーティリティ名の変更（`outline-none` の意味、`ring` の初期幅など）で見た目が変わることがあるため、主要な状態（hover・focus-visible・disabled・error）を目で確かめる。

## 3. グローバルCSS（公式Storybookの設定に合わせた最小構成）

```css
/* src/index.css など */
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&display=swap");

@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  body {
    @apply font-sans text-std-17N-170 text-solid-gray-900;
  }
  /* ModalDialog を使う場合：モーダル表示中に背景がスクロールしないように */
  html:has(:modal) { overflow: clip; }
}
```

- フォントは Noto Sans JP が前提（`font-sans` トークンの先頭）。Webフォントを読み込まない場合はOSのフォントで代用される。
- コンポーネントは Tailwind の Preflight（`@tailwind base`）がある前提で書かれている。Preflight を無効にしているプロジェクトでは、ボタンやリストの見た目が崩れる。

## 4. コンポーネントをコピーする

```bash
python <skill>/scripts/add_components.py Button Input Label ErrorText --dest src/components/dads
```

- `Slot` など、依存している同梱コンポーネントも自動で一緒にコピーされる。
- コンポーネント同士は `../Slot` のような相対パスで参照し合っているため、**同じ親フォルダの下に並べて置く**。
- `ProgressIndicator` は `keyframes.css`、`SearchBox` は `search-box.css` をコンポーネント自身がimportする。CSSのimportを扱えるバンドラー（Vite / Next.js など）を前提としている。
- パスエイリアス（`@/components/...`）を使いたい場合も、コピーしたファイル同士の相対importはそのまま残す。

## 5. 使う

```tsx
import { Button } from './components/dads/Button';

<Button variant='solid-fill' size='lg' type='submit'>提出する</Button>
```

propsの正確な名前と値は、コピーした `.tsx` の型定義で確認する。使い方の例は `assets/components/<Name>/<Name>.stories.tsx` にある。

## キーカラーを変える

DADSの `key` カラー（初期値は青系）を、サービスの色に差し替えられる。

```js
theme: {
  extend: {
    colors: {
      key: { 50: '...', 100: '...', /* … */ 900: '#…', 1000: '...', 1100: '...', 1200: '...' },
    },
  },
},
```

差し替えた後は、白い文字を載せる濃さ（ボタンの通常色 `key-900`、hover の `key-1000`、active の `key-1200` など）で、背景との**コントラスト比 4.5:1 以上**が保たれているかを確認する。

## Next.js（App Router）で使う場合

- 多くのコンポーネントは本体にフックを持たないため、Server Components からも使える。
- 本体でフックを使っている `DatePicker`、別ファイルのフック（`useTab`、`useModalDialog`、`useMenuListBox`、`useProgressIndicatorAnnouncer`、FileUpload の `hooks/`）を使う場合、またイベントハンドラを渡す場合は、そのファイルに `'use client'` を付ける（同梱コードには `'use client'` は書かれていない）。
