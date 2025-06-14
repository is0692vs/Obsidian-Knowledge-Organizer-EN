# 🔗 09_Link Creation Criteria and Guidelines

## Link Creation Practical Guide (Workflow)

### Step 1: Term Identification and Existing File Verification Phase

```text
【Term Extraction and Verification Procedure】
1. Read through articles and mark technical terms
2. Identify author names and service names
3. Extract important concepts and keywords
4. 【Important】Process replacement for terms containing slashes:
   - Convert "CI/CD" → "CI_CD"
   - Convert "HTML/CSS" → "HTML_CSS"
   - Convert "OS/2" → "OS_2"
   - Unify term notation at this stage before proceeding
5. 【Important】Check existing files using file_search for each term
5. 【Important】Check for excessive fragmentation:
   - If API.md exists → Use ((API)) instead of "API Design", "API Management", etc.
   - If Docker.md exists → Use ((Docker)) instead of "Docker Basics", "Docker Configuration", etc.
   - Don't create new files for concepts that can be covered by existing files
6. 【Important】Type-specific search strategies for notation variations:
   - 【Rule-based Detection】Notation variations by string patterns:
     * Space/hyphen: "OpenAI API" → file_search("OpenAI*API")
     * Case: "JavaScript" → grep_search("javascript", isRegexp=false)
     * Abbreviation/expansion: "API" → file_search("Application*Programming*Interface")
   - 【Semantic Detection】Notation variations requiring contextual understanding:
     * Japanese/English mix: "AI" → semantic_search("artificial intelligence machine learning")
     * Abbreviation/formal: "Azure" → semantic_search("Microsoft Azure MS Azure")
     * Synonyms: "framework" → semantic_search("library framework toolkit")
7. Check similar terms in the same directory using semantic_search
8. Prioritize considering link density
```

### Step 2: Notation Unification and Link Name Decision Phase

```text
【Notation Unification and Link Name Decision Procedure】
1. When existing files are found:
   → Unify notation to existing file names
   → Change notation in text to existing link names
   → Use existing files even with modifiers if the core concept is the same
2. When multiple similar files are found:
   → Select the most general and shortest notation as the main file
   → Change other files to redirect format
3. When no existing files are found:
   → Re-search with core concept excluding modifiers
   → Avoid creating new files if comprehensive files exist
   → Create new files only for truly new concepts
4. Final link name decision
```

### Step 3: Link Creation Execution Phase

```text
【Link Creation Execution Procedure】
1. Check target file existence using file_search
2. Create term file if it doesn't exist
3. 【Important】Replace slashes with _ and insert links:
   - Text "CI/CD" → ((CI_CD))
   - Text "HTML/CSS" → ((HTML_CSS))
   - Text "OS/2" → ((OS_2))
4. Execute broken link check
5. Proceed to next term
```

## Basic Principles of Link Creation

### 1. Link Creation Judgment Criteria

#### 【Highest Priority】Active Utilization of Existing Files Rule

**Terms with existing .md files must be linked:**

```text
【Existing File Verification and Linking Procedure】
1. Always execute file_search to verify term existence
2. 【Important】Additional search for notation variation detection:
   - For terms with spaces/hyphens, also search without them
   - Example: "OpenAI API" → file_search("OpenAI*API") or grep_search("OpenAI.*API", isRegexp=true)
   - Example: "React-Router" → file_search("React*Router") or grep_search("React.*Router", isRegexp=true)
3. If exists, actively link regardless of notation
4. Execute unification process if notation variations exist
5. Execute integration process if multiple files with same meaning exist

【Important】Avoid excessive concept fragmentation:
- For example, if API.md exists, use ((API)) instead of ((API Design))
- Don't create new files for topics that can be handled within existing file scope
- Avoid modified links with "Design", "Management", "Basics", etc.
- Prioritize handling details within comprehensive concept files
```

#### 【Important】Types of Notation Variations and Detection Methods

Notation variations can be broadly divided into two types, each requiring different detection methods:

##### 🔍 **1. Rule-based Detectable Notation Variations**

**Features: Mechanically detectable by string patterns**

```text
【Examples of Rule-based Notation Variations】
✓ Space/hyphen/underscore:
  - OpenAI API ⟷ OpenAI-API ⟷ OpenAI_API ⟷ OpenAIAPI
  - React Router ⟷ React-Router ⟷ ReactRouter
  - Vue.js CLI ⟷ Vue.js-CLI ⟷ VuejsCLI

✓ Case variations:
  - JavaScript ⟷ javascript ⟷ Javascript
  - GitHub ⟷ github ⟷ Github

✓ Abbreviation/expansion:
  - API ⟷ Application Programming Interface
  - CLI ⟷ Command Line Interface
  - URL ⟷ Uniform Resource Locator
```

**Detection Methods:**

- `file_search("term1*term2")` for wildcard search
- `grep_search("term1.*term2", isRegexp=true)` for regex search
- Reliable detection through string pattern matching

##### 🧠 **2. Notation Variations Requiring Semantic Interpretation**

**Features: Difficult to detect without contextual understanding**

```text
【Examples of Semantic Notation Variations】
✓ Language mixing:
  - AI ⟷ artificial intelligence ⟷ machine learning
  - Cloud ⟷ クラウド ⟷ cloud computing
  - Database ⟷ データベース ⟷ DB

✓ Abbreviation/formal name:
  - Microsoft Azure ⟷ Azure ⟷ MS Azure
  - Amazon Web Services ⟷ AWS ⟷ Amazon Web Services
  - Google Cloud Platform ⟷ GCP ⟷ Google Cloud

✓ Synonyms/near-synonyms:
  - Machine Learning ⟷ ML ⟷ Artificial Intelligence
  - Programming ⟷ Coding ⟷ Development
  - Framework ⟷ Library (context-dependent)
```

**Detection Methods:**

- Execute `semantic_search()` for semantic similarity search
- AI agent contextual understanding and judgment required
- Check semantic relationships with terms in the same directory

##### 🚨 **Detection Strategy Usage Guidelines**

```text
【Execution Order for Notation Variation Detection】
1. First execute rule-based search (fast & reliable)
   → Pattern matching with file_search, grep_search
2. Then execute semantic search (careful & judgment-based)
   → Detect similar concepts with semantic_search
3. Combine both results for integrated judgment
   → Final semantic judgment by AI agent
```

**Examples of Notation Unification:**

- Microsoft Azure ⟷ Azure → Unify both to [[Azure]]
- OpenAI API ⟷ OpenAI-API ⟷ OpenAIAPI → Unify all to [[OpenAI API]] (prioritize space version)
- React Router ⟷ React-Router ⟷ ReactRouter → Unify all to [[React Router]] (prioritize space version)
- AI ⟷ artificial intelligence → Unify both to [[AI]] (prioritize shorter version)

**Rules for Space/Hyphen Notation:**

- Official documentation uses spaces → Use space version as main
- Official documentation uses hyphens → Use hyphen version as main
- When unclear → Prioritize space version (for readability)

#### Notation Variation and Synonym Integration Protocol

**【Important】Avoiding Duplicate Files with Same Meaning:**

```text
【Synonym Check and Integration Procedure】
1. Search for similar terms in the same directory before creating new links
2. Detect semantically identical terms with semantic_search
3. Execute integration process when notation variations or synonyms are found
4. Select main file (priority: official name > shorter notation > usage frequency)
5. Convert sub-files to redirect format
6. Batch replace existing links to main file notation
```

**Specific Integration Examples:**

**Before Integration:**

```
Words/Tools/OpenAI API.md (detailed content)
Words/Tools/OpenAI-API.md (detailed content)
Words/Tools/ChatGPT API.md (detailed content)
```

**After Integration:**

```
Words/Tools/OpenAI API.md (detailed content - main file)
Words/Tools/OpenAI-API.md (redirect)
Words/Tools/ChatGPT API.md (independent - different service)
```

**Standard Format for Redirect Files:**

```markdown
# OpenAI-API

Synonymous with [[OpenAI API]]. A notation variation of the API service provided by OpenAI.

For details, please refer to [[OpenAI API]].

## Related Concepts

- [[OpenAI API]] - Official notation
```

**Priority Order for Main File Selection:**

1. **Official name** > abbreviations/colloquial terms
2. **Shorter notation** > longer notation (when equivalent)
3. **Usage frequency** > less frequently used terms
4. **English notation** > katakana notation (for technical terms)

**Batch Replacement Execution:**

```text
【Link Notation Unification Procedure】
1. Search all old notation links with grep_search
2. Batch replace all [[old notation]] with [[new notation]]
3. Execute broken link check after replacement
4. Update file structure index.md
```

#### Term Extraction Criteria

**Terms to be linked:**

1. **Technical Terms and Specialized Terms**

   - Programming languages (Python, JavaScript, Go, etc.)
   - Frameworks and libraries (React, Django, Express, etc.)
   - Tools and services (Docker, Git, AWS, etc.)
   - Technical concepts (Object-oriented programming, Functional programming, etc.)

2. **Person Names and Organization Names**

   - Author names and developer names
   - Company names and organization names (only when important)

3. **Important Keywords**
   - Terms related to the main theme of the article
   - Repeatedly mentioned concepts
   - Terms with high relevance to other articles

#### Terms Not to Link

**Links to avoid:**

1. **Overly General Words**

   - Generic terms like "technology", "method", "system", "data"
   - Adjectives like "good", "bad", "simple", "difficult"

2. **Context-dependent Terms**

   - Expressions that only have meaning within the flow of the text
   - Ambiguous terms with multiple meanings

3. **Already Well-explained General Terms**
   - Basic web technologies like HTML, CSS (except for specialized uses)

### 2. Link Density Guidelines

#### Recommended Number of Links per Article

- **Short articles (under 500 characters)**: 3-5 links
- **Medium articles (500-1500 characters)**: 5-10 links
- **Long articles (over 1500 characters)**: 10-20 links

#### Recommended Number of Links per Paragraph

- **Maximum 2-3 links per paragraph** as a guideline
- Avoid consecutive links (prioritize readability)

### 3. Link Naming Conventions

#### Basic Rules

1. **Prioritize Official Names**

   - "JavaScript" (○) vs "JS" (△)
   - "GitHub" (○) vs "ギットハブ" (×)

2. **Replace Slashes with \_ (Mandatory)**

   - "CI/CD" → "CI_CD"
   - "HTML/CSS" → "HTML_CSS"
   - "OS/2" → "OS_2"
   - "TCP/IP" → "TCP_IP"
   - "UI/UX" → "UI_UX"
   - "I/O" → "I_O"

3. **Handling Abbreviations**
   - Common abbreviations are acceptable (API, IDE, CLI, etc.)
   - Prioritize formal names for custom abbreviations

#### Notation Unification Rules

**Priority Order:**

1. **Official name** > casual name
2. **English notation** > katakana notation (for technical terms)
3. **Complete form** > abbreviated form (when ambiguity exists)

## Category-specific Link Creation Guidelines

### Programming Related

**Must link:**

- Programming language names
- Framework and library names
- Design pattern and concept names

**Conditional linking:**

- Basic HTML/CSS (only for special usage cases)
- Common algorithm names (when discussing specific implementations)

### Tools Related

**Must link:**

- Development tool names (VSCode, IntelliJ, etc.)
- AI service names (ChatGPT, GitHub Copilot, etc.)
- Version control tool names

**Conditional linking:**

- OS names (only for OS-specific topics)
- Browser names (only for browser-specific features)

### Infrastructure Related

**Must link:**

- Cloud service names (AWS, Azure, etc.)
- Container technologies (Docker, Kubernetes, etc.)
- Network technologies and protocol names

### Finance Related

**Must link:**

- Investment product and financial product names
- Investment methods and strategy names
- Financial institution names (when important)

## Quality Check Items

### Post-Link Creation Verification

- [ ] Confirm that linked files exist
- [ ] Confirm that link names use official names and unified notation
- [ ] Confirm that slashes are properly replaced with \_
- [ ] Confirm that link density is within appropriate range
- [ ] Confirm that text readability is maintained

### Patterns to Avoid

1. **Excessive Linking**

   - 5 or more links in one paragraph
   - Consecutive linking of adjacent words

2. **Inappropriate Links**

   - Linking overly general terms
   - Terms that have no meaning without context

3. **Notation Inconsistency**

   - Notation variations within the same article
   - Notation inconsistency with existing term files

4. **Excessive Concept Fragmentation**
   - Creating [[API Design]] when API.md exists
   - Creating [[Docker Basics]] when Docker.md exists
   - Unnecessary fragmentation with modified links

## Troubleshooting

### Common Decision Dilemmas

**Q: Should HTML or CSS be linked?**
A: Generally No. However, specific technologies like CSS Grid, Flexbox are acceptable.

**Q: Should all company names be linked?**
A: Only important companies related to the main theme of the article.

**Q: Should abbreviations or formal names be prioritized?**
A: Prioritize commonly used notation. API is ○, Application Programming Interface is ×.

**Q: When the text says "CI/CD", how should the link be handled?**
A: Must use [[CI_CD]]. Keep text notation as "CI/CD", only replace slashes with \_ in links.

**Q: What about slash-containing terms like "HTML/CSS", "TCP/IP", "UI/UX"?**
A: All must be replaced with \_. Use [[HTML_CSS]], [[TCP_IP]], [[UI_UX]].

**Q: When both Microsoft Azure and Azure files exist?**
A: Use shorter version (Azure) as main, change longer version to redirect format. Unify text links to [[Azure]].

**Q: Between AI and artificial intelligence, which should be the main file?**
A: Use shorter and more common "AI" as main, make "artificial intelligence" a redirect.

**Q: What's the judgment criteria when multiple terms with same meaning exist in the same directory?**
A: Priority order: 1.Official name > 2.Shorter notation > 3.Usage frequency > 4.English notation.

**Q: Should I create "API Design" and "API Management" links when API.md exists?**
A: No. Avoid excessive fragmentation, use [[API]]. Handle design and management within API.md.

**Q: Should I create "Docker Basics" and "Docker Introduction" links when Docker.md exists?**
A: No. Use [[Docker]] and prioritize handling from basics to advanced topics within existing files.

**Q: What's the judgment criteria for whether existing files exist?**
A: Execute file_search with core concepts excluding modifiers (design, management, basics, introduction, etc.).

**Q: Between OpenAI API and OpenAI-API, which should be main?**
A: Check official documentation notation. When unclear, prioritize space version [[OpenAI API]].

**Q: When both React Router and React-Router files exist?**
A: Follow official documentation. React official uses space notation, so [[React Router]] is main.

**Q: What's the search method for notation variations with spaces/hyphens?**
A: Execute both file_search("term1*term2") and grep_search("term1.*term2", isRegexp=true).

**Q: How to determine if notation variation is rule-based or semantic?**
A: Detectable by string patterns → rule-based, requires contextual understanding → semantic detection.

**Q: What's the detection method for semantic notation variations like "AI" and "artificial intelligence"?**
A: Search with semantic_search("AI artificial intelligence machine learning").

**Q: What type is "Microsoft Azure" and "Azure"?**
A: Semantic notation variation. Relationship between abbreviation and formal name, requires semantic_search detection.

**Q: When found by both rule-based and semantic detection?**
A: AI agent makes final judgment combining both results. Prioritize more comprehensive files.

### Error Prevention Methods

1. **Prevention of Notation Variations (Type-specific Strategies)**

   - 【Rule-based Notation Variations】Thorough pattern matching search
     - Use combination of file_search + grep_search
     - Check all patterns for space/hyphen/case variations
   - 【Semantic Notation Variations】Similar concept detection with semantic_search
     - Broad search for Japanese-English mix, abbreviation-formal name, synonyms
     - Check semantic relationships with related terms in same directory
   - Final confirmation with Words.md

2. **Prevention of Excessive Linking**

   - Count links per paragraph
   - Re-read to confirm natural flow

3. **Prevention of Broken Links**

   - Thorough pre-confirmation with file_search
   - Immediate check after link creation

4. **Prevention of Forgotten Slash Replacement**

   - Always convert slash-containing terms to \_ at term extraction stage
   - Ensure [[CI_CD]] not [[CI/CD]] during link creation
   - Apply replacement only to links, not text notation

5. **Prevention of Excessive Fragmentation**

   - Search existing files with core concepts excluding modifiers
   - Avoid new file creation when comprehensive files exist
   - Avoid easy addition of "design", "management", "basics", etc.

6. **Two-stage Strategy for Notation Variation Detection**
   - 【Stage 1】Rule-based Detection: Reliable detection through pattern matching
     - file_search("term1*term2") + grep_search("term1.*term2", isRegexp=true)
     - Check all patterns for space/hyphen/case variations
   - 【Stage 2】Semantic Detection: AI contextual understanding and similar concept detection
     - Semantic similar term search with semantic_search()
     - Broad detection of Japanese-English mix, abbreviation-formal name, synonyms
   - Use official documentation notation confirmation as final judgment criteria

---

**Important Note for AI Agents**:

- In this documentation, we use (()) for examples to avoid creating broken links
- When creating actual files and linking to existing files, always use [[]] syntax
- Only create [[]] links when the target file actually exists
- Never create [[]] links to non-existent example files
