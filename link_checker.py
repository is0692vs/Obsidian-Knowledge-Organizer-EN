#!/usr/bin/env python3
"""
Obsidianナレッジベースのリンク切れチェッカー
[[]]形式の内部リンクをチェックし、対応するファイルが存在しないリンクを特定する
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
        """ワークスペース内の全.mdファイルを走査し、ファイル名セットを作成"""
        md_files = set()
        
        for root, dirs, files in os.walk(self.vault_path):
            for file in files:
                if file.endswith('.md'):
                    # 拡張子を除いたファイル名
                    base_name = file[:-3]
                    md_files.add(base_name)
                    
                    # フルパス形式（相対パス）も追加
                    rel_path = os.path.relpath(os.path.join(root, file), self.vault_path)
                    rel_path_no_ext = rel_path[:-3]
                    md_files.add(rel_path_no_ext)
        
        self.existing_files = md_files
        return md_files
    
    def extract_links_from_file(self, file_path: Path) -> List[Tuple[str, int, str]]:
        """ファイルから[[]]リンクを抽出"""
        links = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    matches = self.link_pattern.findall(line)
                    for match in matches:
                        # パイプリンク（[[リンク先|表示名]]）の場合、リンク先のみを取得
                        link_target = match.split('|')[0].strip()
                        links.append((link_target, line_num, line.strip()))
        except (UnicodeDecodeError, FileNotFoundError) as e:
            print(f"ファイル読み込みエラー: {file_path} - {e}")
        
        return links
    
    def check_all_links(self) -> Dict:
        """全ファイルのリンクをチェック"""
        print("🔍 ファイル走査中...")
        self.scan_existing_files()
        print(f"📁 発見されたファイル数: {len(self.existing_files)}")
        
        print("\n🔗 リンクチェック中...")
        
        # 全.mdファイルを走査
        for root, dirs, files in os.walk(self.vault_path):
            for file in files:
                if file.endswith('.md'):
                    file_path = Path(root) / file
                    rel_path = os.path.relpath(file_path, self.vault_path)
                    
                    links = self.extract_links_from_file(file_path)
                    
                    for link_target, line_num, line_content in links:
                        # テンプレート用のプレースホルダーをスキップ
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
        """テンプレート用のプレースホルダーかどうかを判定"""
        placeholders = [
            '用語名', '関連用語1', '関連用語2', '関連用語3',
            'タグ名', 'ツール名', 'サービス名', '著者名',
            'ファイル名', 'カテゴリ名', 'プロジェクト名',
            '記事タイトル', '概念名', '技術名'
        ]
        
        return link_target in placeholders
    
    def check_link_exists(self, link_target: str) -> bool:
        """リンク先ファイルが存在するかチェック"""
        # 直接的なファイル名マッチ
        if link_target in self.existing_files:
            return True
        
        # 大文字小文字を無視した検索
        link_lower = link_target.lower()
        for existing_file in self.existing_files:
            if existing_file.lower() == link_lower:
                return True
        
        # 部分一致検索（末尾一致）
        for existing_file in self.existing_files:
            if existing_file.endswith(link_target) or link_target.endswith(existing_file):
                return True
        
        return False
    
    def generate_report(self) -> Dict:
        """レポート生成"""
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
        """レポートをコンソールに出力"""
        report = self.generate_report()
        
        print("\n" + "="*60)
        print("📊 OBSIDIAN リンク切れチェック結果")
        print("="*60)
        
        summary = report['summary']
        print(f"📁 総ファイル数: {summary['total_files']}")
        print(f"🔗 総リンク数: {summary['total_links']}")
        print(f"❌ リンク切れ数: {summary['broken_links']}")
        print(f"✅ 成功率: {summary['success_rate']}%")
        
        if self.broken_links:
            print(f"\n💥 リンク切れ詳細 ({len(self.broken_links)}件):")
            print("-" * 60)
            
            # ファイル別にグループ化
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
            print("\n🎉 リンク切れは見つかりませんでした！")
    
    def save_report(self, output_file: str = "link_check_report.json"):
        """レポートをJSONファイルに保存"""
        report = self.generate_report()
        
        output_path = self.vault_path / output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print(f"\n💾 レポートを保存しました: {output_path}")
        return output_path
    
    def get_broken_links_array(self) -> List[str]:
        """リンク切れターゲットのリストを返す"""
        return [link['target'] for link in self.broken_links]
    
    def suggest_fixes(self):
        """修正提案を生成"""
        if not self.broken_links:
            return
        
        print("\n🔧 修正提案:")
        print("-" * 60)
        
        # リンク切れターゲットをユニークにして頻度順にソート
        broken_targets = {}
        for link in self.broken_links:
            target = link['target']
            if target not in broken_targets:
                broken_targets[target] = 0
            broken_targets[target] += 1
        
        sorted_targets = sorted(broken_targets.items(), key=lambda x: x[1], reverse=True)
        
        for target, count in sorted_targets[:10]:  # 上位10件
            print(f"📝 '{target}' (出現{count}回)")
            
            # 類似ファイル名を検索
            similar_files = self.find_similar_files(target)
            if similar_files:
                print(f"   💡 類似ファイル: {', '.join(similar_files[:3])}")
            else:
                print(f"   ➕ 新規作成が必要: {target}.md")
            print()


    def find_similar_files(self, target: str, threshold: float = 0.6) -> List[str]:
        """類似ファイル名を検索（簡易版）"""
        target_lower = target.lower()
        similar = []
        
        for existing_file in self.existing_files:
            existing_lower = existing_file.lower()
            
            # 部分文字列が含まれているかチェック
            if target_lower in existing_lower or existing_lower in target_lower:
                similar.append(existing_file)
        
        return similar

    def get_unique_broken_links(self) -> List[str]:
        """ユニークなリンク切れファイル名のリストを取得（AIエージェント向け）"""
        if not self.broken_links:
            return []
        
        # プレースホルダーを除外したユニークなリンク切れファイル名を取得
        broken_targets = set()
        for link in self.broken_links:
            target = link['target']
            if not self.is_template_placeholder(target):
                broken_targets.add(target)
        
        # 頻度順にソート
        target_counts = {}
        for link in self.broken_links:
            target = link['target']
            if target in broken_targets:
                target_counts[target] = target_counts.get(target, 0) + 1
        
        # 頻度順でソート
        sorted_targets = sorted(target_counts.items(), key=lambda x: x[1], reverse=True)
        return [target for target, count in sorted_targets]
    
    def print_creation_list(self):
        """AIエージェント向けの作成すべきファイルリストを出力"""
        unique_targets = self.get_unique_broken_links()
        
        if not unique_targets:
            print("\n✅ 作成すべきファイルはありません！")
            return
        
        print(f"\n📋 AIエージェント向け：作成すべきファイルリスト ({len(unique_targets)}件)")
        print("=" * 60)
        print("🤖 以下のファイル名について、意味を解釈して適切なディレクトリに作成してください：")
        print("-" * 60)
        
        for i, target in enumerate(unique_targets, 1):
            # 頻度を取得
            count = sum(1 for link in self.broken_links if link['target'] == target)
            print(f"{i:2d}. {target} (参照回数: {count}回)")
        
        print("-" * 60)
        print("📁 推奨配置ディレクトリ:")
        print("   Words/Programming/  - プログラミング関連用語")
        print("   Words/Tools/        - ツール・AI技術関連") 
        print("   Words/Cloud/        - クラウドサービス関連")
        print("   Words/Infrastructure/ - インフラ・サーバー関連")
        print("   Words/Finance/      - 投資・金融関連")
        print("   Words/Authors/      - 人名・著者関連")
        print("   Words/Services/     - サービス・タグ関連")
        print("=" * 60)


def main():
    """
    メイン実行関数 - セッション終了条件判定機能付き
    戻り値: True = セッション終了条件達成（リンク切れ0件）
           False = セッション終了条件未達成（リンク切れ有り）
    """
    import sys
    
    # ワークスペースパスの設定
    if len(sys.argv) > 1:
        vault_path = sys.argv[1]
    else:
        vault_path = "."  # 現在のディレクトリ
    
    print("� OBSIDIAN リンク切れチェッカー")
    print("📋 セッション終了条件: リンク切れ件数 = 0件")
    print(f"📂 対象パス: {os.path.abspath(vault_path)}")
    print("=" * 60)
    
    checker = ObsidianLinkChecker(vault_path)
    
    try:
        # チェック実行
        report = checker.check_all_links()
        
        # 結果表示
        checker.print_report()
        
        # セッション終了条件判定
        broken_count = len(checker.broken_links)
        
        print("\n" + "=" * 60)
        print("🎯 セッション終了条件判定")
        print("=" * 60)
        
        if broken_count == 0:
            print("✅ セッション終了条件達成！")
            print("🎉 リンク切れ件数: 0件")
            print("✨ ナレッジベースのリンク整合性が完璧です")
            print("=" * 60)
            return True
        else:
            print("⚠️  セッション終了条件未達成")
            print(f"💥 リンク切れ件数: {broken_count}件")
            print("\n📝 次のステップ:")
            print("   1. 下記のリンク切れファイルをAIエージェントが作成")
            print("   2. 作成後、再度このスクリプトを実行")
            print("   3. リンク切れ0件でセッション完了")
            
        # レポート保存
        checker.save_report()
        
        # AIエージェント向けファイル作成リスト表示
        if broken_count > 0:
            checker.print_creation_list()
        
        # 詳細修正提案
        checker.suggest_fixes()
        
        print("\n" + "=" * 60)
        print("🤖 AIエージェント向け情報:")
        print(f"   作成すべきファイル数: {broken_count}件")
        print("   詳細は上記の修正提案を参照してください")
        print("=" * 60)
        
        return False
        
    except KeyboardInterrupt:
        print("\n⏹️  処理が中断されました")
        return False
    except Exception as e:
        print(f"\n❌ エラーが発生しました: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    main()
