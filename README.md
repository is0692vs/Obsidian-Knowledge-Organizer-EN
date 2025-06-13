# Obsidian AI Knowledge Framework

Framework for automatic term organization and knowledge systematization using Obsidian and AI agents

## 🎯 Concept

This framework is a template for AI agents to automatically extract terms from web pages and articles collected in Obsidian and organize them systematically.

### Main Features

- 📝 **Automatic term extraction**: AI automatically extracts important terms from web-clipped pages
- 🔗 **Automatic link generation**: Visualization of relationships using Obsidian's bidirectional link functionality
- 📚 **Systematic classification**: Build knowledge base by organizing terms by category
- 🤖 **Detailed instruction system**: Function-specific instruction manuals for AI agents to perform consistent work
- 🛡️ **Link integrity guarantee**: Automatic file existence confirmation system when creating [[]] links
- 📁 **File structure management**: Index system for efficient file existence confirmation
- 🔍 **Broken link prevention**: Elimination of uncreated links through gradual file creation
- 🧠 **Notation variation unification**: Comprehensive notation unification through rule-based and semantic detection

## ⚡ Prerequisites

Environment required to use this framework:

### System Requirements

- **Python**: 3.8 or higher (for tools like link checker)
- **Obsidian**: Latest version recommended
- **AI Agent**: With file editing permissions (Claude, ChatGPT, GitHub Copilot, etc.)

## 🚀 Quick Start

### 1. Setup

```bash
# Clone this repository
git clone https://github.com/is0692vs/obsidian-knowledge-organizer.git
```

### 2. Obsidian Configuration

Specify the Vault folder as the vault

### 3. Python Environment Setup (Required)

This framework uses Python scripts for functions like broken link checking.

#### Python Requirements

- **Python**: 3.8 or higher
- **Dependencies**: Currently uses only standard library (requirements.txt prepared for future extensions)

#### Installation Procedure

```bash
# 1. Check Python version
python3 --version
# or
python --version

# 2. Create virtual environment (recommended)
python3 -m venv venv

# 3. Activate virtual environment
# macOS/Linux:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Verify link checker operation
python link_checker.py
```

#### Available Python Tools

**link_checker.py**: Check for broken [[]] format internal links

```bash
# Basic usage
python link_checker.py

# Results are output to link_check_report.json
```

#### Troubleshooting

**When Python is not found:**

```bash
# Install with Homebrew (macOS)
brew install python3

# Ubuntu/Debian
sudo apt update && sudo apt install python3 python3-pip python3-venv

# Windows: Download from https://python.org
```

**When virtual environment won't activate:**

```bash
# Specify path explicitly
/path/to/venv/bin/python -m pip install -r requirements.txt
```

### 4. Required Tools

- [Obsidian](https://obsidian.md/) - Knowledge base building tool
- [Obsidian Web Clipper](https://obsidian.md/clipper) - For web page clipping
- AI Agent (Claude, ChatGPT, GitHub Copilot, etc.) with file editing permissions

### 5. Obsidian Web Clipper Configuration

1. Install Obsidian Web Clipper extension in browser
2. Set Clippings folder as save destination in settings

## 📖 Basic Workflow

### Step 1: Article Collection

1. **Collect articles with Web Clipper**

   - Use Obsidian Web Clipper in browser
   - Save articles to Clippings folder

2. **Manual article addition**
   - Create markdown files directly in Clippings folder

### Step 2: AI Agent Organization

Request AI agents (GitHub Copilot, Claude, ChatGPT, etc.) using the following prompt patterns:

#### 🗂️ Instructions Reference Order

Have AI agents refer to instructions in the following order:

1. **[[AI Agent Instructions]]** - Main entry point
2. **[[Instructions/00_Index and Quick Guide]]** - Work-specific quick reference
3. **Relevant specialized instructions as needed**:
   - [[Instructions/01_Project Overview]]
   - [[Instructions/02_Link Management]]
   - [[Instructions/03_Directory Structure and Placement Rules]]
   - [[Instructions/04_Workflow]]
   - [[Instructions/05_File Format]]
   - [[Instructions/06_Duplication Check and Notation Variation Handling]]
   - [[Instructions/07_Index Management]]
   - [[Instructions/08_Troubleshooting]]
   - [[Instructions/09_Link Creation Criteria and Guidelines]]

#### 📝 Recommended Prompt Patterns

**🎯 Basic Pattern (Most Recommended):**

```text
Please refer to AI_Agent_Instructions.md and start from Instructions/00_Index_and_Quick_Guide.md.

Article file: Clippings/[article name].md

Please execute complete integration of the article following the instructions procedures.
```

**📋 Detailed Specification Pattern (When additional requests exist):**

```text
Please refer to AI_Agent_Instructions.md and start from Instructions/00_Index_and_Quick_Guide.md to completely integrate the following article into the knowledge base:

Article file: Clippings/[article name].md
Special requests: [Example: emphasize programming field, focus on specific terms, etc.]

Execute the following according to instructions:
1. Duplication check
2. Term extraction and file creation
3. Article placement and link addition
4. Index update
5. Broken link check
6. Work report
```

**🔗 Link Addition Specific Pattern:**

```text
Please refer to AI_Agent_Instructions.md and start from Instructions/00_Index_and_Quick_Guide.md.

Please add [[]] links to article "[article name]".

Following Instructions/04_Workflow.md:
1. Identify important terms
2. Confirm file existence and create
3. Add [[]] links
4. Update indexes
5. Final confirmation
```

**🛠️ Maintenance Pattern:**

```text
Please refer to AI_Agent_Instructions.md and start from Instructions/00_Index_and_Quick_Guide.md.

Please detect and repair broken links throughout the knowledge base.

Please execute following the procedures in Instructions/08_Troubleshooting.md.
```

#### ⚠️ Important Points

- **Always instruct reference to "AI_Agent_Instructions.md"**
- **Clearly state "start from Instructions/00_Index_and_Quick_Guide.md"**
- **Specify concrete file names**
- **Request execution of instructions procedures**
- **Have them refer to appropriate specialized instructions according to work content**

Using these patterns enables AI agents to execute work with consistent quality.

### Step 3: Result Confirmation

1. **Confirm article movement**
   - Check if moved from Clippings to appropriate Articles subfolder
2. **Confirm term creation**
   - Check if new term files are created in Words folder
3. **Confirm links**
   - Check if appropriate [[]] links are created within articles

## 📁 Directory Structure

```text
obsidian-ITknowledge/
├── README.md                    # This file (main document)
├── AI_Agent_Instructions.md     # Main entry point for AI agents
├── Instructions/                # Function-specific detailed instructions
│   ├── 00_Index_and_Quick_Guide.md
│   ├── 01_Project_Overview.md
│   ├── 02_Link_Management.md
│   ├── 03_Directory_Structure_and_Placement_Rules.md
│   ├── 04_Workflow.md
│   ├── 05_File_Format.md
│   ├── 06_Duplication_Check_and_Notation_Variation_Handling.md
│   ├── 07_Index_Management.md
│   ├── 08_Troubleshooting.md
│   └── 09_Link_Creation_Criteria_and_Guidelines.md
├── 00-FileIndex.md              # For efficient file existence confirmation
├── CONTRIBUTING.md              # Contribution guidelines
├── link_checker.py              # Broken link detection tool
├── link_check_report.json       # Link check results
├── Clippings/                   # Raw articles collected with Web Clipper
├── Vault/                       # Obsidian main vault
│   ├── Articles/                # Storage for organized articles
│   │   ├── 00-Articles_EN.md    # Description of article categories
│   │   ├── Cloud/              # Cloud-related articles
│   │   ├── Finance/            # Finance and investment-related articles
│   │   ├── Infrastructure/     # Infrastructure-related articles
│   │   ├── Programming/        # Programming-related articles
│   │   └── Tools/              # Tool-related articles
│   └── Words/                   # Extracted and organized glossary
│       ├── 00-Words_EN.md      # Description of term categories
│       ├── Authors/            # Authors and names
│       ├── Cloud/              # Cloud service terms
│       ├── Finance/            # Finance and investment terms
│       ├── Infrastructure/     # Infrastructure technology terms
│       ├── Programming/        # Programming terms
│       ├── Services/           # Various service terms
│       ├── Tags/               # Tag and classification terms
│       └── Tools/              # Tool and technology terms
```

## 🔧 Advanced Usage and Customization

### 1. Adding New Categories

```text
Please refer to AI_Agent_Instructions.md and add new category "[category name]" following Instructions/03_Directory_Structure_and_Placement_Rules.md.

Execute with the following steps:
1. Create Articles/[category name]/ directory
2. Create Words/[category name]/ directory
3. Create descriptive .md files in each directory
4. Update index files
```

### 2. Term Organization and Integration

Subdirectory creation when terms in the same category become numerous:

```text
Please refer to AI_Agent_Instructions.md and execute subdirectory creation for Words/[category name]/ following the "Automatic Subdirectory Creation Rules" in Instructions/03_Directory_Structure_and_Placement_Rules.md.
```

### 3. Integration of Notation Variations and Duplicate Terms

```text
Please refer to AI_Agent_Instructions.md and execute notation variation integration for term "[term name]" following Instructions/06_Duplication_Check_and_Notation_Variation_Handling.md and Instructions/09_Link_Creation_Criteria_and_Guidelines.md.
```

### 4. Broken Link Check and Repair

This framework provides dedicated check tools to prevent broken links (state where [[]] link target files don't exist).

```bash
# Broken link detection and repair procedure
python link_checker.py

# How to read output:
# ✅ "Session completion condition achieved" → No broken links (complete)
# ⚠️ "Session completion condition not achieved" → Repair needed
# 📋 "For AI agents: List of files to create" → List of files to create
```

**Repair by AI agents:**

```text
Please refer to AI_Agent_Instructions.md and detect and repair broken links throughout the knowledge base following Instructions/02_Link_Management.md and Instructions/08_Troubleshooting.md.
```

## 🔧 Troubleshooting

### Common Problems and Solutions

**Q: AI doesn't classify terms correctly**
A: Review classification rules in Instructions/01_Project_Overview.md and add specific examples.

**Q: Links aren't generated correctly**
A: Refer to Instructions/09_Link_Creation_Criteria_and_Guidelines.md and confirm use of Obsidian link format (`[[term name]]`).

**Q: Terms are duplicated**
A: Request integration from AI agents following Instructions/06_Duplication_Check_and_Notation_Variation_Handling.md.

**Q: Files corresponding to [[]] links aren't created**
A: Have AI agents refer to the "Mandatory Confirmation When Creating Links" section in Instructions/04_Workflow.md and execute strict file management using 00-FileIndex.md.

**Q: Mass broken links occurring**
A: Detect broken links with link_checker.py following Instructions/02_Link_Management.md and Instructions/08_Troubleshooting.md, and execute batch repair by AI agents.

**Q: Notation variations not detected**
A: Refer to "Types of Notation Variations and Detection Methods" in Instructions/09_Link_Creation_Criteria_and_Guidelines.md and execute both rule-based and semantic detection.

**Q: Excessively fragmented links created**
A: Check "Avoiding Excessive Concept Fragmentation" rules in Instructions/09_Link_Creation_Criteria_and_Guidelines.md and thoroughly utilize existing files.

### AI Agent Repair Prompts

**Broken link repair:**

```text
Please refer to AI_Agent_Instructions.md and detect and repair broken links throughout the knowledge base following Instructions/08_Troubleshooting.md.
```

**Duplicate term integration:**

```text
Please refer to AI_Agent_Instructions.md and execute integration of duplicate term "[term name]" following Instructions/06_Duplication_Check_and_Notation_Variation_Handling.md.
```

**Article reorganization:**

```text
Please refer to AI_Agent_Instructions.md and execute link addition and term organization for article "[article name]" following Instructions/04_Workflow.md.
```

## 📊 Quality Management and Best Practices

### Regular Maintenance

1. **Monthly review**

   - Confirm newly added terms and articles
   - Review category structure
   - Mass check for broken links

2. **Annual organization**
   - Review old articles
   - Organize inactive terms
   - Update instructions

### Best Practices

1. **Utilize Instructions directory**

   - Always request AI agents to refer to "AI_Agent_Instructions.md"
   - Clearly state "start from Instructions/00_Index_and_Quick_Guide.md"
   - Refer to appropriate specialized instructions according to work content
   - Continue using recommended prompt patterns

2. **Maintain consistency**

   - Unify term notation (Instructions/09_Link_Creation_Criteria_and_Guidelines.md)
   - Adhere to file naming conventions (Instructions/05_File_Format.md)
   - Replace links containing slashes with underscores
   - Two-stage detection of notation variations (rule-based + semantic detection)

3. **Gradual work**

   - Don't perform large amounts of processing at once
   - Proceed gradually while confirming
   - Check for broken links after each work session
   - Actively utilize existing files

4. **Notation variation and synonym handling**
   - Rule-based detection: file_search + grep_search
   - Semantic detection: semantic_search
   - Check official documentation notation
   - Unify to main file and create redirects

## 🚨 Cautions

1. **Data backup**

   - Regular Git commits and pushes
   - Create branches before important changes

2. **Privacy protection**

   - Handle articles containing personal information carefully
   - Check confidential information before publication

3. **License compliance**
   - Confirm copyright of quoted articles
   - Proper source attribution

## 🤝 Contribution and Community

### Contributing to Improvements

Please help improve this framework:

1. **Issue reporting**

   - Submit improvement suggestions via GitHub Issues
   - Bug reports and feature requests

2. **New feature proposals**

   - New category templates
   - AI agent instruction improvements
   - Workflow optimization proposals

3. **Document improvements**

   - Enrich and clarify instructions
   - Add cases and specific examples
   - Add troubleshooting items

4. **Template sharing**
   - Create industry-specific templates
   - Customization for specific purposes
   - Share within community

### Important Usage Matters

- **Grant appropriate file editing permissions to AI agents**
- **Always have them refer to the Instructions directory**
- **Use recommended prompt patterns**
- **Execute regular backups**

---

## 📚 Reference Materials

- [Obsidian Official Documentation](https://help.obsidian.md/)
- [Obsidian Web Clipper](https://obsidian.md/clipper)
- [Instructions Directory](./Instructions/) - Detailed manual for AI agents
- [CONTRIBUTING.md](./CONTRIBUTING.md) - Detailed contribution guidelines

**📝 Note**: This framework is continuously improved. Always refer to the latest instructions and guidelines.
