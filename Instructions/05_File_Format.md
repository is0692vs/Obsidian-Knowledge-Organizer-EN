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

{Concise summary of the article}

## Content

{Article main text (with [[]] links)}

## Main Technologies and Concepts

- [[Technology1]]
- [[Technology2]]
- [[Technology3]]

## Related Articles

- [[Related Article1]]
- [[Related Article2]]

## Tags

- [[Tag1]]
- [[Tag2]]

## Reference Information

- Author: [[Author Name]]
- Original URL: {URL (if available)}
- Added Date: {Date}
```

## Author Files (under Words/Authors/)

```markdown
# {Author Name}

## List of Written Articles

- [[Article Title1]]
- [[Article Title2]]
- [[Article Title3]]

## Organization

{Affiliated organization/company name (if no information available, write "(No information)")}
```

### ⚠️ Author File Recording Rules

- **Recording content is limited to "List of Written Articles" and "Organization" only**
- Do not record profile, specialties, or personal information
- Record only objective information about article links and organizational information
