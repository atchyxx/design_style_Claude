# コンポーネント一覧（React版コードスニペット）

同梱版: v2.7.0（2026-09-09）。「依存」はコピー時に一緒に必要な同梱コンポーネント、「外部」はnpmパッケージ。
DADSページは DADS公式サイト `https://design.digital.go.jp/dads/components/<slug>/` に対応。
ソースは `assets/components/<フォルダ名>.md`（`deprecated/X` は `deprecated-X.md`）。
「作例のみ」の4つ（Calendar・Card・Drawer・Table）は共通部品がなく、同梱していない。Storybook（https://design.digital.go.jp/dads/react/）の作例を参照するか、依存欄の部品とトークンで組み立てる。

| コンポーネント（フォルダ） | DADS名 / slug | 用途 | 主なexport | 依存 | 外部 |
|---|---|---|---|---|---|
| `Accordion` | アコーディオン / `accordion` | 見出しをクリックして詳細を開閉する（FAQなど）。details/summaryベース | Accordion, AccordionBackLink, AccordionContent, AccordionSummary | — | — |
| `Blockquote` | 引用ブロック / `blockquote` | 他の文献・発言の引用 | Blockquote | — | — |
| `Breadcrumbs` | パンくずナビゲーション / `breadcrumb` | サイト階層内の現在位置を示す | BreadcrumbItem, BreadcrumbLink, BreadcrumbList, Breadcrumbs, BreadcrumbsLabel | Slot | — |
| `Button` | ボタン / `button` | 操作の実行・遷移のトリガー。solid-fill / outline / text の3種と大きさ | Button, ButtonSize, ButtonVariant | Slot | — |
| `Calendar` | — | カレンダー表示の作例（react-aria-components使用） | （作例のみ・同梱なし：Storybook参照） | Button, Link, Select | @internationalized/date, react-aria-components |
| `Card` | カード / `card` | カード型レイアウトの作例6種（共通コンポーネントはない） | （作例のみ・同梱なし：Storybook参照） | Button, Checkbox, Link | — |
| `Carousel` | カルーセル / `carousel` | 複数のスライドを切り替えて見せる | Carousel, CarouselSingle, CarouselSingleImage, CarouselSingleLink, CarouselSlide | Disclosure | — |
| `Checkbox` | チェックボックス / `checkbox` | 複数選択・同意のチェック。エラー状態あり | Checkbox, CheckboxSize | — | — |
| `ChipLabel` | チップラベル / `chip-label` | 状態やカテゴリを示す小さなラベル（操作しない） | ChipLabel, ChipLabelColor, ChipLabelVariant | — | — |
| `DatePicker` | 日付ピッカー／カレンダー / `date-picker` | 年・月・日を入力する日付入力（1つの欄） | DatePicker, DatePickerCalendarButton, DatePickerDate, DatePickerMonth, DatePickerSize, DatePickerYear | — | — |
| `Disclosure` | ディスクロージャー / `disclosure` | 補足情報の開閉（アコーディオンより軽い） | Disclosure, DisclosureBackLink, DisclosureSummary | — | — |
| `Divider` | ディバイダー / `divider` | 区切り線 | Divider, DividerColor | — | — |
| `Dl` | 説明リスト / `description-list` | 用語と説明の対（説明リスト） | Dd, Dl, Dt | — | — |
| `Drawer` | ドロワー / `drawer` | 画面端からスライドするメニューの作例 | （作例のみ・同梱なし：Storybook参照） | Divider, HamburgerMenuButton, Link | — |
| `EmergencyBanner` | 緊急時バナー / `emergency-banner` | 災害など緊急時のお知らせ（最上位の警告） | EmergencyBanner, EmergencyBannerBody, EmergencyBannerButton, EmergencyBannerHeading, EmergencyBannerHeadingLevel | — | — |
| `ErrorText` | — | フォーム項目のエラーメッセージ | ErrorText | — | — |
| `FileUpload` | ファイルアップロード／ドロップエリア / `file-upload` | ファイル選択・ドラッグ＆ドロップ・一覧表示 | FileInfo, FileUpload, FileUploadDropArea, FileUploadFileInfo, FileUploadFileItem, FileUploadFileList | — | — |
| `HamburgerMenuButton` | ハンバーガーメニューボタン / `hamburger-menu-button` | モバイル用メニューの開閉ボタン | CloseIcon, CloseWithLabelIcon, HamburgerIcon, HamburgerMenuButton, HamburgerMenuIconButton, HamburgerWithLabelIcon | — | — |
| `Heading` | 見出し / `heading` | 見出し（h1〜h6）。サイズ・肩書き・罫線つき | Heading, HeadingLevel, HeadingShoulder, HeadingSize, HeadingTitle, RuleSize | — | — |
| `HorizontalMenu` | 水平メニュー / `horizontal-menu` | ヘッダー等の横並びナビゲーション | HorizontalMenu, HorizontalMenuItem, HorizontalMenuItemButton, HorizontalMenuItemLink | — | — |
| `Image` | 画像 / `image` | 画像とキャプション | Image, ImageArea, ImageAreaLink, ImageCaption, ImageCaptionStyle | — | — |
| `Input` | インプットテキスト / `input-text` | 1行テキスト入力 | Input, InputBlockSize | — | — |
| `Label` | — | フォーム項目のラベル | Label, LabelSize | — | — |
| `LanguageSelector` | ランゲージセレクター / `language-selector` | 表示言語の切り替え | LanguageSelector, LanguageSelectorArrowIcon, LanguageSelectorButton, LanguageSelectorGlobeIcon, LanguageSelectorGlobeWithLabelIcon, LanguageSelectorMenu | — | — |
| `Legend` | — | fieldset（ラジオ・チェックボックス群）の見出し | Legend, LegendSize | — | — |
| `Link` | — | テキストリンク。外部リンクアイコンつき | Link, LinkExternalLinkIcon | Slot | — |
| `List` | 箇条書きリスト / `list` | 箇条書き・番号付きリスト | List | — | — |
| `MenuList` | メニューリスト / `menu-list` | 縦並びのメニュー（サイドナビなど） | MenuList, MenuListItem, MenuListItemButton, MenuListItemLink, MenuListSize, MenuListType | — | — |
| `MenuListBox` | — | ボタンから開くポップアップメニュー | MenuItemSelectDetail, MenuListBox, MenuListBoxOpener, MenuListBoxOpenerFontWeight, MenuListBoxOpenerSize, MenuListBoxOpenerStyle | — | — |
| `ModalDialog` | モーダルダイアログ / `modal-dialog` | 確認・警告などのモーダルダイアログ（dialog要素） | ModalDialog, ModalDialogActions, ModalDialogBody, ModalDialogClose, ModalDialogContent, ModalDialogHeader | — | — |
| `NotificationBanner` | ノティフィケーションバナー / `notification-banner` | 成功・エラー・警告・情報などのお知らせ枠 | NotificationBanner, NotificationBannerBody, NotificationBannerClose, NotificationBannerHeadingLevel, NotificationBannerIcon, NotificationBannerMobileClose | — | — |
| `PageNavigation` | ページナビゲーション / `page-navigation` | ページ送り（ページネーション） | PageNavigation, PageNavigationArrowButton, PageNavigationArrowButtonSize, PageNavigationButton, PageNavigationControl, PageNavigationCounter | Button, Slot | — |
| `ProgressIndicator` | — | 処理中・進捗の表示（スピナー・バー）。読み上げ対応 | ProgressIndicator, ProgressIndicatorAnnouncerMessages, ProgressIndicatorLinear, ProgressIndicatorSize, ProgressIndicatorSpinner, ProgressIndicatorStatic | — | — |
| `Radio` | ラジオボタン / `radio` | 複数の選択肢から1つを選ぶ | Radio, RadioSize | — | — |
| `RequirementBadge` | — | 「必須」「任意」の表示 | RequirementBadge | — | — |
| `ResourceList` | リソースリスト / `resource-list` | 文書・ファイル・記事などの一覧（行ごとに操作あり） | ResourceList, ResourceListAction, ResourceListActionButton, ResourceListBody, ResourceListContents, ResourceListControl | Slot | — |
| `SearchBox` | 検索ボックス / `search-box` | サイト内検索の入力欄と検索ボタン | SearchBox, SearchBoxDetail, SearchBoxDetailActions, SearchBoxFields, SearchBoxInput, SearchBoxSelect | Button | — |
| `Select` | セレクトボックス / `select` | ドロップダウンから1つ選ぶ（select要素） | Select, SelectBlockSize | — | — |
| `SeparatedDatePicker` | 日付ピッカー／カレンダー / `date-picker` | 年・月・日を別々の欄で入力する日付入力 | SeparatedDatePicker, SeparatedDatePickerCalendarButton, SeparatedDatePickerDate, SeparatedDatePickerMonth, SeparatedDatePickerSize, SeparatedDatePickerYear | — | — |
| `Slot` | — | 子要素にpropsを渡すための内部部品（asChild用） | Slot | — | — |
| `StatusBadge` | — | 件数や状態を示すバッジ | StatusBadge | — | — |
| `StepNavigation` | ステップナビゲーション / `step-navigation` | 申請手続きなどの手順・進捗ステップ | StepNavigation, StepNavigationDescription, StepNavigationList, StepNavigationNumber, StepNavigationStateIndicator, StepNavigationStep | Slot | — |
| `SupportText` | — | フォーム項目の補足説明文 | SupportText | — | — |
| `Switch` | スイッチ / `switch` | オン／オフの即時切り替え | SwitchMode, SwitchOnOff | — | — |
| `Tab` | タブ / `tab` | 同一画面内で表示内容を切り替えるタブ | Tab, TabChangeDetail, TabItem, TabList, TabPanel, TabPosition | — | — |
| `Table` | テーブル／データテーブル / `table` | 表・データテーブルの作例（並べ替え・選択など） | （作例のみ・同梱なし：Storybook参照） | Checkbox, Link, List | — |
| `Textarea` | テキストエリア / `textarea` | 複数行テキスト入力。文字数カウントあり | Textarea | — | — |
| `UtilityLink` | ユーティリティリンク / `utility-link` | フッター等の補助的なリンク | UtilityLink, UtilityLinkExternalLinkIcon | Slot | — |
| `deprecated/ScrollToTopButton` | スクロールトップボタン / `scroll-top-button` | ページ上部へ戻るボタン（非推奨） | ScrollToTopButton | — | — |

## React版がまだないDADSコンポーネント（2026-09時点で「提供予定」）

チップタグ、コンボボックス、ヘッダーコンテナ、メガメニュー、モバイルメニュー、ノーティスブロック、テーブルコントロール、目次（TOC）。
これらが必要なときは、DADSのガイドラインとHTML版（https://github.com/digital-go-jp/design-system-example-components-html）を参照して、
既存コンポーネントのスタイル規則（`references/styling-rules.md`）に合わせて自作する。
