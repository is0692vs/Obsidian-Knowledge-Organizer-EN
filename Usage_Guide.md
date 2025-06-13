# Usage Guide

> **📝 Important Notice**  
> The content of this usage guide has been integrated into **README.md**.  
> For the latest detailed usage instructions, please refer to **[README.md](./README.md)**.

## 📋 Integrated Content

README.md includes the following integrated content:

- 🚀 **Setup Procedures**
- 📖 **Basic Workflow**
- 🗂️ **Instructions Reference Order**
- 📝 **Recommended Prompt Patterns**
- 🔧 **Advanced Usage and Customization**
- 🔧 **Troubleshooting**
- 📊 **Quality Management and Best Practices**

## 🔗 Quick Links

- **[README.md](./README.md)** - Main document (integrated usage guide)
- **[AI Agent Instructions.md](./AI_Agent_Instructions.md)** - Main entry point for AI agents
- **[Instructions/00_Index and Quick Guide.md](./Instructions/00_Index_and_Quick_Guide.md)** - Work-specific quick reference

---

**This file will no longer be updated. Please check README.md for all latest information.**

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
   - [[Instructions/08_Troubleshooting]]

#### 📝 Recommended Prompt Patterns

**🎯 Basic Pattern (Most Recommended):**

```
Please refer to AI_Agent_Instructions.md and start from Instructions/00_Index_and_Quick_Guide.md.

Article file: Clippings/[article name].md

Please execute complete integration of the article following the instructions procedures.
```

**📋 Detailed Specification Pattern (When additional requests exist):**

```
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

```
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

```
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

## 🔧 Advanced Usage

### Customization

1. **Adding new categories**

   - Request AI agents to create new directories following instructions in Instructions/03_Directory_Structure_and_Placement_Rules.md

2. **Term organization**

   - Consider subdirectory creation when terms in same category exceed 5

3. **Tag system utilization**
   - Manage tags in Words/Tags/ folder
   - Use for cross-cutting classification

### Troubleshooting

1. **Fix broken links**

   - Use Obsidian's broken link detection feature
   - Request AI agents to fix with the following prompt:

   ```text
   Please refer to AI_Agent_Instructions.md and detect and repair broken links throughout the knowledge base following Instructions/08_Troubleshooting.md.
   ```

2. **Consolidate duplicate terms**

   - Refer to procedures in Instructions/06_Duplication_Check_and_Notation_Variation_Handling.md
   - Request integration work from AI agents:

   ```text
   Please refer to AI_Agent_Instructions.md and execute integration of duplicate term "[term name]" following Instructions/06_Duplication_Check_and_Notation_Variation_Handling.md.
   ```

3. **Article reorganization**

   - When existing articles need improvement:

   ```text
   Please refer to AI_Agent_Instructions.md and execute link addition and term organization for article "[article name]" following Instructions/04_Workflow.md.
   ```

## 📊 Quality Management

### Regular Maintenance

1. **Monthly review**

   - Confirm newly added terms and articles
   - Review category structure

2. **Annual organization**
   - Review old articles
   - Organize inactive terms

### Best Practices

1. **Utilize Instructions directory**

   - Always request AI agents to refer to "AI_Agent_Instructions.md"
   - Clearly state "start from Instructions/00_Index_and_Quick_Guide.md"
   - Refer to appropriate specialized instructions according to work content
   - Use recommended prompt patterns

2. **Maintain consistency**

   - Unify term notation
   - Adhere to file naming conventions
   - Continue using same prompt patterns
   - Replace links containing slashes with underscores

3. **Gradual work**
   - Don't perform large amounts of processing at once
   - Proceed gradually while confirming
   - Check for broken links after each work session

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

## 🤝 Community Contribution

1. **Improvement suggestions**

   - Submit improvement suggestions via GitHub Issues
   - Share new feature ideas

2. **Template sharing**

   - Create industry-specific templates
   - Share within community

3. **Document improvement**
   - Update usage guides
   - Add use cases
