# 🛠️ 08_Troubleshooting

## Broken Link Detection and Repair

### Enhanced Detection Procedure

```text
【Enhanced Detection Procedure】
1. Stage 1: Search for "\\[\\[.*\\]\\]" using grep_search
2. Stage 2: Check existence of each link target using file_search
3. Stage 3: Verify link consistency using semantic_search
4. Stage 4: Cross-check with file structure index
5. List non-existent files (detailed records)

【Multi-stage Repair Procedure】
1. Create files following placement rules (one by one)
2. Immediately after creation: Verify existence using file_search
3. Update file structure index
4. After update: Check for broken links using grep_search
5. After complete repair: Comprehensive check using semantic_search
6. Final verification by running all stages again
```

## Common Error Patterns

### 1. Link Names with Slashes (Important)

- **Problem**: Links like ((CI/CD)) where Obsidian interprets slashes as directories
- **Solution**: Replace slashes with underscores
  - Example: ((CI/CD)) → ((CI_CD))
  - Example: ((HTML/CSS)) → ((HTML_CSS))
  - Example: ((Front-end/Back-end)) → ((Front-end_Back-end))

### 2. Special Characters in File Names

- **Problem**: "CI/CD" needs to be converted to "CI-CD.md"
- **Solution**: Replace special characters with hyphens

### 3. Notation Variations

- **Problem**: "JavaScript" vs "Javascript" → Need to decide unified notation
- **Solution**: Follow unification rules in ((06_Duplication Check and Notation Variation Handling))

### 4. Cascading Non-creation

- **Problem**: (([]]) within new files also need verification
- **Solution**: Execute existence checking and creation step by step

## Error Resolution Priority Order

1. **Broken Links (Highest Priority)**: Resolve even if it means stopping all other work
2. **Notation Variations**: Process efficiently as batch work
3. **Category Classification Errors**: Can be postponed (doesn't affect functionality)
4. **Format Issues**: Fix last

## Debug Procedure

### 1. Problem Identification

```bash
# MANDATORY: Batch detection of broken links with Python
python link_checker.py

# Supplementary: Pattern confirmation with grep search
grep_search "\\[\\[.*\\]\\]"
```

**CRITICAL**: Always use `python link_checker.py` as the primary method for broken link detection. This tool provides:

- Frequency-sorted broken link ranking
- Reference count for each broken link
- Priority order for file creation

### 2. Problem Analysis

- **Primary focus**: Reference count from Python tool output
- **Creation priority**: Start with highest frequency broken links
- **Batch planning**: Group 10-15 files per creation batch
- Identify notation variation patterns
- Determine category placement for each file

### 3. Repair Execution

- **MANDATORY**: Create files in frequency order (highest reference count first)
- **Execute python link_checker.py before and after each batch**
- Always execute verification after repair
- Record progress status

### 4. Final Verification

```bash
# MANDATORY final check
python link_checker.py

# Supplementary verification
grep_search "\\[\\[.*\\]\\]"
semantic_search "broken link"
```

- Execute all check items
- Report repair results
- Organize handover items for next work

**Note**: In examples above, we use (()) to avoid creating broken links in documentation. When creating actual content, use [[]] syntax for links to existing files.
