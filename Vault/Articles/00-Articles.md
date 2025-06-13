# 00-Articles

This folder stores web pages and articles collected using Obsidian Web Clipper and other tools.

## 📁 Category Structure

### Cloud/

Articles related to cloud services and cloud computing

- AWS, Azure, Google Cloud Platform
- Serverless technology
- Cloud-native development

### Finance/

Articles related to finance, investment, and economics

- Stock investment strategies
- Cryptocurrency
- Economic analysis
- Fintech

### Infrastructure/

Articles related to IT infrastructure and system foundations

- Docker, Kubernetes
- Network technology
- Security
- DevOps

### Programming/

Articles related to programming languages and development technologies

- Various programming languages
- Frameworks
- Algorithms
- Software design

### Tools/

Articles related to development tools and software

- IDEs, editors
- Development support tools
- AI tools
- Productivity tools

## 🔧 Directory Management Rules

### When Adding New Categories

When articles that don't fit into existing categories reach 5 or more, consider creating new directories:

1. **Create new directory**: Articles/{new directory name}/
2. **Move related articles**: Move articles from existing directories
3. **Create directory description file**: Articles/{new directory name}/00-Articles-{new directory name}.md (directly under the applicable directory)
4. **Update this index**: Add new category to this file

### Subdirectory Creation Rules

When articles in a single category exceed 10:

1. **Create subcategories by technology/field**
2. **Create subcategory overview files**
3. **Update parent category description**

## 📝 Article Format

All article files should maintain the following format:

```markdown
# Article Title

> **Source**: [Original URL] > **Author**: Author Name
> **Date**: Collection Date

## Summary

Brief summary of article content

## Content

Main article content

## Related Terms

- [[Related Term 1]]
- [[Related Term 2]]

## Tags

#tag1 #tag2 #tag3
```

## 📊 Current Status

**Total Articles**: {To be updated by AI agents}
**Categories**: 5 main categories
**Last Updated**: {To be updated by AI agents}

## 🔗 Related Files

- [[00-Words]] - Term index
- [[00-FileIndex]] - Complete file list
- Individual category overview files in each subdirectory

## 🔄 動的ディレクトリ管理

**AI エージェント向け指示**：既存のカテゴリに適合しない新しい分野の記事が蓄積された場合（3 件以上）、以下の手順で新しいディレクトリを作成してください：

1. **このファイル（00-Articles.md）を更新**：新しいディレクトリの説明をカテゴリ構造セクションに追加
2. **新しいディレクトリを作成**：Articles/{新ディレクトリ名}/
3. **ディレクトリ説明ファイルを作成**：00-Articles-{新ディレクトリ名}.md（ルートディレクトリ Vault/直下）
4. **README.md を更新**：プロジェクトルートの README.md に新しいカテゴリを反映

**新規カテゴリの例**：

- QuantumComputing/ （量子コンピューティング）
- Blockchain/ （ブロックチェーン）
- MachineLearning/ （機械学習・AI）
- GameDevelopment/ （ゲーム開発）
- Biotechnology/ （バイオテクノロジー）

## 🔄 AI エージェントによる自動処理

このフォルダの記事は、AI エージェントが以下の処理を自動実行します：

1. **記事の分析**: 内容を解析し、重要な用語を特定
2. **用語抽出**: 技術用語、人名、サービス名などを抽出
3. **分類処理**: 適切な Words カテゴリに振り分け
4. **リンク生成**: Obsidian の双方向リンクで関連性を構築

## 📝 記事追加時の手順

1. Obsidian Web Clipper で記事をクリップ
2. 適切なカテゴリフォルダに保存
3. AI エージェントに処理を依頼：
   ```
   Articles/[カテゴリ]/[記事名].md を分析して、
   AI_マニュアル.mdに従って用語を抽出し、整理してください。
   ```

## ⚠️ 注意事項

- 著作権に配慮し、必要に応じて要約や引用形式で保存
- 記事のソース URL、取得日時を明記
- 個人情報や機密情報を含む内容は避ける

---

このフォルダは知識ベース構築の入力点として機能し、AI エージェントと連携して自動的に構造化された知識へと変換されます。
