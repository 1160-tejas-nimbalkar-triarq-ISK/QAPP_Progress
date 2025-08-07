#!/usr/bin/env python3
"""Cache Manager - Clean existing cache and prevent future cache creation"""

import os
import shutil
import platform
from pathlib import Path

def set_no_cache_env():
    """Set environment variable to prevent Python cache creation"""
    os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
    
    try:
        if platform.system() == "Windows":
            os.system('setx PYTHONDONTWRITEBYTECODE 1 >nul 2>&1')
            print("✅ Cache prevention enabled (restart terminal)")
        else:
            # For Unix systems, suggest manual addition to shell profile
            print("💡 Add 'export PYTHONDONTWRITEBYTECODE=1' to your shell profile")
    except:
        print("⚠️  Manual environment setup may be needed")

def clean_cache():
    """Remove all Python cache files and unwanted generated files"""
    removed = {'dirs': 0, 'files': 0, 'temp': 0}
    
    # Unwanted files to remove
    unwanted_files = ["pretty.output", "config.env"]
    
    for item in Path.cwd().rglob("*"):
        try:
            if item.name == "__pycache__" and item.is_dir():
                shutil.rmtree(item)
                removed['dirs'] += 1
            elif item.suffix == ".pyc":
                item.unlink()
                removed['files'] += 1
            elif item.name in unwanted_files and item.is_file():
                item.unlink()
                removed['temp'] += 1
        except:
            pass
    
    return removed

if __name__ == "__main__":
    print("🚀 Cache Manager")
    print("-" * 30)
    
    # Set environment variable
    set_no_cache_env()
    
    # Clean existing cache
    counts = clean_cache()
    print(f"🧹 Cleaned {counts['dirs']} cache dirs, {counts['files']} .pyc files, {counts['temp']} temp files")
    print("✨ Done!") 