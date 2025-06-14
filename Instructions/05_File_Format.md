# 📝 05_File Format

## Description File Naming Rules

**New Rule: Parent directory name-child directory name.md**

- File name alone can identify placement location
- Example: `Articles-Cloud.md`, `Words-Programming.md`
- Placement location: Directly under Vault/ (root directory)
- Solves traditional same-name file problems

## Term Files (under Words/)

```markdown
# {Term Name}

{Concise and accurate definition of the term (1-2 lines)}

## Main Features

- {Feature 1}
- {Feature 2}
- {Feature 3}

## {Field-specific Section}

### {Category 1}

- {Specific explanation}

### {Category 2}

- {Specific explanation}

## Application in ((Personal Development))

(Only when applicable)

- {Practical application methods}
- {Specific benefits}

## Related Concepts

- ((Related Term 1)) - Explanation of relationship
- ((Related Term 2)) - Explanation of relationship

## Tags

- ((Tag1))
- ((Tag2))
```

## Article Files (under Articles/)

```markdown
# {Article Title}

{記事の簡潔な要約}

## 内容

{記事の本文（[[]]リンク付き）}

## 主要な技術・概念

- [[技術1]]
- [[技術2]]
- [[技術3]]

## 関連記事

- [[関連記事1]]
- [[関連記事2]]

## タグ

- [[タグ1]]
- [[タグ2]]

## 参考情報

- 著者：[[著者名]]
- 原文 URL：{URL（もしあれば）}
- 追加日：{日付}
```

## 著者ファイル（Words/Authors/配下）

```markdown
# {著者名}

## 書いた記事一覧

- [[記事タイトル1]]
- [[記事タイトル2]]
- [[記事タイトル3]]

## 組織

{所属組織・会社名（情報がない場合は「（情報なし）」）}
```

### ⚠️ 著者ファイルの記載ルール

- **記載内容は「書いた記事一覧」と「組織」のみに限定**
- プロフィール、専門分野、個人的な情報は記載しない
- 記事とのリンクと組織情報のみを客観的に記載
