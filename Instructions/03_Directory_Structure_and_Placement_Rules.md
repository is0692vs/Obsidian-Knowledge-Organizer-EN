# 📁 03_Directory Structure and Placement Rules

## Directory Structure

```text
Knowledge Base/
├── Articles/            # Organized articles
│   ├── Programming/     # Programming related articles
│   │   └── 00-Articles-Programming.md  # Description file
│   ├── Tools/           # Tool related articles
│   │   └── 00-Articles-Tools.md        # Description file
│   ├── Infrastructure/  # Infrastructure related articles
│   │   └── 00-Articles-Infrastructure.md # Description file
│   ├── Cloud/           # Cloud related articles
│   │   └── 00-Articles-Cloud.md        # Description file
│   ├── Finance/         # Investment related articles
│   │   └── 00-Articles-Finance.md      # Description file
│   └── 00-Articles.md      # Article index
├── Clippings/           # Original article clips (temporary storage)
├── Words/               # Glossary
│   ├── Programming/     # Programming related terms
│   │   └── 00-Words-Programming.md     # Description file
│   ├── Tools/           # Tool related terms
│   │   └── 00-Words-Tools.md           # Description file
│   ├── Infrastructure/  # Infrastructure related terms
│   │   └── 00-Words-Infrastructure.md  # Description file
│   ├── Cloud/           # Cloud related terms
│   │   └── 00-Words-Cloud.md           # Description file
│   ├── Finance/         # Investment related terms
│   │   └── 00-Words-Finance.md         # Description file
│   ├── Authors/         # Author information
│   │   └── 00-Words-Authors.md         # Description file
│   ├── Services/        # Service information
│   │   └── 00-Words-Services.md        # Description file
│   ├── Tags/            # Tag classification
│   │   └── 00-Words-Tags.md            # Description file
│   └── 00-Words.md         # Term index
├── 00-FileIndex.md # Complete file list
└── AI_Manual.md     # Detailed manual (reference)
```

### ⚠️ Description File Naming Rules

**New Rule: Numbered parent directory name-child directory name.md**

**Two naming options:**

#### Option 1: Leading number (displays at top)

- `Articles/Cloud/` → `Articles/Cloud/00-Articles-Cloud.md`
- `Words/Cloud/` → `Words/Cloud/00-Words-Cloud.md`
- `Words/Programming/` → `Words/Programming/00-Words-Programming.md`

#### オプション 2：末尾番号（一番下に表示）

- `Articles/Cloud/` → `Articles/Cloud/ZZ-Articles-Cloud.md`
- `Words/Cloud/` → `Words/Cloud/ZZ-Words-Cloud.md`
- `Words/Programming/` → `Words/Programming/ZZ-Words-Programming.md`

**推奨：オプション 1（先頭番号）**

- ABC 順ソート時に説明ファイルが最上位に表示
- ディレクトリを開いた時に即座に説明ファイルが目に入る
- 新規ファイル追加時も常に見つけやすい位置を維持

**この命名規則により：**

- ファイル名だけで配置場所が特定可能
- ABC 順ソート時に説明ファイルが目立つ位置に固定
- 説明ファイルが対応するディレクトリ直下に配置
- 他のファイルが増えても説明ファイルの視認性を保持

## ファイル配置の判断基準

### 用語ファイル配置（Words/）

- プログラミング言語・フレームワーク・技法 → `Words/Programming/`
- 開発ツール・AI 技術・ソフトウェア → `Words/Tools/`
- クラウドサービス・プロバイダー → `Words/Cloud/`
- インフラ技術・サーバー・ネットワーク → `Words/Infrastructure/`
- 投資・金融・経済用語 → `Words/Finance/`
- 人名・著者・開発者 → `Words/Authors/`

### 記事ファイル配置（Articles/）

- プログラミング関連記事 → `Articles/Programming/`
- ツール紹介・使い方記事 → `Articles/Tools/`
- インフラ構築・運用記事 → `Articles/Infrastructure/`
- クラウド活用記事 → `Articles/Cloud/`
- 投資・資産運用記事 → `Articles/Finance/`

## Words/ 説明ファイルの階層リンク構造

### 基本設計原則

**各ディレクトリ直下の同名.md 説明ファイルは、00-FileIndex.md の小型版として機能します：**

- グラフビューでの意味のある階層構造を形成
- ディレクトリ内の全用語ファイルへの[[]]リンクを体系的に整理
- カテゴリ別の階層構造で知識のネットワーク化を実現

### 説明ファイルの構造パターン

**必須セクション構成：**

```markdown
# ディレクトリ名

## 概要

グラフビューでの階層的な知識ネットワーク形成を明記

## 主要カテゴリ

### カテゴリ 1 名

- [[用語1]] - 簡潔な説明
- [[用語2]] - 簡潔な説明

### カテゴリ 2 名

- [[用語3]] - 簡潔な説明
- [[用語4]] - 簡潔な説明

## サブディレクトリ

- [[00-Words-Programming-Languages]] - プログラミング言語専門用語
- [[00-Words-Programming-Frameworks]] - フレームワーク関連用語

## サブディレクトリ構想

将来的なサブディレクトリ分割の指針
```

### ⚠️ 説明ファイルリンク構造の必須ルール

**各説明ファイルは以下に必ずリンクする：**

1. **同ディレクトリ内の全 md ファイル**
   - 例：`Words/Programming/`内の`オブジェクト指向.md`、`コンパイル.md`等
2. **サブディレクトリの説明ファイル**

   - 例：`Words/Programming/Languages/`配下がある場合は`Words-Programming-Languages.md`
   - サブディレクトリ命名規則：`親-子-孫.md`

3. **リンク更新のタイミング**
   - 新規ファイル作成時：即座に説明ファイルを更新
   - サブディレクトリ作成時：親の説明ファイルにサブディレクトリリンクを追加
   - ファイル移動時：移動元・移動先の説明ファイルを両方更新

### 説明ファイル更新タイミング

**新規用語ファイル作成時：**

1. 用語ファイル作成後、即座に対応する説明ファイルを確認
2. 適切なカテゴリに[[]]リンクを追加
3. 必要に応じてカテゴリ構造を調整
4. 5 件を超える場合はサブディレクトリ化を検討

**サブディレクトリ作成時：**

1. 新サブディレクトリの説明ファイル作成（`親-子.md`形式）
2. 親ディレクトリの説明ファイルに「サブディレクトリ」セクション追加
3. 移動ファイルのリンクを親から削除、サブの説明ファイルに追加

**説明ファイル編集の必須チェック項目：**

- ✅ 同ディレクトリ内の全 md ファイルへの[[]]リンクが存在
- ✅ 全サブディレクトリの説明ファイルへの[[]]リンクが存在
- ✅ カテゴリ分類が論理的に整理
- ✅ 階層構造がグラフビューで意味をなす
- ✅ リンク切れが存在しない

### ディレクトリ別カテゴリ設計指針

#### Programming/

- プログラミング言語、Web 開発・フレームワーク、開発手法・設計、開発プロセス・実践、AI・先端技術、開発・学習リソース

#### Infrastructure/

- コンテナ・仮想化技術、ネットワーク・セキュリティ、アーキテクチャ・サービス、運用・開発プロセス

#### Tools/

- IDE・エディタ・開発環境、AI ツール・支援開発、バージョン管理・パッケージ管理、ナレッジ管理・文書化

#### Services/

- 開発・情報共有プラットフォーム

#### Authors/

- 技術系記事執筆者（専門分野別）

#### Tags/、Finance/、Cloud/

- 現在は個別ファイル未作成、将来的な分類構想を記載

## Articles/ 説明ファイルの階層リンク構造

### Articles/ 基本設計原則

**各ディレクトリ直下の同名.md 説明ファイルは、記事管理のインデックスとして機能します：**

- グラフビューでの意味のある階層構造を形成
- ディレクトリ内の全記事ファイルへの[[]]リンクを体系的に整理
- カテゴリ別の階層構造で記事のネットワーク化を実現

### Articles/ 説明ファイルの構造パターン

**必須セクション構成：**

```markdown
# ディレクトリ名

## 概要

グラフビューでの階層的な知識ネットワーク形成を明記

## 収録記事

### カテゴリ 1 名

- [[記事タイトル1]] - 簡潔な内容説明
- [[記事タイトル2]] - 簡潔な内容説明

### カテゴリ 2 名

- [[記事タイトル3]] - 簡潔な内容説明
- [[記事タイトル4]] - 簡潔な内容説明

## サブディレクトリ

- [[Articles-Programming-WebDev]] - Web 開発関連記事
- [[Articles-Programming-Languages]] - プログラミング言語記事

## サブディレクトリ構想

将来的なサブディレクトリ分割の指針
```

### ⚠️ Articles 説明ファイルリンク構造の必須ルール

**各説明ファイルは以下に必ずリンクする：**

1. **同ディレクトリ内の全記事 md ファイル**
   - 例：`Articles/Programming/`内の記事ファイル全て
2. **サブディレクトリの説明ファイル**
   - 例：`Articles/Programming/WebDev/`配下がある場合は`Articles-Programming-WebDev.md`
   - サブディレクトリ命名規則：`Articles-親-子.md`

### Articles/ 説明ファイル更新タイミング

**新規記事ファイル作成時：**

1. 記事ファイル作成後、即座に対応する説明ファイルを確認
2. 適切なカテゴリに[[]]リンクを追加
3. 必要に応じてカテゴリ構造を調整
4. 5 件を超える場合はサブディレクトリ化を検討

**サブディレクトリ作成時：**

1. 新サブディレクトリの説明ファイル作成（`Articles-親-子.md`形式）
2. 親ディレクトリの説明ファイルに「サブディレクトリ」セクション追加
3. 移動記事のリンクを親から削除、サブの説明ファイルに追加

**説明ファイル編集の必須チェック項目：**

- ✅ 同ディレクトリ内の全記事ファイルへの[[]]リンクが存在
- ✅ 全サブディレクトリの説明ファイルへの[[]]リンクが存在
- ✅ カテゴリ分類が論理的に整理
- ✅ 階層構造がグラフビューで意味をなす
- ✅ リンク切れが存在しない

### Articles/ ディレクトリ別カテゴリ設計指針

#### Articles/Programming/

- Python・Web 開発記事、言語別記事、フレームワーク記事、アルゴリズム記事

#### Articles/Infrastructure/

- Docker・コンテナ技術記事、ネットワーク技術記事、セキュリティ記事、DevOps 記事

#### Articles/Tools/

- AI 支援開発ツール記事、IDE・エディタ記事、バージョン管理記事、生産性向上ツール記事

#### Articles/Cloud/、Articles/Finance/

- 現在は個別記事未作成、将来的な分類構想を記載

## STEP 2.5: .gitignore ファイルの更新【重要】

新しいサブディレクトリを作成した場合、.gitignore ファイルに説明ファイルの除外設定を追加してください：

```gitignore
# 新しいサブディレクトリの説明ファイルも追跡する
!Vault/Articles/新ディレクトリ名/新ディレクトリ名.md
!Vault/Words/新ディレクトリ名/新ディレクトリ名.md
```

## ディレクトリとファイルの作成

1. 新しいディレクトリを作成
2. ディレクトリ直下に「ディレクトリ名.md」形式で説明ファイルを作成
3. 関連する記事・用語ファイルを新ディレクトリに移動

## サブディレクトリ自動作成ルール

### 作成判断基準

**同一カテゴリのファイルが 4 つ以上蓄積し、かつ他の異なるカテゴリのファイルも存在する場合、サブディレクトリを作成する**

#### 具体例

**Words/Programming/に以下のファイルが存在する場合：**

- C.md
- Java.md
- Python.md
- JavaScript.md
- オブジェクト指向.md
- 関数型プログラミング.md

→ プログラミング言語（4 つ）と プログラミング概念（2 つ）が混在
→ `Words/Programming/Languages/` サブディレクトリを作成

**作成しない例：**

- C.md、Java.md、Python.md の 3 つのみ → 4 つ未満なので作成しない
- プログラミング言語のみで他のカテゴリが存在しない → 分割の意味がないので作成しない

### 作成手順

```text
【サブディレクトリ作成プロセス】
1. 対象ディレクトリ内のファイル分析・カテゴリ分類
2. 4つ以上の同一カテゴリと他カテゴリの混在を確認
3. 適切なサブディレクトリ名を決定
   例：Languages（言語）、Frameworks（フレームワーク）、Concepts（概念）
4. サブディレクトリの作成
5. サブディレクトリ直下に同名の説明.mdファイルを作成
6. 該当ファイルをサブディレクトリに移動
7. 親ディレクトリの説明ファイルを更新
8. 00-FileIndex.mdを更新
9. リンク切れチェック実行
```

### 推奨サブディレクトリ名

#### Words/Programming/配下

- **Languages/** - プログラミング言語（C、Java、Python 等）
- **Frameworks/** - フレームワーク（React、Vue、Django 等）
- **Concepts/** - プログラミング概念（オブジェクト指向、関数型等）
- **Tools/** - 開発ツール（IDE、デバッガー等）

#### Words/Infrastructure/配下

- **Containers/** - コンテナ技術（Docker、Kubernetes 等）
- **Networks/** - ネットワーク技術（TCP/IP、DNS 等）
- **Security/** - セキュリティ技術（暗号化、認証等）

#### Words/Tools/配下

- **Editors/** - エディタ・IDE（VSCode、IntelliJ 等）
- **AI/** - AI ツール（GitHub Copilot、ChatGPT 等）
- **VersionControl/** - バージョン管理（Git、SVN 等）

### サブディレクトリ説明ファイルのテンプレート

```markdown
# サブディレクトリ名

## 概要

このディレクトリは[親ディレクトリ名]の[カテゴリ名]に関する用語を整理しています。
グラフビューでの階層的な知識ネットワーク形成を目的としています。

## 収録用語

### [サブカテゴリ 1]

- [[用語1]] - 簡潔な説明
- [[用語2]] - 簡潔な説明

### [サブカテゴリ 2]

- [[用語3]] - 簡潔な説明
- [[用語4]] - 簡潔な説明

## 関連ディレクトリ

- [[00-Words-Programming]] - 親ディレクトリ（必須）
- [[00-Words-Tools]] - 関連する他のディレクトリ

## 追加指針

さらに細分化が必要になった場合の指針を記載
```

### ⚠️ サブディレクトリ説明ファイル必須要素

**各サブディレクトリ説明ファイルは：**

1. **収録されている全ファイルにリンク**
2. **親ディレクトリの説明ファイルにリンク**（必須）
3. **関連する他のディレクトリにもリンク**

### 実行タイミング

**自動作成を検討すべきタイミング：**

1. 新規用語ファイル作成時
2. 既存ディレクトリの整理時
3. 月次メンテナンス時
4. カテゴリ分析時

**チェック項目：**

- ✅ 同一カテゴリに 4 つ以上のファイル
- ✅ 他カテゴリのファイルも存在
- ✅ 論理的な分割が可能
- ✅ サブディレクトリ名が適切
