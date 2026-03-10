#!/usr/bin/env python3
"""
Script to count files and lines in bug_snippets and bug_fixes directories
"""

import os
from pathlib import Path

def count_lines(file_path):
    """Count the number of lines in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return len(f.readlines())
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0

def main():
    base_path = Path(__file__).parent
    
    # Define directories to check
    directories = [
        base_path / 'bug_snippets',
        base_path / 'bug_fixes'
    ]
    
    # File extensions to check
    valid_extensions = {'.py', '.c', '.cpp', '.java', '.js', '.php'}
    
    total_files = 0
    files_info = []
    
    print("=" * 60)
    print("FILE AND LINE COUNT REPORT")
    print("=" * 60)
    
    for directory in directories:
        if not directory.exists():
            print(f"Warning: Directory {directory} does not exist")
            continue
        
        print(f"\n📁 Directory: {directory.name}/")
        print("-" * 60)
        
        dir_files = []
        for file_path in sorted(directory.iterdir()):
            if file_path.is_file() and file_path.suffix in valid_extensions:
                line_count = count_lines(file_path)
                dir_files.append((file_path.name, line_count))
                files_info.append((file_path.name, line_count))
                total_files += 1
        
        if dir_files:
            for filename, lines in dir_files:
                print(f"  {filename:<25} {lines:>5} lines")
        else:
            print("  No source files found")
    
    print("\n" + "=" * 60)
    print(f"Total Files: {total_files}")
    total_lines = sum(count for _, count in files_info)
    print(f"Total Lines: {total_lines}")
    print("=" * 60)
    
    # Print summary by file
    print("\nSUMMARY:")
    for filename, lines in files_info:
        print(f"  {filename}: {lines} lines")

if __name__ == '__main__':
    main()
