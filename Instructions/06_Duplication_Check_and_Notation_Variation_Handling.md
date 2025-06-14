# 🔍 06_Duplication Check and Notation Variation Handling

## Duplication Check Procedure

```text
【Required Check Items】
1. Use semantic_search to search for article titles and main keywords
2. Check for similar articles in Articles/ and Clippings/
3. Check for existing articles by the same author
4. Check for identical or similar terms in Words/
```

## Notation Variation Response Principles

### Priority Order

1. **Confusion Avoidance (Highest Priority)**: Notation that won't be confused with other concepts
2. **Memorability**: Easy to remember and use notation
3. **Official Name**: Official names and formal notation

### Response Method

- Primary notation: Include detailed explanatory content
- Secondary notation: Change to concise redirect format

```markdown
# Microsoft Azure

Same as ((Azure)). Cloud computing platform provided by Microsoft.

Please refer to ((Azure)) for details.

## Related Concepts

- ((Azure)) - Main article
```

## Notation Variation Unification Rules

For different notations of the same concept (e.g., OpenAI API vs OpenAI-API), unify as follows:

1. **Main File Selection**: Adopt the most common and complete notation
2. **Sub-file Creation**: Notation variation files should have concise redirect descriptions

```markdown
# OpenAI-API

Same as ((OpenAI API)). API service provided by OpenAI.

Please refer to ((OpenAI API)) for details.
```

3. **Unification Principle**: Space separation > Hyphen separation > Underscore separation

**Note**: In examples above, we use (()) to avoid creating broken links in documentation. When creating actual content, use [[]] syntax for links to existing files.
