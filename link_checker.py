#!/usr/bin/env python3
"""
Obsidian Knowledge Base Link Checker
Check internal links in [[]] format and identify links without corresponding files
"""

import os
import re
import json
from pathlib import Path
from typing import List, Dict, Set, Tuple


class ObsidianLinkChecker:
    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)
        self.broken_links = []
        self.all_links = []
        self.existing_files = set()
        self.link_pattern = re.compile(r'\[\[([^\]]+)\]\]')
        
    def scan_existing_files(self) -> Set[str]:
        """Scan all .md files in workspace and create a set of file names"""
        md_files = set()
        
        for root, dirs, files in os.walk(self.vault_path):
            for file in files:
                if file.endswith('.md'):
                    # File name without extension
                    base_name = file[:-3]
                    md_files.add(base_name)
                    
                    # Also add full path format (relative path)
                    rel_path = os.path.relpath(os.path.join(root, file), self.vault_path)
                    rel_path_no_ext = rel_path[:-3]
                    md_files.add(rel_path_no_ext)
        
        self.existing_files = md_files
        return md_files
    
    def extract_links_from_file(self, file_path: Path) -> List[Tuple[str, int, str]]:
        """Extract [[]] links from file"""
        links = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    matches = self.link_pattern.findall(line)
                    for match in matches:
                        # For pipe links ([[link_target|display_name]]), get only the link target
                        link_target = match.split('|')[0].strip()
                        links.append((link_target, line_num, line.strip()))
        except (UnicodeDecodeError, FileNotFoundError) as e:
            print(f"File read error: {file_path} - {e}")
        
        return links
    
    def check_all_links(self) -> Dict:
        """Check all file links"""
        print("🔍 Scanning files...")
        self.scan_existing_files()
        print(f"📁 Files found: {len(self.existing_files)}")
        
        print("\n🔗 Checking links...")
        
        # Scan all .md files
        for root, dirs, files in os.walk(self.vault_path):
            for file in files:
                if file.endswith('.md'):
                    file_path = Path(root) / file
                    rel_path = os.path.relpath(file_path, self.vault_path)
                    
                    links = self.extract_links_from_file(file_path)
                    
                    for link_target, line_num, line_content in links:
                        # Skip template placeholders
                        if self.is_template_placeholder(link_target):
                            continue
                            
                        link_info = {
                            'file': rel_path,
                            'line': line_num,
                            'target': link_target,
                            'content': line_content,
                            'exists': self.check_link_exists(link_target)
                        }
                        
                        self.all_links.append(link_info)
                        
                        if not link_info['exists']:
                            self.broken_links.append(link_info)
        
        return self.generate_report()
    
    def is_template_placeholder(self, link_target: str) -> bool:
        """Check if it's a template placeholder"""
        placeholders = [
            'Term Name', 'Related Term 1', 'Related Term 2', 'Related Term 3',
            'Tag Name', 'Tool Name', 'Service Name', 'Author Name',
            'File Name', 'Category Name', 'Project Name',
            'Article Title', 'Concept Name', 'Technology Name',
            # Japanese placeholders (for backward compatibility)
            '用語名', '関連用語1', '関連用語2', '関連用語3',
            'タグ名', 'ツール名', 'サービス名', '著者名',
            'ファイル名', 'カテゴリ名', 'プロジェクト名',
            '記事タイトル', '概念名', '技術名'
        ]
        
        return link_target in placeholders
    
    def check_link_exists(self, link_target: str) -> bool:
        """Check if the link target file exists"""
        # Direct filename match
        if link_target in self.existing_files:
            return True
        
        # Case-insensitive search
        link_lower = link_target.lower()
        for existing_file in self.existing_files:
            if existing_file.lower() == link_lower:
                return True
        
        # Partial match search (suffix match)
        for existing_file in self.existing_files:
            if existing_file.endswith(link_target) or link_target.endswith(existing_file):
                return True
        
        return False
    
    def generate_report(self) -> Dict:
        """Generate report"""
        report = {
            'summary': {
                'total_files': len(self.existing_files),
                'total_links': len(self.all_links),
                'broken_links': len(self.broken_links),
                'success_rate': round((len(self.all_links) - len(self.broken_links)) / max(len(self.all_links), 1) * 100, 2)
            },
            'broken_links': self.broken_links,
            'existing_files': sorted(list(self.existing_files))
        }
        
        return report
    
    def print_report(self):
        """Print report to console"""
        report = self.generate_report()
        
        print("\n" + "="*60)
        print("📊 OBSIDIAN BROKEN LINK CHECK RESULTS")
        print("="*60)
        
        summary = report['summary']
        print(f"📁 Total Files: {summary['total_files']}")
        print(f"🔗 Total Links: {summary['total_links']}")
        print(f"❌ Broken Links: {summary['broken_links']}")
        print(f"✅ Success Rate: {summary['success_rate']}%")
        
        if self.broken_links:
            print(f"\n💥 Broken Link Details ({len(self.broken_links)} items):")
            print("-" * 60)
            
            # Group by file
            by_file = {}
            for link in self.broken_links:
                file_name = link['file']
                if file_name not in by_file:
                    by_file[file_name] = []
                by_file[file_name].append(link)
            
            for file_name, links in by_file.items():
                print(f"\n📄 {file_name}")
                for link in links:
                    print(f"   L{link['line']:3d}: [[{link['target']}]]")
                    print(f"        → {link['content'][:100]}")
        
        else:
            print("\n🎉 No broken links found!")
    
    def save_report(self, output_file: str = "link_check_report.json"):
        """Save report to JSON file"""
        report = self.generate_report()
        
        output_path = self.vault_path / output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print(f"\n💾 Report saved: {output_path}")
        return output_path
    
    def get_broken_links_array(self) -> List[str]:
        """Return list of broken link targets"""
        return [link['target'] for link in self.broken_links]
    
    def suggest_fixes(self):
        """Generate fix suggestions"""
        if not self.broken_links:
            return
        
        print("\n🔧 Fix Suggestions:")
        print("-" * 60)
        
        # Make broken targets unique and sort by frequency
        broken_targets = {}
        for link in self.broken_links:
            target = link['target']
            if target not in broken_targets:
                broken_targets[target] = 0
            broken_targets[target] += 1
        
        sorted_targets = sorted(broken_targets.items(), key=lambda x: x[1], reverse=True)
        
        for target, count in sorted_targets[:10]:  # Top 10
            print(f"📝 '{target}' (appears {count} times)")
            
            # Search for similar file names
            similar_files = self.find_similar_files(target)
            if similar_files:
                print(f"   💡 Similar files: {', '.join(similar_files[:3])}")
            else:
                print(f"   ➕ New file needed: {target}.md")
            print()


    def find_similar_files(self, target: str, threshold: float = 0.6) -> List[str]:
        """Search for similar file names (simple version)"""
        target_lower = target.lower()
        similar = []
        
        for existing_file in self.existing_files:
            existing_lower = existing_file.lower()
            
            # Check if substring is contained
            if target_lower in existing_lower or existing_lower in target_lower:
                similar.append(existing_file)
        
        return similar

    def get_unique_broken_links(self) -> List[str]:
        """Get list of unique broken file names (for AI agents)"""
        if not self.broken_links:
            return []
        
        # Get unique broken file names excluding placeholders
        broken_targets = set()
        for link in self.broken_links:
            target = link['target']
            if not self.is_template_placeholder(target):
                broken_targets.add(target)
        
        # Sort by frequency
        target_counts = {}
        for link in self.broken_links:
            target = link['target']
            if target in broken_targets:
                target_counts[target] = target_counts.get(target, 0) + 1
        
        # Sort by frequency
        sorted_targets = sorted(target_counts.items(), key=lambda x: x[1], reverse=True)
        return [target for target, count in sorted_targets]
    
    def print_creation_list(self):
        """Print list of files to create for AI agents"""
        unique_targets = self.get_unique_broken_links()
        
        if not unique_targets:
            print("\n✅ No files need to be created!")
            return
        
        print(f"\n📋 For AI Agents: List of Files to Create ({len(unique_targets)} items)")
        print("=" * 60)
        print("🤖 Please interpret the meaning of the following file names and create them in appropriate directories:")
        print("-" * 60)
        
        for i, target in enumerate(unique_targets, 1):
            # Get frequency
            count = sum(1 for link in self.broken_links if link['target'] == target)
            print(f"{i:2d}. {target} (references: {count} times)")
        
        print("-" * 60)
        print("📁 Recommended placement directories:")
        print("   Words/Programming/  - Programming-related terms")
        print("   Words/Tools/        - Tools & AI technology") 
        print("   Words/Cloud/        - Cloud services")
        print("   Words/Infrastructure/ - Infrastructure & servers")
        print("   Words/Finance/      - Investment & finance")
        print("   Words/Authors/      - Names & authors")
        print("   Words/Services/     - Services & tags")
        print("=" * 60)


def main():
    """
    Main execution function - with session termination condition check
    Return value: True = Session termination condition achieved (0 broken links)
                 False = Session termination condition not achieved (broken links exist)
    """
    import sys
    
    # Set workspace path
    if len(sys.argv) > 1:
        vault_path = sys.argv[1]
    else:
        vault_path = "."  # Current directory
    
    print("🔗 OBSIDIAN BROKEN LINK CHECKER")
    print("📋 Session termination condition: Number of broken links = 0")
    print(f"📂 Target path: {os.path.abspath(vault_path)}")
    print("=" * 60)
    
    checker = ObsidianLinkChecker(vault_path)
    
    try:
        # Execute check
        report = checker.check_all_links()
        
        # Display results
        checker.print_report()
        
        # Session termination condition check
        broken_count = len(checker.broken_links)
        
        print("\n" + "=" * 60)
        print("🎯 Session Termination Condition Check")
        print("=" * 60)
        
        if broken_count == 0:
            print("✅ Session termination condition achieved!")
            print("🎉 Broken links count: 0")
            print("✨ Knowledge base link integrity is perfect")
            print("=" * 60)
            return True
        else:
            print("⚠️  Session termination condition not achieved")
            print(f"💥 Broken links count: {broken_count}")
            print("\n📝 Next steps:")
            print("   1. AI agent creates the broken link files listed below")
            print("   2. After creation, run this script again")
            print("   3. Session complete when broken links = 0")
            
        # Save report
        checker.save_report()
        
        # Display file creation list for AI agents
        if broken_count > 0:
            checker.print_creation_list()
        
        # Detailed fix suggestions
        checker.suggest_fixes()
        
        print("\n" + "=" * 60)
        print("🤖 Information for AI Agents:")
        print(f"   Files to create: {broken_count}")
        print("   Please refer to the above fix suggestions for details")
        print("=" * 60)
        
        return False
        
    except KeyboardInterrupt:
        print("\n⏹️  Process was interrupted")
        return False
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    main()
