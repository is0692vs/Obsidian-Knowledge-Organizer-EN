# 📁 03_Directory Structure and Placement Rules

## Directory Structure

```text
Knowledge Base/
├── Articles/            # Organized articles
│   ├── Programming/     # Programming related articles
│   │   └── 00-Articles-Programming.md  # Description file
│   ├── Tools/           # Tool related articles
│   │   └── 00-Articles-Tools.md        # Description file
│   ├── Infrastructure/  # Infrastructure related articles
│   │   └── 00-Articles-Infrastructure.md # Description file
│   ├── Cloud/           # Cloud related articles
│   │   └── 00-Articles-Cloud.md        # Description file
│   ├── Finance/         # Investment related articles
│   │   └── 00-Articles-Finance.md      # Description file
│   └── 00-Articles.md      # Article index
├── Clippings/           # Original article clips (temporary storage)
├── Words/               # Glossary
│   ├── Programming/     # Programming related terms
│   │   └── 00-Words-Programming.md     # Description file
│   ├── Tools/           # Tool related terms
│   │   └── 00-Words-Tools.md           # Description file
│   ├── Infrastructure/  # Infrastructure related terms
│   │   └── 00-Words-Infrastructure.md  # Description file
│   ├── Cloud/           # Cloud related terms
│   │   └── 00-Words-Cloud.md           # Description file
│   ├── Finance/         # Investment related terms
│   │   └── 00-Words-Finance.md         # Description file
│   ├── Authors/         # Author information
│   │   └── 00-Words-Authors.md         # Description file
│   ├── Services/        # Service information
│   │   └── 00-Words-Services.md        # Description file
│   ├── Tags/            # Tag classification
│   │   └── 00-Words-Tags.md            # Description file
│   └── 00-Words.md         # Term index
├── 00-FileIndex.md # Complete file list
└── AI_Manual.md     # Detailed manual (reference)
```

### ⚠️ Description File Naming Rules

**New Rule: Numbered parent directory name-child directory name.md**

**Two naming options:**

#### Option 1: Leading number (displays at top)

- `Articles/Cloud/` → `Articles/Cloud/00-Articles-Cloud.md`
- `Words/Cloud/` → `Words/Cloud/00-Words-Cloud.md`
- `Words/Programming/` → `Words/Programming/00-Words-Programming.md`

#### Option 2: Trailing number (displays at bottom)

- `Articles/Cloud/` → `Articles/Cloud/ZZ-Articles-Cloud.md`
- `Words/Cloud/` → `Words/Cloud/ZZ-Words-Cloud.md`
- `Words/Programming/` → `Words/Programming/ZZ-Words-Programming.md`

**Recommended: Option 1 (Leading number)**

- Description files display at top during ABC sort
- Description files are immediately visible when opening directory
- Maintains easily findable position even when new files are added

**This naming convention provides:**

- File placement location identifiable from filename alone
- Description files fixed in prominent position during ABC sort
- Description files placed directly under corresponding directory
- Description file visibility maintained even as other files increase

## File Placement Criteria

### Term File Placement (Words/)

- Programming languages, frameworks, techniques → `Words/Programming/`
- Development tools, AI technology, software → `Words/Tools/`
- Cloud services, providers → `Words/Cloud/`
- Infrastructure technology, servers, networks → `Words/Infrastructure/`
- Investment, finance, economic terms → `Words/Finance/`
- Names, authors, developers → `Words/Authors/`

### Article File Placement (Articles/)

- Programming-related articles → `Articles/Programming/`
- Tool introduction and how-to articles → `Articles/Tools/`
- Infrastructure construction and operation articles → `Articles/Infrastructure/`
- Cloud utilization articles → `Articles/Cloud/`
- Investment and asset management articles → `Articles/Finance/`

## Words/ Description File Hierarchical Link Structure

### Basic Design Principles

**Each description .md file directly under a directory functions as a mini-version of 00-FileIndex.md:**

- Forms meaningful hierarchical structure in graph view
- Systematically organizes [[]] links to all term files in the directory
- Realizes knowledge networking through category-based hierarchical structure

### Description File Structure Pattern

**Required section configuration:**

```markdown
# Directory Name

## Overview

Explicitly state hierarchical knowledge network formation in graph view

## Main Categories

### Category 1 Name

- [[Term1]] - Concise description (example format)
- [[Term2]] - Concise description (example format)

### Category 2 Name

- [[Term3]] - Concise description (example format)
- [[Term4]] - Concise description (example format)

## Subdirectories

- [[00-Words-Programming-Languages]] - Programming language specialized terms
- [[00-Words-Programming-Frameworks]] - Framework-related terms

**Note**: In Instructions/ directory, [[]] links like [[Sample File]] are safe to use for examples since they are not processed by Obsidian's link system.

## Subdirectory Planning

Guidelines for future subdirectory division
```

### ⚠️ Mandatory Rules for Description File Link Structure

**Each description file must link to the following:**

1. **All md files in the same directory**
   - Example: `Object-Oriented.md`, `Compilation.md`, etc. in `Words/Programming/`
2. **Description files of subdirectories**

   - Example: If `Words/Programming/Languages/` exists, then `Words-Programming-Languages.md`
   - Subdirectory naming convention: `Parent-Child-Grandchild.md`

3. **Link update timing**
   - When creating new file: Immediately update description file
   - When creating subdirectory: Add subdirectory link to parent description file
   - When moving file: Update both source and destination description files

### Description File Update Timing

**When creating new term file:**

1. After creating term file, immediately check corresponding description file
2. Add [[]] link to appropriate category
3. Adjust category structure as needed
4. Consider subdirectory creation if exceeding 5 files

**When creating subdirectory:**

1. Create new subdirectory description file (`Parent-Child.md` format)
2. Add "Subdirectories" section to parent directory description file
3. Remove moved file links from parent, add to sub description file

**Mandatory checklist for description file editing:**

- ✅ [[]] links exist to all md files in same directory
- ✅ [[]] links exist to all subdirectory description files
- ✅ Category classification is logically organized
- ✅ Hierarchical structure makes sense in graph view
- ✅ No broken links exist

### Directory-specific Category Design Guidelines

#### Programming/

- Programming languages, Web development & frameworks, Development methods & design, Development processes & practices, AI & advanced technology, Development & learning resources

#### Infrastructure/

- Container & virtualization technology, Network & security, Architecture & services, Operations & development processes

#### Tools/

- IDE & editors & development environments, AI tools & development support, Version control & package management, Knowledge management & documentation

#### Services/

- Development & information sharing platforms

#### Authors/

- Technical article writers (by specialty)

#### Tags/, Finance/, Cloud/

- Currently no individual files created, future classification plans documented

## Articles/ Description File Hierarchical Link Structure

### Articles/ Basic Design Principles

**Each description .md file directly under a directory functions as an index for article management:**

- Forms meaningful hierarchical structure in graph view
- Systematically organizes [[]] links to all article files in the directory
- Realizes article networking through category-based hierarchical structure

### Articles/ Description File Structure Pattern

**Required section configuration:**

```markdown
# Directory Name

## Overview

Explicitly state hierarchical knowledge network formation in graph view

## Collected Articles

### Category 1 Name

- [[Article Title 1]] - Concise content description
- [[Article Title 2]] - Concise content description

### Category 2 Name

- [[Article Title 3]] - Concise content description
- [[Article Title 4]] - Concise content description

## Subdirectories

- [[Articles-Programming-WebDev]] - Web development related articles
- [[Articles-Programming-Languages]] - Programming language articles

## Subdirectory Planning

Guidelines for future subdirectory division
```

### ⚠️ Mandatory Rules for Articles Description File Link Structure

**Each description file must link to the following:**

1. **All article md files in the same directory**
   - Example: All article files in `Articles/Programming/`
2. **Description files of subdirectories**
   - Example: If `Articles/Programming/WebDev/` exists, then `Articles-Programming-WebDev.md`
   - Subdirectory naming convention: `Articles-Parent-Child.md`

### Articles/ Description File Update Timing

**When creating new article file:**

1. After creating article file, immediately check corresponding description file
2. Add [[]] link to appropriate category
3. Adjust category structure as needed
4. Consider subdirectory creation if exceeding 5 files

**When creating subdirectory:**

1. Create new subdirectory description file (`Articles-Parent-Child.md` format)
2. Add "Subdirectories" section to parent directory description file
3. Remove moved article links from parent, add to sub description file

**Mandatory checklist for description file editing:**

- ✅ [[]] links exist to all article files in same directory
- ✅ [[]] links exist to all subdirectory description files
- ✅ Category classification is logically organized
- ✅ Hierarchical structure makes sense in graph view
- ✅ No broken links exist

### Articles/ Directory-specific Category Design Guidelines

#### Articles/Programming/

- Python & Web development articles, Language-specific articles, Framework articles, Algorithm articles

#### Articles/Infrastructure/

- Docker & container technology articles, Network technology articles, Security articles, DevOps articles

#### Articles/Tools/

- AI-assisted development tool articles, IDE & editor articles, Version control articles, Productivity tool articles

#### Articles/Cloud/, Articles/Finance/

- Currently no individual articles created, future classification plans documented

## STEP 2.5: .gitignore File Update【Important】

When creating new subdirectories, add exclusion settings for description files to the .gitignore file:

```gitignore
# Track description files of new subdirectories as well
!Vault/Articles/NewDirectoryName/NewDirectoryName.md
!Vault/Words/NewDirectoryName/NewDirectoryName.md
```

## Directory and File Creation

1. Create new directory
2. Create description file in "DirectoryName.md" format directly under directory
3. Move related article/term files to new directory

## Automatic Subdirectory Creation Rules

### Creation Decision Criteria

**When 4 or more files of the same category accumulate AND files of other different categories also exist, create a subdirectory**

#### Specific Example

**When the following files exist in Words/Programming/:**

- C.md
- Java.md
- Python.md
- JavaScript.md
- Object-Oriented.md
- Functional Programming.md

→ Programming languages (4) and Programming concepts (2) are mixed
→ Create `Words/Programming/Languages/` subdirectory

**Examples where NOT to create:**

- Only C.md, Java.md, Python.md (3 files) → Don't create as less than 4
- Only programming languages with no other categories → No point in division, so don't create

### Creation Process

```text
【Subdirectory Creation Process】
1. Analyze files in target directory and classify by category
2. Confirm 4 or more files of same category mixed with other categories
3. Determine appropriate subdirectory name
   Examples: Languages, Frameworks, Concepts
4. Create subdirectory
5. Create description .md file with same name directly under subdirectory
6. Move relevant files to subdirectory
7. Update parent directory description file
8. Update 00-FileIndex.md
9. Execute broken link check
```

### Recommended Subdirectory Names

#### Under Words/Programming/

- **Languages/** - Programming languages (C, Java, Python, etc.)
- **Frameworks/** - Frameworks (React, Vue, Django, etc.)
- **Concepts/** - Programming concepts (Object-oriented, Functional, etc.)
- **Tools/** - Development tools (IDE, Debugger, etc.)

#### Under Words/Infrastructure/

- **Containers/** - Container technology (Docker, Kubernetes, etc.)
- **Networks/** - Network technology (TCP/IP, DNS, etc.)
- **Security/** - Security technology (Encryption, Authentication, etc.)

#### Under Words/Tools/

- **Editors/** - Editors and IDEs (VSCode, IntelliJ, etc.)
- **AI/** - AI tools (GitHub Copilot, ChatGPT, etc.)
- **VersionControl/** - Version control (Git, SVN, etc.)

### Subdirectory Description File Template

```markdown
# Subdirectory Name

## Overview

This directory organizes terms related to [Category Name] within [Parent Directory Name].
Aims to form hierarchical knowledge network in graph view.

## Collected Terms

### [Subcategory 1]

- [[Term1]] - Concise description
- [[Term2]] - Concise description

### [Subcategory 2]

- [[Term3]] - Concise description
- [[Term4]] - Concise description

## Related Directories

- [[00-Words-Programming]] - Parent directory (required)
- [[00-Words-Tools]] - Related other directories

## Additional Guidelines

Guidelines for further subdivision if needed
```

### ⚠️ Required Elements for Subdirectory Description Files

**Each subdirectory description file must:**

1. **Link to all files contained within**
2. **Link to parent directory description file** (required)
3. **Also link to related other directories**

### Execution Timing

**When to consider automatic creation:**

1. When creating new term files
2. When organizing existing directories
3. During monthly maintenance
4. During category analysis

**Checklist:**

- ✅ 4 or more files in same category
- ✅ Files from other categories also exist
- ✅ Logical division is possible
- ✅ Subdirectory name is appropriate
