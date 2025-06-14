# 00-Words-Tags

## Overview

This directory manages tag classification and category organization. It provides a tag system for cross-cutting classification of articles and terms.

## Target Scope

- Technology field tags (programming languages, cloud, infrastructure, etc.)
- Article type tags (tutorial, explanation, comparison, case study, etc.)
- Difficulty level tags (beginner, intermediate, advanced)
- Trend and chronological tags
- Industry and domain-specific tags

## Current Files

This directory currently contains the following files:

- [[00-Words-Tags]] - This directory description file

_When new tag files are added, they will be listed here with actual links to existing files._

## Tag File Structure

Each tag file includes the following information:

- Tag definition and target scope
- List of related articles
- List of related terms
- Sub-tags and related tags
- Usage guidelines

## Related Links

- [[00-Words]] - Main terms collection page
- [[00-Articles]] - Main articles management page

## AI Agent Instructions

When adding tag files to this directory:

1. **Prioritize Using Existing Tags**

   - Always refer to Tags/ directory when creating new files
   - Actively utilize existing tags when applicable
   - Implement appropriate tagging for articles and terms

2. **New Tag Creation Criteria**

   - Create new tags only when existing tags cannot properly classify content
   - Use concise and clear tag names
   - Check for duplication and similarity with existing tags

3. **Tag File Creation Process**

   - Properly set hierarchical structure (parent tags, child tags)
   - Automatically update links to related articles and terms
   - Consider organization and consolidation based on tag usage frequency

4. **Dynamic Generation and Updates**
   - Generate tag files simultaneously when creating articles and terms
   - Update tag files when adding related content
   - Maintain cross-links between tag files

### Tag File Format

```markdown
# {Tag Name}

{Tag definition and scope description}

## Related Articles

- ((Article Title 1))
- ((Article Title 2))

## Related Terms

- ((Term 1))
- ((Term 2))

## Related Tags

- ((Parent Tag)) - Upper concept
- ((Related Tag)) - Cross-cutting relationship
- ((Child Tag)) - Lower concept

## Usage Guidelines

- {Conditions and criteria for using this tag}
- {Application examples and non-application examples}
```

## Update History

- 2025-06-15: Directory description file translated to English
- 2025-06-13: Directory description file created
