#!/usr/bin/env python3
"""
Simple Obsidian Knowledge Base Link Checker
Check internal links in [[]] format and output broken link list ranked by frequency
"""

import os
import re
import json
from pathlib import Path
from typing import List, Dict, Set, Tuple
from collections import Counter


class ObsidianLinkChecker:
    def __init__(self, workspace_path: str = "."):
        self.workspace_path = Path(workspace_path)
        self.vault_path = self.workspace_path / "Vault"
        self.broken_links = []
        self.existing_files = set()
        self.link_pattern = re.compile(r'\[\[([^\]]+)\]\]')
        
    def scan_existing_files(self) -> Set[str]:
        """Scan all .md files in Vault and create a set of file names"""
        md_files = set()
        
        # Display error message if Vault directory doesn't exist
        if not self.vault_path.exists():
            print(f"Error: Vault directory not found: {self.vault_path}")
            return md_files
        
        for root, dirs, files in os.walk(self.vault_path):
            for file in files:
                if file.endswith('.md'):
                    # File name without extension
                    base_name = file[:-3]
                    md_files.add(base_name)
                    
                    # Also add full path format (relative path from Vault)
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
    
    def is_template_placeholder(self, link_target: str) -> bool:
        """Check if it's a template placeholder"""
        placeholders = [
            'Term Name', 'Related Term 1', 'Related Term 2', 'Related Term 3',
            'Tag Name', 'Tool Name', 'Service Name', 'Author Name',
            'File Name', 'Category Name', 'Project Name',
            'Article Title', 'Concept Name', 'Technology Name'
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
    
    def check_all_links(self) -> Dict:
        """Check all file links in Vault and collect only broken links"""
        self.scan_existing_files()
        
        # Scan all .md files in Vault
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
                            
                        # Record only broken links
                        if not self.check_link_exists(link_target):
                            self.broken_links.append({
                                'file': rel_path,
                                'line': line_num,
                                'target': link_target,
                                'content': line_content.strip()
                            })
        
        return self.generate_report()
    
    def generate_report(self) -> Dict:
        """Generate broken link report (ranked by frequency)"""
        # Count frequency of broken link targets
        broken_targets = Counter(link['target'] for link in self.broken_links)
        
        # Sort by frequency
        sorted_broken = sorted(broken_targets.items(), key=lambda x: x[1], reverse=True)
        
        report = {
            'broken_links_count': len(self.broken_links),
            'unique_broken_targets': len(broken_targets),
            'broken_targets_ranked': [
                {'target': target, 'count': count} 
                for target, count in sorted_broken
            ],
            'detailed_broken_links': self.broken_links
        }
        
        return report
    
    def print_simple_report(self):
        """Print minimal necessary report to console"""
        report = self.generate_report()
        
        print(f"Broken links: {report['broken_links_count']} items")
        
        if report['broken_links_count'] > 0:
            print("\nBroken link ranking (by frequency):")
            for i, item in enumerate(report['broken_targets_ranked'][:30], 1):
                print(f"{i:2d}. {item['target']} ({item['count']} times)")
    
    def save_report(self, output_file: str = "broken_links.json"):
        """Save report to JSON file"""
        report = self.generate_report()
        
        output_path = self.workspace_path / output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print(f"Report saved: {output_path}")
        return output_path
    

def main():
    """Main execution function (Vault-only version)"""
    import sys
    
    # Set workspace path
    if len(sys.argv) > 1:
        workspace_path = sys.argv[1]
    else:
        workspace_path = "."  # Current directory
    
    print(f"Search target: {os.path.abspath(workspace_path)}/Vault")
    
    checker = ObsidianLinkChecker(workspace_path)
    
    try:
        # Execute check
        checker.check_all_links()
        
        # Display results (simple)
        checker.print_simple_report()
        
        # Save report
        checker.save_report()
        
    except KeyboardInterrupt:
        print("Process was interrupted")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
