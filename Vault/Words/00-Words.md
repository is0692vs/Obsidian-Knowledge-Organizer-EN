---
title: "Words - Glossary"
created: 2025-06-13
description: "Detailed glossary of technical terms and concepts"
tags:
  - "index"
  - "MOC"
  - "glossary"
aliases:
  - "glossary"
---

# Words - Technical Glossary

This page is an index of the technical terms and concepts glossary stored in the Words folder. It provides detailed explanations of important terms referenced in Clippings and other notes.

## 📁 Category Structure

### Authors/

Information about article authors, notable figures, and experts

- Technical writers
- Industry experts
- Researchers
- Entrepreneurs

### Cloud/

Terms related to cloud services and platforms

- AWS, Azure, Google Cloud services
- Cloud architecture
- Serverless technology
- Container orchestration

### Finance/

Terms related to finance, investment, and economics

- Investment strategies and methods
- Financial products
- Economic indicators
- Fintech technology

### Infrastructure/

Terms related to IT infrastructure and system foundations

- Network technology
- Security
- Databases
- Monitoring and operations tools

### Programming/

Programming languages and development technology related terms

- Programming languages
- Frameworks and libraries
- Development methods and concepts
- Algorithms

### Services/

Web services, applications, and platforms

- SaaS products
- Development support services
- Communication and collaboration tools
- Entertainment services

### Tools/

Development tools and software related terms

- IDEs and editors
- Build and deployment tools
- AI tools
- Productivity tools

## 🔄 Dynamic Directory Management

**Instructions for AI Agents**: When terms in new fields that don't fit existing categories accumulate (5 or more), create new directories following these steps:

1. **Update this file (00-Words.md)**: Add new directory description to the Category Structure section
2. **Create new directory**: Words/{NewDirectoryName}/
3. **Create directory description file**: 00-Words-{NewDirectoryName}.md (in the directory)
4. **Update file index**: Add new category section to the main file index
5. **Update README.md**: Reflect new category in project root README.md

**Examples of new categories**:

- QuantumComputing/ (Quantum computing terms)
- Blockchain/ (Blockchain and cryptographic technology)
- MachineLearning/ (Machine learning and AI terms)
- GameDevelopment/ (Game development terms)
- Biotechnology/ (Biotechnology terms)
- IoT/ (IoT and edge computing)
- AR_VR/ (Augmented reality and virtual reality)

## How to Use This Folder

This folder collects important terms that form the foundation of the knowledge base. When adding new terms, consider the following points:

1. **Front matter** - Basic information like title, created, tags
2. **Concise definition** - Write a concise definition at the beginning
3. **Structured content** - Structure logically using headings
4. **Cross-links** - Links to other related terms
5. **External links** - Links to official sites and documentation

## 🔧 Automated Processing by AI Agents

Terms in this folder are automatically processed by AI agents for:

1. **Term extraction**: Identify technical terms, names, service names from articles
2. **Duplicate checking**: Check for duplicates and notation variations with existing terms
3. **Classification**: Categorize into appropriate folders
4. **File creation**: Create corresponding Markdown files for each term
5. **Link generation**: Build bidirectional links with related terms
6. **Index updates**: Add new terms to relevant index files

## 📝 Standard Structure for Term Files

Each term file follows this structure:

```markdown
# Term Name

## Overview

Basic explanation of the term

## Details

More detailed explanation and technical content

## Related Terms

- ((Related Term 1)) - Use [[]] syntax when linking to actual existing files
- ((Related Term 2)) - Use [[]] syntax when linking to actual existing files

## Related Articles

- ((Article Title 1)) - Use [[]] syntax when linking to actual existing files
- ((Article Title 2)) - Use [[]] syntax when linking to actual existing files

## External Links

- [Official Site](URL)
- [Documentation](URL)

## Tags

#CategoryName #SubCategory
```

**Important Note for AI Agents**:

- In this documentation, we use (()) for examples to avoid creating broken links
- When creating actual files and linking to existing files, always use [[]] syntax
- Only create [[]] links when the target file actually exists
- Never create [[]] links to non-existent example files like [[Sample Article]] or [[Example Term]]
