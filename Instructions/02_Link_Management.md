# 🚨 02_Link Management

## Most Important Principle: Maintaining Zero Broken Links

### 【Absolute Compliance】Mandatory Process When Creating [[]] Links

**Always execute the following when creating [[]] links:**

```text
【Required Steps】
1. 【Important】If link name contains slashes, replace with underscore
   Example: [[CI/CD]] → [[CI_CD]], [[HTML/CSS]] → [[HTML_CSS]]
   Reason: Obsidian interprets slashes as directory separators
2. Use file_search tool to verify corresponding file existence
3. If file doesn't exist, create it immediately before adding [[]] link
4. If new [[]] links are used within created file, repeat steps 1-3
5. Intermediate check: Use grep_search to check for broken links
6. Final verification: Double-check with semantic_search for broken links
```

### 【Enhanced】Broken Link Check Frequency

**Mandatory checkpoints during work process:**

```text
【Broken Link Check Execution Timing】
1. Immediately after creating new file
2. Immediately after adding [[]] link (after each addition)
3. After completing file editing
4. After updating index
5. After completing work section
6. Final verification before completing all work (execute 2 times)

【Tools to Use】
- grep_search: Search links with "\\[\\[.*\\]\\]" pattern
- file_search: Individual file existence verification
- semantic_search: Comprehensive link integrity verification
```

### 【Newly Added】Zero Broken Links Guarantee Protocol

**Strictly comply with the following in all work:**

```text
【Zero Tolerance Rule】
1. 【Important】If link name contains slashes, replace with underscore before creating link
   Example: Process [[CI/CD]] → [[CI_CD]]
2. Always verify existence with file_search before writing [[]] link
3. If file doesn't exist, pause work and create file
4. If multiple [[]] links exist in one file, verify and create one by one in order
5. After file creation, immediately check for broken links with grep_search
6. If even one error is detected, prohibit next work until all are fixed

【Multi-stage Verification System】
- Stage 1: Individual file verification with file_search
- Stage 2: Link pattern search with grep_search
- Stage 3: Comprehensive integrity verification with semantic_search
- Stage 4: Cross-verification with file structure index
```

## **MANDATORY: Broken Link Detection with Python Tools**

**All broken link repair work MUST start by executing the following Python script:**

```bash
# 1. Batch broken link detection (MANDATORY EXECUTION)
python link_checker.py

# Output interpretation:
# - "Broken links: 0 items" = 0 broken links (work completed)
# - "Broken links: X items" = X broken links exist (repair needed)
# - "Broken link ranking (by frequency)" = File creation priority list
# - Reference count priority display (create in order of highest frequency)

# 2. Recommended creation order (by reference count)
# - OpenAI API (23 times) → Words/Tools/OpenAI API.md
# - Azure (10 times) → Words/Cloud/Azure.md
# - Automation (6 times) → Words/Programming/Automation.md
# - Screening (5 times) → Words/Finance/Screening.md
```

**【CRITICAL RULE】Python Tool Usage is MANDATORY for Link Checking:**

- **NEVER** use only grep_search or semantic_search for broken link detection
- **ALWAYS** execute `python link_checker.py` as the primary method
- **ALWAYS** create files in order of reference frequency (highest first)
- Other tools are for supplementary verification only

**【Efficiency】Recommended Batch Work Procedure:**

1. **Execute python link_checker.py** → Get list of files to create
2. **Create 10-15 files in batch** → Bulk creation in order of high frequency
3. **Check and unify notation variations** → Merge/redirect similar name files
4. **Execute python link_checker.py again** → Confirm progress and remaining tasks
5. **Next batch creation** → Repeat until session termination condition achieved

## Batch Work Protocol (10 files/set)

### Phase 1: Preparation and Planning

```bash
# 1. Current status assessment (MANDATORY EXECUTION)
python link_checker.py

# Confirm from output:
# - Total broken link count
# - Priority file list (by reference count)
# - Notation variation candidates
```

### Phase 2: Batch Execution (10 files at a time)

```text
【1 Set Work Scope】
- Select top 10 priority items
- Determine appropriate placement directory for each file
- Bulk create 10 files (parallel work recommended)
- If new [[]] links are created during creation, temporarily list them (handle in next set)

【Quality Standards for File Creation】
- Minimum 100 characters of specific content
- Include 2-3 related [[]] links
- Ensure category compatibility
- Basic Markdown structure (headings, lists, etc.)
```

### Phase 3: Verification and Correction

```bash
# 2. Verification after batch creation (MANDATORY EXECUTION)
python link_checker.py

# Confirmation items:
# - Confirm reduction in broken link count
# - Understand newly generated [[]] links
# - Detect notation variation patterns
```

### Phase 4: Notation Variation Unification

```text
【Unification Work Execution】
1. Detect different notations of same concept (e.g., "CI/CD", "CI-CD", "CI CD")
2. Select optimal notation (judge by generality, completeness, readability)
3. Create sub-files (redirect description)
4. Add alias information to main file
```

### Notation Variation Unification Rules

For different notations of same concept (e.g., OpenAI API vs OpenAI-API), unify as follows:

1. **Main file selection**: Adopt the most general and complete notation
1. **Sub-file creation**: Notation variation files have concise redirect description

```markdown
# OpenAI-API

Synonymous with [[OpenAI API]]. API service provided by OpenAI.

Please refer to [[OpenAI API]] for details.
```

1. **Unification principle**: Space separation > Hyphen separation > Underscore separation

### Phase 5: Transition to Next Set

```text
【Continuation Decision】
- 0 broken links → Work completed
- Broken links remaining → Select next 10 file set and return to Phase 2
- Notation variations detected → Prioritize Phase 4 execution

【Progress Report】
Record the following upon completion of each batch:
- Files created: X files
- Broken links reduced: Y → Z files
- Notation variations unified: N files
- Estimated remaining work time: W minutes
```

## **CRITICAL: Python Tool Usage Requirements**

- **MANDATORY**: Use `python link_checker.py` for ALL broken link detection
- **MANDATORY**: Create files in order of reference frequency (highest first)
- **NEVER**: Rely solely on grep_search or semantic_search for link checking
- Always double-check with grep_search/semantic_search after tool execution
- Manually update "File Structure Index.md" after automatic repair
- Placeholders ([[Term Name]], [[Related Term 1]], etc.) are not actual broken links
- Only repair broken links with specific file names

### SUMMARY: Python-First Approach

1. **Primary**: `python link_checker.py` (provides frequency-sorted broken link list)
1. **Create files**: In order of reference count (high → low priority)
1. **Verify**: Use grep_search/semantic_search for supplementary confirmation
1. **Repeat**: Until broken links = 0
