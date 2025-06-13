# 00-FileIndex

This file is an index for AI agents to efficiently check existing files when creating [[]] links.

## Last Updated

2025-06-14

## Root Directory Files

- AI_Manual.md
- AI_Agent_Instructions.md (newly added)
- CONTRIBUTING.md
- README.md
- Usage_Guide.md
- 00-FileIndex.md
- requirements.txt
- link_checker.py
- link_check_report.json

## Articles Directory Structure

```
Articles/
├── 00-Articles.md (English)
├── Cloud/
│   └── 00-Articles-Cloud.md
├── Finance/
│   └── 00-Articles-Finance.md
├── Infrastructure/
│   └── 00-Articles-Infrastructure.md
├── Programming/
│   └── 00-Articles-Programming.md
└── Tools/
    └── 00-Articles-Tools.md
```

## Words Directory Structure

```
Words/
├── 00-Words.md (English)
├── Authors/
│   └── 00-Words-Authors.md
├── Cloud/
│   └── 00-Words-Cloud.md
├── Finance/
│   └── 00-Words-Finance.md
├── Infrastructure/
│   └── 00-Words-Infrastructure.md
├── Programming/
│   └── 00-Words-Programming.md
├── Services/
│   └── 00-Words-Services.md
├── Tags/
│   └── 00-Words-Tags.md
└── Tools/
    └── 00-Words-Tools.md
```

## 既存の用語ファイル一覧

### Authors/

（現在ファイルなし）

### Cloud/

（現在ファイルなし）

### Finance/

（現在ファイルなし）

### Infrastructure/

（現在ファイルなし）

### Programming/

（現在ファイルなし）

### Services/

（現在ファイルなし）

### Tags/

（現在ファイルなし）

### Tools/

（現在ファイルなし）

## AI エージェント向け使用方法

### 1. ファイル存在確認時

新しい[[]]リンクを作成する前に、このインデックスで既存ファイルをチェック：

1. まずこのインデックスで該当ファイルが存在するか確認
2. 存在しない場合は `file_search` ツールで最終確認
3. 存在しない場合は即座にファイル作成
4. 新規作成後、このインデックスを更新

### 2. インデックス更新ルール

ファイルを新規作成した場合、必ずこのインデックスを更新：

```text
【更新手順】
1. 新規作成したファイルパスを該当セクションに追加
2. アルファベット順・あいうえお順で並び替え
3. 最終更新日を更新
4. ファイル作成作業完了を報告
```

### 3. 定期メンテナンス

月 1 回程度、実際のディレクトリ構造と照合して同期を確認

## 注意事項

- このインデックスは AI エージェントの作業効率化のためのもの
- 実際のファイル存在確認は必ず `file_search` ツールで行う
- インデックス更新を忘れずに実行する
- ファイル削除時もインデックスから除去する
