# 📋 07_Index Management

## Mandatory Update Target Files

### Required Updates When Creating New Files

1. **File Structure Index.md**

   - Add newly created files to appropriate sections
   - Organize in alphabetical order

2. **Words.md**

   - Add to relevant category when creating term files

3. **Articles/Articles.md**
   - Add to relevant category when creating articles

## Directory Description Files Guidelines

### Current File Summary Requirements

Each directory description file (00-{Category}.md) must:

1. **List actually existing files** - Do not create sample links to non-existent files
2. **Provide real file summaries** - Document actual files currently managed in the directory
3. **Use actual links only** - Only link to files that actually exist using [[filename]] syntax
4. **Avoid sample links** - Never create examples like [[Article1]] or [[Sample Term]] as these create broken links in Obsidian

### Correct vs Incorrect Linking Examples

**❌ Incorrect (Sample Links):**

```markdown
- ((Article1)) - Sample article about cloud computing
- ((Term Example)) - Example programming term
```

**✅ Correct (Actual File Links):**

```markdown
- [[00-Articles-Cloud]] - Cloud computing articles index
- [[JavaScript]] - Programming language overview (only if JavaScript.md exists)
```

**Important Note**: In examples above, we use (()) to avoid creating broken links in documentation. When creating actual content, always use [[]] syntax for links to existing files.

## Index Update Format

### File Structure Index.md

```markdown
## {Category Name}

- {Filename 1}.md
- {Filename 2}.md (newly added)
- {Filename 3}.md
```

### Words.md

```markdown
### {Subcategory Name}

- [[Term Name1]] - Brief description
- [[Term Name2]] - Brief description (newly added)
```

## Index Update Timing

1. Immediately after creating new files
2. When moving or deleting files
3. When changing categories
4. **When creating subdirectories**
5. When completing work sections

## Special Update Tasks When Creating Subdirectories

### Required Update Items

1. **File Structure Index.md**

   - Add new subdirectories and their description files
   - Update paths for moved files

2. **Parent Directory Description Files**

   - Add links to subdirectories
   - Reorganize category classifications

3. **Words.md (when applicable)**
   - Update to subdirectory-based classifications

### Update Examples

**Before Subdirectory Creation:**

```markdown
## Words/Programming/

- [[C]] - Programming language
- [[Java]] - Programming language
- [[Python]] - Programming language
- [[Object-Oriented]] - Programming concept
```

**After Subdirectory Creation:**

```markdown
## Words/Programming/

- [[Programming]] - Comprehensive directory description for programming-related terms

### Subdirectories

- [[Programming/Languages]] - Programming language related terms
- [[Programming/Concepts]] - Programming concept related terms

### Other Terms

- [[Object-Oriented]] - Programming concept
```

## Index Update Checklist

- ✅ Organize in alphabetical order
- ✅ Confirm no duplicate entries
- ✅ Confirm no broken links
- ✅ Confirm appropriate category classifications
- ✅ Check subdirectory creation conditions (4 or more in same category)
