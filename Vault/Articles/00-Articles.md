# 00-Articles

This folder stores web pages and articles collected using Obsidian Web Clipper and other tools.

## 📁 Category Structure

### Cloud/

Articles related to cloud services and cloud computing

- AWS, Azure, Google Cloud Platform
- Serverless technology
- Cloud-native development

### Finance/

Articles related to finance, investment, and economics

- Stock investment strategies
- Cryptocurrency
- Economic analysis
- Fintech

### Infrastructure/

Articles related to IT infrastructure and system foundations

- Docker, Kubernetes
- Network technology
- Security
- DevOps

### Programming/

Articles related to programming languages and development technologies

- Various programming languages
- Frameworks
- Algorithms
- Software design

### Tools/

Articles related to development tools and software

- IDEs, editors
- Development support tools
- AI tools
- Productivity tools

## 🔧 Directory Management Rules

### When Adding New Categories

When articles that don't fit into existing categories reach 5 or more, consider creating new directories:

1. **Create new directory**: Articles/{new directory name}/
2. **Move related articles**: Move articles from existing directories
3. **Create directory description file**: Articles/{new directory name}/00-Articles-{new directory name}.md (directly under the applicable directory)
4. **Update this index**: Add new category to this file

### Subdirectory Creation Rules

When articles in a single category exceed 10:

1. **Create subcategories by technology/field**
2. **Create subcategory overview files**
3. **Update parent category description**

## 📝 Article Format

All article files should maintain the following format:

```markdown
# Article Title

> **Source**: [Original URL] > **Author**: Author Name
> **Date**: Collection Date

## Summary

Brief summary of article content

## Content

Main article content

## Related Terms

- ((Related Term 1)) - Use [[]] syntax when linking to actual existing files
- ((Related Term 2)) - Use [[]] syntax when linking to actual existing files

## Tags

#tag1 #tag2 #tag3
```

## 📊 Current Status

**Total Articles**: {To be updated by AI agents}
**Categories**: 5 main categories
**Last Updated**: {To be updated by AI agents}

## 🔗 Related Files

- [[00-Words]] - Term index
- ((00-FileIndex)) - Complete file list

**Important Note for AI Agents**:

- **In Vault documentation**: Use (()) for examples to avoid creating broken links in the knowledge base
- **In Instructions/ directory**: ((Sample)) links are not recognized by Obsidian, so sample format can be used freely for examples and templates
- **When creating actual files**: Always use [[]] syntax when linking to existing files within the Vault
- **Link verification**: Only create [[]] links when the target file actually exists in the Vault
- **Directory-specific rules**:
  - Vault/ → Use (()) for examples, [[]] only for real files
  - Instructions/ → Can use [[]] freely for examples since they're not processed by Obsidian
- Individual category overview files in each subdirectory

## 🔄 Dynamic Directory Management

**Instructions for AI Agents**: When articles in new fields that don't fit existing categories accumulate (3 or more), create new directories following these steps:

1. **Update this file (00-Articles.md)**: Add new directory description to the Category Structure section
2. **Create new directory**: Articles/{NewDirectoryName}/
3. **Create directory description file**: 00-Articles-{NewDirectoryName}.md (in the new directory)
4. **Update README.md**: Reflect new category in project root README.md

**Examples of new categories**:

- QuantumComputing/ (Quantum Computing)
- Blockchain/ (Blockchain)
- MachineLearning/ (Machine Learning & AI)
- GameDevelopment/ (Game Development)
- Biotechnology/ (Biotechnology)

## 🔄 Automated Processing by AI Agents

Articles in this folder are automatically processed by AI agents for:

1. **Article Analysis**: Analyze content and identify important terms
2. **Term Extraction**: Extract technical terms, names, service names, etc.
3. **Classification**: Categorize into appropriate Words categories
4. **Link Generation**: Build relationships with Obsidian bidirectional links

## 📝 Procedure for Adding Articles

1. Clip articles using Obsidian Web Clipper
2. Save to appropriate category folder
3. Request processing from AI Agent:

   ```text
   Please analyze Articles/[Category]/[ArticleName].md and
   extract and organize terms according to the AI Manual.
   ```

## ⚠️ Precautions

- Consider copyright and save as summaries or quotes when necessary
- Include article source URL and acquisition date/time
- Avoid content containing personal or confidential information

---

This folder functions as an input point for knowledge base construction and automatically converts to structured knowledge in cooperation with AI agents.
