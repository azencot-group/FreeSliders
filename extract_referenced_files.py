#!/usr/bin/env python3
"""
Extract all file references from index.html and create a .gitignore for unreferenced files.
"""

import re
import os
import json
from pathlib import Path

def extract_file_references(html_file):
    """Extract all website_outputs file references from HTML file."""
    with open(html_file, 'r') as f:
        content = f.read()
    
    # Find all website_outputs references
    pattern = r'[\'"]website_outputs/([^\'\"]+)[\'"]'
    matches = re.findall(pattern, content)
    
    # Also check for audio manifest references
    if 'website_outputs/audio_manifest.json' in content:
        matches.append('audio_manifest.json')
    
    # Clean up and deduplicate
    referenced_files = set()
    for match in matches:
        # Clean up any trailing characters
        clean_path = match.strip()
        referenced_files.add(f"website_outputs/{clean_path}")
    
    return sorted(referenced_files)

def get_all_files_in_website_outputs():
    """Get all files in the website_outputs directory."""
    all_files = set()
    website_outputs = Path("website_outputs")
    
    if website_outputs.exists():
        for file_path in website_outputs.rglob("*"):
            if file_path.is_file():
                all_files.add(str(file_path))
    
    return sorted(all_files)

def check_file_existence(referenced_files):
    """Check which referenced files actually exist."""
    existing = []
    missing = []
    
    for file_path in referenced_files:
        if os.path.exists(file_path):
            existing.append(file_path)
        else:
            missing.append(file_path)
    
    return existing, missing

def create_gitignore(referenced_files, all_files):
    """Create .gitignore entries for unreferenced files."""
    referenced_set = set(referenced_files)
    all_files_set = set(all_files)
    
    # Find unreferenced files
    unreferenced = all_files_set - referenced_set
    
    # Group by directory for cleaner .gitignore
    gitignore_entries = []
    
    # Add unreferenced files to .gitignore
    for file_path in sorted(unreferenced):
        # Convert to relative path from project root
        relative_path = file_path
        gitignore_entries.append(relative_path)
    
    return gitignore_entries, unreferenced

def main():
    print("🔍 Analyzing file references in index.html...")
    
    # Extract referenced files
    referenced_files = extract_file_references("index.html")
    
    print(f"📁 Found {len(referenced_files)} referenced files:")
    for file_path in referenced_files:
        print(f"  - {file_path}")
    
    # Check which files exist
    existing_files, missing_files = check_file_existence(referenced_files)
    
    print(f"\n✅ {len(existing_files)} referenced files exist")
    if missing_files:
        print(f"❌ {len(missing_files)} referenced files are missing:")
        for file_path in missing_files:
            print(f"  - {file_path}")
    
    # Get all files in website_outputs
    all_files = get_all_files_in_website_outputs()
    print(f"\n📂 Total files in website_outputs: {len(all_files)}")
    
    # Create .gitignore entries
    gitignore_entries, unreferenced_files = create_gitignore(existing_files, all_files)
    
    print(f"\n🗑️  {len(unreferenced_files)} unreferenced files found:")
    for file_path in sorted(unreferenced_files):
        print(f"  - {file_path}")
    
    # Read existing .gitignore
    gitignore_path = ".gitignore"
    existing_gitignore = []
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as f:
            existing_gitignore = f.read().splitlines()
    
    # Add new entries to .gitignore
    new_entries = []
    for entry in gitignore_entries:
        if entry not in existing_gitignore:
            new_entries.append(entry)
    
    if new_entries:
        print(f"\n📝 Adding {len(new_entries)} entries to .gitignore:")
        
        with open(gitignore_path, 'a') as f:
            if existing_gitignore and not existing_gitignore[-1].strip():
                pass  # Don't add extra newline
            else:
                f.write('\n')
            f.write("# Unreferenced website output files\n")
            for entry in new_entries:
                f.write(f"{entry}\n")
                print(f"  + {entry}")
        print(f"✅ Updated .gitignore")
    else:
        print("✅ No new .gitignore entries needed")
    
    # Create a summary file
    summary = {
        "referenced_files": existing_files,
        "missing_files": missing_files,
        "unreferenced_files": sorted(unreferenced_files),
        "total_files": len(all_files),
        "referenced_count": len(existing_files),
        "missing_count": len(missing_files),
        "unreferenced_count": len(unreferenced_files)
    }
    
    with open("file_analysis.json", 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"\n📊 Summary saved to file_analysis.json")
    print(f"✅ Analysis complete!")

if __name__ == "__main__":
    main()
