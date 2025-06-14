# 🔧 04_Workflow

## 1. Adding New Articles (from Clippings)

```text
【Required Steps】
1. Duplication check (using semantic_search, grep_search)
2. Article content analysis and category determination
3. **Tag classification and utilization**
   → Reference Tags/ subdirectory to identify applicable tags
   → Create new tags if suitable existing tags don't exist
   → Dynamic tag file generation (under Words/Tags/)
   → Apply tags to articles and terms (frontmatter or related links)
4. Term extraction and 【Important】dynamic Words/ file generation
   → For keywords discovered in articles
   → Check existence with file_search
   → Create immediately if non-existent (in appropriate location)
   → Immediately after creation: broken link check with grep_search
   → **Update corresponding description file (00-Words-{CategoryName}.md) simultaneously with creation**
5. Article creation in Articles/ 【Important: Complete preservation of original article content】
   → Never summarize or abbreviate article content
   → Only addition of metadata (frontmatter) is permitted
   → Main text must be moved as-is from original content
   → [[]] link addition must be done without changing main text content
   → For each [[]] link addition: check existence with file_search
6. [[]] link addition (all corresponding files verified)
   → Existence confirmation, creation, and check for each link
   → Intermediate check: broken link confirmation with grep_search
7. Index update
   → After update: link consistency confirmation with semantic_search
   → **Update corresponding description file (00-Articles-{CategoryName}.md)**
8. Delete original file from Clippings/
9. Final broken link check (execute twice)
   → First time: overall check with grep_search
   → Second time: comprehensive confirmation with semantic_search
```

### ⚠️ Important Principles for Article Content Preservation

- **Absolutely prohibited to summarize, shorten, or abbreviate main article content**
- **Maintain information volume and detail level of original article**
- **Changeable elements: Only metadata (frontmatter) and addition of [[]] links**
- **Main text structure, content, and volume must be identical to original article**

### ⚠️ About Words/ File Creation

- Files under Words/ are dynamically generated during article processing
- Created for the first time when keywords appear during article processing
- "Linking to non-existent files" state is absolutely prohibited

### ⚠️ Slash Processing in Link Names【Important】

- **Links containing slashes must be replaced with \_ (underscore)**
- Example: [[CI/CD]] → [[CI_CD]], [[HTML/CSS]] → [[HTML_CSS]]
- Reason: Obsidian misinterprets slashes as directory separators

## 2. Adding [[]] Links to Existing Articles

```text
【Required Steps】
1. Identify important terms in article
2. 【Important】Replace terms containing slashes with _ (e.g., CI/CD → CI_CD)
3. Pre-check with 00-FileIndex.md
4. Final existence confirmation with file_search (for each term)
5. Immediate creation of missing files (dynamic generation)
   → Immediately after creation: broken link check with grep_search
6. [[]] link addition (step by step)
   → After each link addition: re-confirm existence with file_search
   → Intermediate check: broken link confirmation with grep_search
7. 00-FileIndex.md update
   → After update: link consistency confirmation with semantic_search
8. Final broken link check (execute 3 times)
   → First time: overall check with grep_search
   → Second time: comprehensive confirmation with semantic_search
   → Third time: cross-reference with file structure index
```

## 3. Individual Term File Creation (Dynamic Generation)

```text
【Required Steps】
1. Determine appropriate directory
2. **Tag classification and utilization**
   → Reference Tags/ subdirectory to identify applicable tags
   → Create new tags if suitable existing tags don't exist
   → Dynamic tag file generation (under Words/Tags/)
3. 【Important】Replace _ if filename contains slashes
   Example: "CI/CD.md" → Create as "CI_CD.md"
4. File creation (using standard format)
   → Immediately after creation: existence confirmation with file_search
   → **Update corresponding description file (00-Words-{CategoryName}.md) simultaneously with creation**
5. Existence confirmation and dynamic generation before adding related term [[]] links
   → For each [[]] link: existence confirmation with file_search
   → Replace with _ if containing slashes before processing
   → Create immediately if non-existent
   → After creation: broken link check with grep_search
6. 00-FileIndex.md update
   → After update: link consistency confirmation with semantic_search
7. 00-Words.md update
8. Final broken link check (execute twice)
   → First time: overall check with grep_search
   → Second time: comprehensive confirmation with semantic_search
```

## 4. Automatic Subdirectory Creation (During Directory Organization)

```text
【Decision and Execution Steps】
1. Analyze files in target directory
   → Count files of same category
   → Confirm existence of files from different categories
2. Confirm creation conditions
   → 4 or more of same category AND other categories also exist
   → Judge if logical division is possible
3. Determine subdirectory name
   → Reference [[Instructions/03_Directory_Structure_and_Placement_Rules#Recommended Subdirectory Names]]
4. Create subdirectory
   → Create with create_directory tool
5. Create description file
   → Create in "00-ParentDirectoryName-ChildDirectoryName.md" format directly under subdirectory
   → Example: Words/Languages/ → Words/Languages/00-Words-Programming-Languages.md
   → Use [[Instructions/03_Directory_Structure_and_Placement_Rules#Subdirectory Description File Template]]
   → **Add links to all files to be moved**
   → **Add link to parent directory description file**
6. Move files
   → Move relevant files to subdirectory
   → Execute mv command with run_in_terminal
7. Update parent directory description file
   → **Delete links of moved files**
   → **Add link to subdirectory description file in "Subdirectories" section**
   → Adjust category classification
8. Index update
   → Update 00-FileIndex.md
   → Update 00-Words.md (if applicable)
9. Broken link check
   → Confirm link consistency after move with grep_search
   → Comprehensive confirmation with semantic_search
```

### Subdirectory Creation Timing

**When to consider automatic creation:**

- After creating new term files
- During monthly review of existing directories
- When files of specific category reach 3 (next one will meet creation condition)

### Creation Example

**For Words/Programming/ subdirectory:**

```text
Existing files:
- C.md, Java.md, Python.md, JavaScript.md (programming languages)
- Object-Oriented.md, Functional Programming.md (programming concepts)

→ Create Languages/ subdirectory
→ Move programming languages under Languages/
→ Create Words-Languages.md description file
```
