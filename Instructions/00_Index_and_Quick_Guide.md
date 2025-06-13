# 📋 AI Agent Instructions - Index and Quick Guide

**[IMPORTANT] This instruction manual is designed so that AI agents can completely independently execute Obsidian knowledge base organization and editing just by reading this.**

## 🚀 Quick Start

### Order for New Agents to Read First

1. **[[01_Project Overview]]** - Understand overall project picture and current status
2. **[[02_Link Management]]** - Most important principle: How to maintain zero broken links
3. **[[03_Directory Structure and Placement Rules]]** - File placement criteria
4. **[[04_Workflow]]** - Specific work procedures
5. **[[05_File Format]]** - Standard file creation templates

### Work-specific Quick Reference

#### 🆕 When Adding New Articles

- [[04_Workflow#New Article Addition]]
- [[02_Link Management#Zero Broken Links Guarantee Protocol]]
- [[05_File Format#Article Files]]

#### 🔗 When Adding Links to Existing Articles

- [[04_Workflow#Adding Links to Existing Articles]]
- [[02_Link Management#Batch Work Protocol]]
- [[09_Link Creation Criteria and Guidelines#Term Extraction Criteria]]

#### 📚 When Creating Term Files

- [[04_Workflow#Single Term File Creation]]
- [[03_Directory Structure and Placement Rules#File Placement Criteria]]
- [[05_File Format#Term Files]]
- [[09_Link Creation Criteria and Guidelines#Link Naming Conventions]]

#### 🚨 When Repairing Broken Links

- [[08_Troubleshooting#Broken Link Detection and Repair]]
- [[02_Link Management#Broken Link Detection with Python Tools]]

#### 📋 When Checking Duplicates and Notation Variations

- [[06_Duplication Check and Notation Variation Handling]]

#### 📁 When Creating Subdirectories

- [[04_Workflow#Automatic Subdirectory Creation]]
- [[03_Directory Structure and Placement Rules#Automatic Subdirectory Creation Rules]]

## 📁 Instruction File List

### Basic Configuration

- [[01_Project Overview]] - About the project, directory structure roles, current status
- [[02_Link Management]] - Most important principles, verification protocols, batch work methods
- [[03_Directory Structure and Placement Rules]] - Directory structure, placement criteria

### Work Procedures

- [[04_Workflow]] - Procedures for new article addition, link addition, term file creation
- [[05_File Format]] - Templates for term files, article files, author files

### Quality Management

- [[06_Duplication Check and Notation Variation Handling]] - Duplication check procedures, notation variation unification principles
- [[07_Index Management]] - Required update target files, update formats
- [[08_Troubleshooting]] - Broken link detection and repair, common errors
- [[09_Link Creation Criteria and Guidelines]] - Term extraction, linking criteria, quality guidelines

## 🎯 Efficiency-focused Operations Policy

### [IMPORTANT] Required Rules When Creating Links

- **Links containing slashes must be replaced with \_ (underscore)**
- Example: [[CI/CD]] → [[CI_CD]], [[HTML/CSS]] → [[HTML_CSS]]
- Reason: Obsidian misinterprets slashes as directory separators

### Principles for Work Time Reduction

1. **Rapid decision making**: Decide file placement by first impression (don't hesitate)
2. **Content moderation**: Don't aim for perfection, basic information is sufficient
3. **Utilize parallel processing**: Execute creation of 10 files in parallel
4. **Template utilization**: Copy & modify existing similar files as reference

### Balance of Quality and Efficiency

- **Minimum quality standard**: 100+ characters, 2+ [[]] links, basic structure
- **Completion level**: 60-70% is sufficient (can be improved later)
- **Zero broken links**: Absolute condition (priority over quality)

## ✅ Completion Checklist

**Always confirm before completing all work:**

- [ ] 1st broken link check: Confirmed no broken links using grep_search
- [ ] 2nd broken link check: Confirmed overall integrity using semantic_search
- [ ] 3rd broken link check: Confirmed verification with file structure index
- [ ] File structure index.md updated to latest state
- [ ] Basic content written in newly created files
- [ ] Words.md or Articles.md updated
- [ ] Reported list of created/updated files
- [ ] **Additional confirmation**: Individually confirmed existence of newly created files using file_search
- [ ] **Final confirmation**: Guaranteed zero broken links state through multi-stage verification

## 🚀 Execution Command Examples

### Complete Processing of New Articles

```text
Please completely integrate the following article into the knowledge base:

Article Title: {title}
Content: {content or URL}
Author: {author name}
Field: {Programming/Tools/Infrastructure/Cloud/Finance}

Execute the following according to AI complete instructions:
1. Duplication check
2. Term extraction and file creation
3. Article placement and link addition
4. Index update
5. Broken link check
6. Work report
```

### Adding [[]] Links to Existing Articles

```text
Please add [[]] links to article "{article name}".

According to AI complete instructions:
1. Identify important terms
2. Confirm file existence and create
3. Add [[]] links
4. Update indexes
5. Final confirmation
```

### Batch Repair of Broken Links

```text
Please detect and repair broken links throughout the knowledge base.

Please execute following the troubleshooting procedures in AI complete instructions.
```

---

**These instructions are self-contained. AI agents can perform complete organization and editing of the Obsidian knowledge base using only this content.**
