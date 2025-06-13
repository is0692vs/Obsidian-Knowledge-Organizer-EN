# AI Knowledge Base Organization Manual

This manual provides standard procedures and instructions for directing AI (such as GitHub Copilot) when adding new clips or information to an Obsidian knowledge base. By requesting AI to organize according to this manual's procedures, you can manage your knowledge base in a consistent manner.

## Basic Principles

### Essential Confirmation When Creating [[]] Links [MOST IMPORTANT]

**[ABSOLUTE PRINCIPLE] When creating [[]] links, always confirm that the corresponding .md file exists, and create it immediately if it doesn't.**

To prevent the mass generation of orphaned graph nodes with no corresponding link targets in Obsidian:

#### 1. Strict Link Creation Process [MANDATORY COMPLIANCE]

**For all [[]] link creation, always execute the following:**

```text
[Mandatory Steps for Link Creation]
1. Confirm existence of corresponding file using file_search tool
2. If it doesn't exist, immediately create the file
3. Add [[]] link after file creation is complete
4. If using new [[]] links within the created file, repeat steps 1-3
```

**Example: When creating a [[Docker]] link**

```text
Step 1: Search for "Docker.md" using file_search
Step 2: If it doesn't exist → Create Words/Tools/Docker.md using create_file
Step 3: If using [[Container]] within Docker.md
  → Search for "Container.md" using file_search
  → If it doesn't exist → Create Words/Infrastructure/Container.md using create_file
Step 4: After all related files are created, add [[Docker]] link to original article
```

#### 2. Managing Cascading File Creation

**Link management when creating new files:**

- When creating a new file, also pre-check all [[]] links used within that file
- **Prohibited**: "Write links first and create files later"
- **Required**: Always create corresponding files before writing links

#### 3. Automating File Existence Checks

**Recommended workflow:**

```text
[Standard Process for Article Organization]
1. Extract terms from article
2. Check existing files for each term using file_search
3. Create all non-existing term files
4. After all file creation is complete, add links within article
5. Final check using grep_search to ensure no broken links
```

#### 4. Gradual Link Construction [Recommended]

For articles containing many terms:

```text
[Phased Approach]
Phase 1: Most important terms (5 or fewer) file creation and linking
Phase 2: Moderately important terms (5 or fewer) file creation and linking
Phase 3: Other terms file creation and linking

Perform functionality check after each phase completion
```

#### 5. Error Prevention Checklist

**Always confirm the following:**

- [ ] Verified target file existence using file_search
- [ ] Created files for non-existing cases
- [ ] Confirmed all links within newly created files
- [ ] Final confirmation that there are no broken links
- [ ] Confirmed normal link display in Obsidian

#### 6. Utilizing File Structure Index [Efficiency]

For efficient file existence confirmation, utilize `00-FileIndex.md`:

**[Recommended Workflow]**

```text
1. Before creating [[]] links, first check "00-FileIndex.md"
2. If corresponding file is not listed in index → Final confirmation with file_search
3. If it doesn't exist → Immediately create file
4. After file creation → Update 00-FileIndex.md
5. Final check using grep_search to ensure no broken links
```

**Mandatory items for index updates:**

- Always add to index when creating new files
- Organize alphabetically
- Update last modification date
- Remove from index when deleting files

**Example: When creating a [[Docker]] link**

```text
Step 1: Search for "Docker.md" in 00-FileIndex.md
Step 2: If not listed → Search for "Docker.md" using file_search
Step 3: If it doesn't exist → Create Words/Tools/Docker.md using create_file
Step 4: Add "Docker.md" to Tools section in 00-FileIndex.md
Step 5: Add [[Docker]] link to original article
```

### Thorough Duplication Prevention

Before adding new articles or information, **always perform duplication checks**:

1. **Duplication check with existing articles**

   - Check for similar articles in Articles and Clippings directories
   - Check existing articles by the same author
   - Check articles on the same topic/technology

2. **Term duplication check and notation variation handling**

   - Check for identical/similar terms in Words directory
   - Check for same concepts with different notations
   - **Detection and unification of notation variations**:
     - Example: "Azure" and "Microsoft Azure"
     - Example: "JavaScript" and "JS"
     - Example: "GitHub Copilot" and "Copilot"
     - Example: "Next.js" and "NextJS"

### Standard Procedure for Handling Notation Variations

When terms with the same concept but different notations are discovered:

1. **Criteria for determining primary notation**

   **Priority order**:

   a) **Confusion avoidance (highest priority)**: Choose notation that is less likely to be confused with other concepts

   - Example: "Copilot" vs "GitHub Copilot"
     → "Copilot" might be confused with "Microsoft Copilot"
     → Unify to "GitHub Copilot"

   b) **Catchiness**: Memorable and easy-to-use notation

   - Prioritize common and short notations
   - But not at the expense of confusion avoidance

   c) **Official name authenticity**: Respect official names and notations

   - Check notations in official documentation
   - Consider brand names and trademark notations

   **Specific examples**:

   - "Azure" vs "Microsoft Azure" → "Azure" (short and catchy, no confusion risk)
   - "GitHub Copilot" vs "Copilot" → "GitHub Copilot" (confusion avoidance priority)
   - "Next.js" vs "NextJS" → "Next.js" (official notation)
   - "JavaScript" vs "JS" → "JavaScript" (official name, confusion avoidance)

2. **Implementing file consolidation**

   **Primary file (selected notation)**:

   - Include detailed explanatory content
   - Also mention other notations ("also called ~")
   - Set comprehensive related links

   **Secondary file (consolidated notation)**:

   - Change to concise redirect format
   - Guide to primary file at the beginning
   - Explain notation differences as needed

3. **Handling generic terms**

   **When generic terms refer to multiple specific technologies**:

   - Example: "Copilot" → includes both "GitHub Copilot" and "Microsoft Copilot"
   - Generic term file explains concept + [[]] links to each specific implementation
   - Specific technology files have detailed implementation explanations

4. **Format for secondary files**

   ```markdown
   # Microsoft Azure

   Synonymous with [[Azure]]. A cloud computing platform provided by Microsoft.

   Please refer to [[Azure]] for details.

   ## Related Concepts

   - [[Azure]] - Main article
   ```

5. **Consider rewriting existing [[]] links**

   - Unify to primary notation as much as possible
   - Maintain secondary notation when appropriate in context

6. **Response to duplication discovery**
   - Compare value of existing content vs new content
   - Consider updating existing article if complementary
   - Cancel addition if completely duplicate
   - **When duplication exists between Clippings and Articles**:
     - Prioritize Articles articles and delete duplicate article files (.md) in Clippings
     - If Clippings articles have more detailed information before deletion, integrate into Articles article

### Maintaining Consistency

- Adhere to existing directory structure
- Unify file naming conventions
- Cross-reference using [[]] link notation
- Consistent metadata description

## Basic Structure

The knowledge base is organized with the following structure:

```
iCloudObsidianVault/
├── Articles/            # Organized articles
│   ├── Programming/     # Programming-related articles
│   ├── Tools/           # Tool-related articles
│   ├── Infrastructure/  # Infrastructure-related articles
│   ├── Cloud/           # Cloud-related articles
│   ├── Finance/         # Investment-related articles
│   └── 00-Articles.md      # Articles index
├── Clippings/           # Original article clips
├── Words/               # Glossary
│   ├── Programming/     # Programming-related terms
│   ├── Tools/           # Tool-related terms
│   ├── Infrastructure/  # Infrastructure-related terms
│   ├── Cloud/           # Cloud-related terms
│   ├── Finance/         # Investment-related terms
│   ├── Authors/         # Author information
│   └── 00-Words.md         # Terms index
├── Tags/                # Tag list
│   ├── Programming Languages.md
│   ├── Cloud Services.md
│   ├── Infrastructure Technologies.md
│   ├── Development Tools.md
│   ├── Investment Strategies.md
│   └── Tag Index.md
└── Home.md              # Homepage
```

## AI Instruction Templates

### 1. Adding and Organizing Articles

When incorporating newly clipped articles into the knowledge base, use the following instructions:

```
Please organize the following article into my Obsidian knowledge base:

Article Title: {article title}
Article Content: {article content or URL}
Author: {author name} (if known)
Field: {one of Programming/Tools/Infrastructure/Cloud/Investment}

Procedure:

【Duplication Check (Mandatory)】
0. First check for duplication with existing articles using the following methods:
   - Search for article title and main keywords using semantic_search tool
   - Check related fields in Articles/ directory for similar articles
   - Check Clippings/ directory for the same article
   - Check [[Clippings Index]] to see if already clipped
   - Check existing article list by the same author

   If duplication is found:
   - Judge whether there is additional value compared to existing article content
   - If duplicate, stop processing and guide to existing article link
   - If complementary content, consider updating existing article

【Article Organization/Addition】
1. Analyze article content to identify appropriate category and subcategory
2. Place article in Articles/{appropriate subfolder}/
3. **[Important] Extract related terms and strict file management**:
   - First identify and list all related terms
   - Check existence in "00-FileIndex.md" for each term
   - Final confirmation with `file_search` for non-existing terms
   - Create all non-existing term files
   - Update 00-FileIndex.md
   - After all file creation is complete, add [[]] links within article
4. Add or update author information in Words/Authors/
5. Associate article with tags and update tag pages
6. Update article index (Articles/00-Articles.md)
7. Update terms index (Words/00-Words.md) as needed
8. **Final confirmation**: Confirm no broken links using grep_search

Please adhere to existing folder structure and file formats.
```

### 1.1 Adding [[]] Links in Articles [Important for Preventing Cascade Link Problems]

Strict procedure when adding [[]] links to existing articles:

```
Please add [[]] links to {article name}.

【Mandatory Steps】Strictly follow this order to prevent cascade unwritten links:

1. **Target article analysis**
   - Identify important terms and concepts in the article
   - Carefully select 5-10 terms for [[]] linking (don't add many at once)

2. **Pre-file existence confirmation**
   - First check existence of all terms in "00-FileIndex.md"
   - For terms not in index, final confirmation with file_search
   - Create list of non-existing terms

3. **Pre-batch creation of term files**
   - Create all non-existing terms first based on these criteria:
     - Programming terms: Words/Programming/
     - Tools/Services: Words/Tools/
     - Infrastructure technology: Words/Infrastructure/
     - Cloud services: Words/Cloud/
     - Investment/Finance: Words/Finance/
     - Names/Authors: Words/Authors/
   - Update 00-FileIndex.md

4. **Content restrictions for created files [Important]**
   - Minimize [[]] links within newly created term files
   - Complete with basic explanations only
   - Maximum 3 links in "Related Terms" section
   - When adding related links, always confirm corresponding file existence first

5. **Adding links to article**
   - After all term file creation is complete, add [[]] links to article
   - Gradual addition: Top 3-5 important → Moderately important 3-5 → Others

6. **Final confirmation**
   - Confirm no broken links using grep_search
   - Report list of created files and links

7. **Absolute prohibitions**
   - Leaving [[]] links without corresponding files
   - Writing unconfirmed links within newly created files
   - Creating more than 10 [[]] links at once

This procedure enables building a gradual knowledge graph with zero broken links.
```

### 2. Adding Terms

When adding specific terms or concepts:

```
Please add the following term to my Obsidian knowledge base:

Term: {term name}
Field: {one of Programming/Tools/Infrastructure/Cloud/Investment}
Definition: {basic definition of term}
Additional Information: {additional information if any}

Procedure:
1. Create markdown file in Words/{appropriate subfolder}/
2. Write detailed explanation of term (features, uses, related concepts, etc.)
3. Add links to related terms
4. Update related tag pages
5. Update 00-Words.md

Please use the same structure as existing term files.
```

### 2.1 Words Directory Organization Policy

Organization procedure when similar concept terms increase in Words directory:

```
Please organize terms in Words directory:

Conditions:
- When 5 or more term files with similar meaning/concepts exist in the same category

Procedure:
1. Identify similar term groups:
   - Same technical domain (e.g., AI-related, container-related, database-related)
   - Same product family (e.g., AWS services, Google services)
   - Same concept lineage (e.g., programming languages, frameworks, tools)

2. Create new subdirectories:
   - Format: Words/{existing category}/{new subcategory}/
   - Example: Words/Tools/AI/ (AI-related tools)
   - Example: Words/Cloud/AWS/ (AWS services)
   - Example: Words/Programming/Languages/ (programming languages)

3. Move related files:
   - Move applicable term files to new directory
   - Don't change file names

4. Update indexes and links:
   - Update 00-Words.md structure for new directory
   - Confirm other file links don't break
   - Add redirect explanations as needed

5. Create new subcategory overview:
   - Create README.md or overview file in new directory
   - Include overview of that category and list of contained terms

Organization examples:
- 5+ AI-related tools in Tools/ → Create Tools/AI/
- 5+ AWS-related services in Cloud/ → Create Cloud/AWS/
- 5+ language-related terms in Programming/ → Create Programming/Languages/
```

### 3. Adding or Updating Tags

When adding/updating new tags:

```
Please add or update the following tag in my Obsidian knowledge base:

Tag Name: {tag name}
Related Field: {one of Programming Languages/Cloud Services/Infrastructure Technologies/Development Tools/Investment Strategies}
Related Articles: {related article titles} (if known)
Related Terms: {related terms} (if known)

Procedure:
1. Update applicable tag page (Tags/{related field}.md)
2. Add new sections as needed
3. Link related articles and terms
4. Update tag index (Tags/Tag Index.md) as needed

Please use the same structure as existing tag pages.
```

### 4. Updating Indexes

When updating indexes only:

```
Please update the indexes in my Obsidian knowledge base.

Target Index: {00-Articles.md/00-Words.md/Tag Index.md}
Items to Add: {list of newly added items}

Procedure:
1. Read current index file
2. Add new items to appropriate sections
3. Maintain consistent format
4. Update other index files as needed

Please maintain consistency with existing index structure.
```

## Article Movement and Organization (Migration from Clippings)

Web-clipped articles are initially saved in the `Clippings/` folder, but after AI organization is complete, delete the original files and move them to categorized folders. Here's the procedure:

```markdown
Please move the following article from Clippings to appropriate category:

Article Title: {article title}
Current Location: Clippings/{filename}.md
Category: {one of Programming/Cloud/Infrastructure/Tools/Investment}

Procedure:

1. Analyze article content and determine optimal subcategory
2. Create article file in Articles/{appropriate subcategory}/ with same name
3. Organize article structure as needed and fix/add related links
4. Delete original file in Clippings/
5. Update related index files (fix references to deleted location)
6. Update Articles/00-Articles.md index

Notes:

- Perform movement in 2 steps: "copy & delete"
- Maintain article content while unifying and organizing format
- Update references to prevent broken links
```

### Batch Movement Example

When moving multiple articles at once, use instructions like the following:

```markdown
Please move the following articles from Clippings to appropriate categories:

Article List:

1. {Article Title 1} - Recommended Category: {Programming}
2. {Article Title 2} - Recommended Category: {Cloud}
3. {Article Title 3} - Recommended Category: {Infrastructure}

For each article:

1. Analyze content and determine optimal subfolder
2. Copy article to appropriate folder in Articles/
3. Delete original file in Clippings/
4. Update links and indexes

After all processing is complete, report the list of moved articles and their new locations.
```

This method ensures articles are properly organized without duplication and maintains the knowledge base structure.

## Complete Batch Processing Instructions

When directing AI to perform multiple tasks at once, you can use the following template:

```markdown
Please incorporate the following new web clip into the knowledge base:

Article Title: {article title}
Article URL: {article URL}
Content Summary: {brief article summary}
Author: {author name (if known)}
Field: {one of Programming/Tools/Infrastructure/Cloud/Investment}

Please perform the following tasks in batch:

1. Analyze article content and extract important terms and concepts
2. Create detailed explanation files in Words/{appropriate subfolder}/ for each extracted term
3. Add or update author information in Words/Authors/
4. Update related tag pages
5. Classify article in appropriate genre Articles subfolder
6. Update related index files (00-Words.md, 00-Articles.md)
7. Create links to existing terms and concepts mentioned in article
8. If there are broken links, create target files

Please faithfully follow existing file structure and format. Add appropriate blank lines before and after markdown headings and bullet points.
```

By giving comprehensive instructions like this, you can complete knowledge base organization with a single instruction.

## Standard Formats

### Article File Format

Article files maintain the original clip content as-is.

### Term File Format

```markdown
# {term name}

{concise definition of term}

## Main Features

- {feature 1}
- {feature 2}
- {feature 3}

## Uses/Types/Classifications

### {subcategory 1}

- {detail item}

### {subcategory 2}

- {detail item}

## Related Concepts

- [[Related term 1]] - Brief explanation of relationship
- [[Related term 2]] - Brief explanation of relationship
```

### Tag Page Format

```markdown
# {field} Tag List

This page provides access to articles and notes through {field}-related tags.

## {subcategory 1} Related

Tags: #{tag 1} #{tag 2}

### {subcategory 1} Articles

- [[Article 1]] - Brief description
- [[Article 2]] - Brief description

### {subcategory 1} Terms

- [[Term 1]] - Brief description
- [[Term 2]] - Brief description
```

## Important Principles

1. **Consistency**: Maintain existing naming conventions and file structure
2. **Cross-linking**: Always create links between related content
3. **Tagging**: Use appropriate tags to enable cross-cutting access
4. **Organization**: Place in appropriate subfolders based on content
5. **Indexing**: Add all new content to indexes

## Special Processing

### Programming Language-Specific Tags

When adding programming language-related articles or terms, use language-specific tags (e.g., #Python, #CSharp).

### Cloud Provider-Specific Tags

When adding cloud service-related articles or terms, use provider-specific tags (e.g., #AWS, #Azure).

### Author Information Handling

When article author information is available, create/update author profiles in the `Words/Authors/` folder.

```markdown
# {author name}

{brief author description}

## Related Articles

- [[Article Title 1]]
- [[Article Title 2]]

## Areas of Expertise

- {expertise area 1}
- {expertise area 2}
```

## Edge Cases

1. **Articles spanning multiple fields**: Place in most relevant field and relate to other fields with tags
2. **Articles in new categories**: If doesn't fit existing categories, consider new subfolders and update indexes and homepage
3. **Term duplication**: When same term is used in different fields, create separate files for each field and cross-reference

## Broken Link Checking and Repair

The Obsidian knowledge base uses [[]] format links. When target files don't exist, broken links occur. Instructions for periodically repairing such broken links are as follows:

```markdown
Please check and repair broken links in the knowledge base.

Procedure:

1. Use grep_search tool to search for all [[]] links in the knowledge base

   - Use regex: `\[\[[^\]]+\]\]`
   - Set maxResults: 100 to grasp the whole

2. Identify frequent links from search results and confirm corresponding file existence with file_search tool

   - Search with `**/*{link name}.md` pattern
   - Judge as broken link if doesn't exist

3. For non-existing link targets, create appropriate files based on these criteria:

   - Programming terms: Create in Words/Programming/
   - Tool/technology terms: Create in Words/Tools/
   - Cloud-related terms: Create in Words/Cloud/
   - Infrastructure-related terms: Create in Words/Infrastructure/
   - Investment-related terms: Create in Words/Finance/
   - Names/authors: Create in Words/Authors/
   - Articles: Create in appropriate Articles/subfolder

4. Created files follow existing format and include basic content

5. Add new terms to 00-Words.md in appropriate categories

6. Report list of repaired broken links and list of newly created files

Notes:

- Replace characters that can't be used in file names (/ \ : \* ? " < > |) appropriately
- Example: "CI/CD" → "CI-CD.md"
- Avoid duplicate headings at same level
- Set appropriate cross-links to clarify connections with related concepts
```

Repairing broken links is important for maintaining knowledge base integrity. Regularly executing this procedure maintains a state where all links function properly.

- For articles: Create in appropriate Articles/subfolder

4. Created files follow existing format and include basic content
5. Report list of repaired broken links and list of newly created files

Repairing broken links is important for maintaining knowledge base integrity.

## Implementation Best Practices

Important notes and recommendations when using AI to organize knowledge base:

### Markdown Format Best Practices

1. **Heading format**:
   - Add blank lines before and after headings
   - Maintain proper hierarchical structure (h1 → h2 → h3)
2. **List format**:
   - Add blank lines before and after lists
   - Use proper indentation for nested lists
3. **Link format**:
   - Always use `[[link target]]` format for internal links
   - `[[link target|display text]]` format also available as needed
4. **Code blocks**:
   - Specify language for code blocks (e.g., ```markdown)
   - Properly wrap inline code with `code`

### File Names and Paths

1. Be careful with special characters in file names (avoid `/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `|`)
2. Use spaces as-is, don't replace with underscores or hyphens
3. Japanese file names also usable as-is

### Other Notes

- Tags are best in alphanumeric but Japanese also usable (e.g., #Programming)
- Create links even if link targets don't exist yet, create corresponding files later
- Content spanning multiple fields should be classified in main field and related to other fields with tags

## Usage Examples

### Example 1: Programming Article Organization

```markdown
Please incorporate the following new web clip into the knowledge base:

Article Title: "Pandas Utilization in Python: Introduction to Data Analysis"
Article URL: https://example.com/python-pandas
Content Summary: Article explaining basic data analysis techniques using Python's pandas library. Covers data frame operations, filtering, visualization, etc.
Author: Taro Yamada
Field: Programming

Please perform the following tasks in batch:

1. Analyze article content and extract important terms and concepts
2. Create detailed explanation files in Words/Programming/ for each extracted term
3. Add or update author information in Words/Authors/Taro Yamada.md
4. Update Tags/Programming Languages.md and associate with #Python tag
5. Classify article in Articles/Programming/
6. Update related index files
7. Create links to existing terms and concepts mentioned in article
8. If there are broken links, create target files
```

### Example 2: Batch Processing of Cloud-Related Articles

```markdown
Please incorporate the following new web clip into the knowledge base:

Article Title: "AWS Lambda vs Azure Functions: Serverless Comparison"
Article URL: https://example.com/serverless-comparison
Content Summary: Article with detailed comparison of AWS and Azure serverless services. Explains differences from perspectives of pricing, scaling, supported languages, etc.
Author: Cloud Expert
Field: Cloud

Please perform the following tasks:

1. Create explanations of important cloud service terms (Lambda, Azure Functions, serverless, etc.) in Words/Cloud/
2. Update AWS, Azure tags in Tags/Cloud Services.md
3. Add author information
4. Classify article appropriately and update indexes
```

## Manual Usage

This manual is particularly useful in the following scenarios:

1. **When adding new articles** - Use when organizing articles clipped from web
2. **When organizing existing content** - When requesting organization of already existing articles or terms
3. **When repairing broken links** - When repairing broken links in knowledge base
4. **When updating indexes** - When various index updates are needed

When requesting work from AI, please customize and use the instruction templates in this manual as appropriate. This will enable maintaining a consistent knowledge base.

## Adding [[]] Links and Creating Corresponding Files

In Obsidian knowledge base, links between terms are created in [[]] format. When organizing articles, it's necessary to add [[]] to important terms and confirm corresponding files exist.

【Important Principle】When creating [[]] links, always confirm that the corresponding .md file exists, and create it immediately if it doesn't. This is to prevent generation of isolated graph nodes in Obsidian.

### Comprehensive [[]] Link Processing Procedure

Standard procedure for systematically adding [[]] links to all articles and creating corresponding files:

```markdown
Please execute the procedure for comprehensively checking [[]] format links in currently held articles and necessarily creating corresponding files for all articles.

【Strict Rule】When [[]] links exist, the state of non-existing corresponding .md files is prohibited.

Procedure:

1. **Comprehensive [[]] link search across all articles**

   - Search `Articles/**/*.md` with regex `\[\[[^\]]+\]\]` using grep_search tool
   - Extract and list all [[]] links

2. **Link corresponding file existence confirmation and immediate creation**

   - file_search with `**/*{term name}.md` for each extracted term
   - If non-existing file is found, create immediately (creating "later" is prohibited)

3. **Immediate creation of missing files**

   - Place in appropriate directories by technical field:
     - Programming terms: Words/Programming/
     - Development tools: Words/Tools/
     - Cloud technology: Words/Cloud/
     - Infrastructure technology: Words/Infrastructure/
     - Investment/Finance: Words/Finance/
     - Authors/Names: Words/Authors/

4. **Standardizing file content**
   Create each file with the following structure:

# {term name}

{1-2 lines of concise and accurate definition}

## Main Features

- {feature 1}
- {feature 2}
- {feature 3}

## {field-specific section}

### {category 1}

- {specific explanation}

### {category 2}

- {specific explanation}

## Utilization in [[Personal Development]] (when applicable)

- {practical utilization methods}
- {specific benefits}

## Related Concepts

- [[Related term 1]] - Explanation of relationship
- [[Related term 2]] - Explanation of relationship

5. **Update 00-Words.md**
   - Classify and add newly created files to appropriate categories
   - Organize maintaining hierarchical structure

Notes:

- File names must exactly match terms in [[]]
- Properly escape or replace special characters
- Build knowledge network with cross-links
- Skip creation if existing file present
```

### Procedure for Adding [[]] Links Within Articles

```markdown
Please add [[]] links to important terms in article "{article title}".

【Important】When creating [[]] links, always perform existence confirmation and creation of corresponding .md files.
To prevent mass generation of graph nodes with non-existing link targets in Obsidian, file creation is mandatory simultaneously with link creation.

Procedure:

1. Analyze article content and identify the following types of important terms:

   - Technical terms (programming languages, tools, concepts, etc.)
   - Names (authors, developers, researchers, etc.)
   - Company/service names (GitHub, AWS, Google, etc.)
   - Method/process names (agile development, CI/CD, code review, etc.)

2. Execute the following sequentially for each identified term:

   a) Confirm corresponding file existence with file_search tool

   - Search pattern: `**/*{term name}.md`

   b) If file doesn't exist, create new one (following classification criteria below)

   c) After confirming file existence, linkify term by surrounding with [[]]

   - Example: "Python" → "[[Python]]"
   - Example: "GitHub Actions" → "[[GitHub Actions]]"

3. When same term appears multiple times, only linkify first occurrence

4. Don't linkify terms in existing links or headings

Notes:

- Always create corresponding file before linkification
- Don't linkify overly general terms ("system", "method", etc.)
- Don't linkify article title itself
- Don't linkify terms not important in context
```

### Mandatory: Creating [[]] Link Corresponding Files

```markdown
【Warning】When creating [[]] links, corresponding .md files must exist.
To prevent isolated graph nodes in Obsidian, strictly follow this procedure.
Procedure for creating corresponding files for linkification terms:

1. Always confirm corresponding file existence for each [[]] link

   - Search with `**/*{term name}.md` pattern using file_search tool
   - If doesn't exist, always create new one

2. Classification criteria for new file creation:

   Technical term classification:

   - Programming languages/technology: Words/Programming/
   - Development tools/AI technology: Words/Tools/
   - Cloud services: Words/Cloud/
   - Infrastructure technology: Words/Infrastructure/
   - Investment/financial technology: Words/Finance/

   Other classifications:

   - Names: Words/Authors/
   - Companies/organizations: Words/Tools/ or appropriate field
   - Articles: Articles/{appropriate subfolder}/

3. Mandatory elements for newly created files:

   - Appropriate heading (# term name)
   - Basic explanation (minimum 2-3 lines)
   - Related concepts section ([[]] links to other related terms)
   - Personal development utilization section (when applicable)

4. Addition to 00-Words.md:

   - Add new terms to appropriate categories
   - Include concise explanatory text

5. Confirmation after creation completion:

   - Confirm corresponding files exist for all [[]] links
   - Report list of created files

Absolute principles to follow:

- When [[]] links are created, state of non-existing corresponding .md files is not permitted
- Execute file creation simultaneously with link creation
- "Create later" is prohibited, always create immediately
```

### Building Knowledge Network

Through this procedure, important concepts in articles are properly linked, building a consistent knowledge network throughout the knowledge base.

- **Discoverability**: Easily find related concepts
- **Understanding promotion**: Clear definitions and relationships of terms
- **Maintainability**: Add new information by relating to existing knowledge
- **Consistency**: Provide unified information for same concepts

### Dynamic Directory Structure Management

When articles/terms in new genres or fields are added, existing directory structure may not adequately classify them. In such cases, create new directories dynamically following this procedure.

#### Criteria for Deciding to Create New Directories

Consider creating new directories when any of the following conditions are met:

1. **When 3 or more articles/terms that can't be properly classified in existing directories have accumulated**
2. **Emergence of new technical fields/concept domains** (e.g., quantum computing, blockchain, bioinformatics, etc.)
3. **When subcategories within existing directories reach 5 or more**

#### Procedure for Creating New Directories

**STEP 1: Update directory description files**

Before creating new directories, always update the applicable parent directory description file (e.g., 00-Articles.md, 00-Words.md):

```
Please update {parent directory}/parent directory name.md:

New subdirectory: {new directory name}/
Description: {description of fields/concepts that directory handles}
Target articles/terms: {list of articles/terms to be moved}

Please add description of new directory according to existing description file structure.
```

**STEP 2: Create directories and files**

1. Create new directory
2. Create description file in "directory name.md" format directly under directory
3. Move related articles/term files to new directory

**STEP 3: Update index files**

- Articles/00-Articles.md
- Words/00-Words.md
- 00-Words.md
- README.md

Please update these files according to new directory structure.

#### Mandatory Creation of Directory Description Files

**Important Principle**: Always create description files in "directory name.md" format directly under all directories.

**Standard structure for description files**:

```markdown
# {directory name}

## Overview

This directory manages {articles/terms} related to {field/concept description}.

## Target Scope

- {specific target 1}
- {specific target 2}
- {specific target 3}

## Subdirectories

### {subdirectory 1}/

{description of subdirectory 1}

### {subdirectory 2}/

{description of subdirectory 2}

## Related Links

- [[higher concept]]
- [[related field]]

## Update History

- {date}: Directory creation
- {date}: {subdirectory} addition
```

#### Directory Naming Conventions

- **Use English names**: For international understanding and file path compatibility
- **PascalCase**: Capitalize first letter of words (e.g., MachineLearning, QuantumComputing)
- **Avoid abbreviations**: ArtificialIntelligence instead of AI (except widely recognized abbreviations)
- **Plural form**: Show that contents are multiple (e.g., Languages, Frameworks)

## Specialized Procedure for Broken Link Detection/Repair

Please implement the following detection/repair procedure to prevent broken links in Obsidian:

### Regular Broken Link Checks

**Mandatory check to implement after every work session:**

```
Please detect and repair broken links in my Obsidian knowledge base.

【Detection Procedure】
1. Search for all [[]] links using grep_search with "\\[\\[.*\\]\\]"
2. Confirm corresponding file existence for each link target using file_search
3. List non-existing files

【Repair Procedure】
1. Check appropriate placement location in 00-FileIndex.md
2. Create non-existing files based on these criteria:
   - Programming terms: Words/Programming/
   - Tool/technology terms: Words/Tools/
   - Cloud-related terms: Words/Cloud/
   - Infrastructure-related terms: Words/Infrastructure/
   - Investment-related terms: Words/Finance/
   - Names/authors: Words/Authors/
   - Articles: appropriate Articles/subfolder
3. Update 00-FileIndex.md
4. Perform broken link check again as final confirmation

【Reporting Items】
- Number and list of detected broken links
- List of newly created files
- Confirmation of repair completion
```

### Preventive Link Management

**Prevention measures during new work:**

1. **Pre-planning**: List [[]] links to be created
2. **Batch confirmation**: Pre-existence confirmation in 00-FileIndex.md
3. **Batch creation**: Create all missing files first
4. **Gradual link addition**: Add only confirmed links
5. **Regular checks**: Final confirmation after work completion

### Error Patterns and Countermeasures

**Common broken link patterns:**

1. **Notation variations**: "JavaScript" vs "Javascript"

   - Countermeasure: Decide primary notation and handle with alias settings

2. **File name character restrictions**: "CI/CD" → can't use in file names

   - Countermeasure: Convert appropriately to "CI-CD.md", etc.

3. **Cascading non-creation**: [[Container]] in Docker.md not created

   - Countermeasure: Create all related files in advance

4. **Case mismatch**: [[Python]] and [[python]]
   - Countermeasure: Maintain unified naming conventions

### Quality Assurance Checklist

**Final confirmation before work completion:**

- [ ] Confirmed no broken links using grep_search
- [ ] Updated 00-FileIndex.md to latest state
- [ ] Basic content written in newly created files
- [ ] Updated related higher indexes (00-Words.md, etc.)
- [ ] Confirmed normal link display in Obsidian
