#!/usr/bin/env python3
"""
Test script to validate the basic structure without external dependencies.
"""

import sys
import os
from pathlib import Path

# Add modules directory to path
sys.path.insert(0, 'modules')

def test_directory_structure():
    """Test that all required directories exist"""
    print("Testing directory structure...")
    
    required_dirs = [
        'images/uploads',
        'images/analyzed',
        'images/archive',
        'data',
        'docs',
        'modules',
    ]
    
    all_exist = True
    for directory in required_dirs:
        exists = Path(directory).is_dir()
        status = "✓" if exists else "✗"
        print(f"  {status} {directory}")
        if not exists:
            all_exist = False
    
    return all_exist

def test_files_exist():
    """Test that all required files exist"""
    print("\nTesting required files...")
    
    required_files = [
        'assistant.py',
        'config.yaml',
        'requirements.txt',
        'README.md',
        'ROADMAP.md',
        'LICENSE',
        'CONTRIBUTING.md',
        'setup.sh',
        '.gitignore',
        'modules/__init__.py',
        'modules/image_analyzer.py',
        'modules/data_evaluator.py',
        'modules/post_generator.py',
        'modules/config_manager.py',
    ]
    
    all_exist = True
    for file_path in required_files:
        exists = Path(file_path).is_file()
        status = "✓" if exists else "✗"
        print(f"  {status} {file_path}")
        if not exists:
            all_exist = False
    
    return all_exist

def test_python_syntax():
    """Test Python files for syntax errors"""
    print("\nTesting Python syntax...")
    
    python_files = [
        'assistant.py',
        'modules/__init__.py',
        'modules/image_analyzer.py',
        'modules/data_evaluator.py',
        'modules/post_generator.py',
        'modules/config_manager.py',
    ]
    
    all_valid = True
    for file_path in python_files:
        try:
            with open(file_path, 'r') as f:
                compile(f.read(), file_path, 'exec')
            print(f"  ✓ {file_path}")
        except SyntaxError as e:
            print(f"  ✗ {file_path}: {e}")
            all_valid = False
    
    return all_valid

def test_config_file():
    """Test config file is valid YAML"""
    print("\nTesting configuration file...")
    
    try:
        # Try to import yaml
        try:
            import yaml
            with open('config.yaml', 'r') as f:
                config = yaml.safe_load(f)
            print(f"  ✓ config.yaml is valid YAML")
            return True
        except ImportError:
            print(f"  ⚠ PyYAML not installed, skipping YAML validation")
            # Just check file exists
            if Path('config.yaml').is_file():
                print(f"  ✓ config.yaml exists")
                return True
            return False
    except Exception as e:
        print(f"  ✗ config.yaml: {e}")
        return False

def test_documentation():
    """Test that documentation files are not empty"""
    print("\nTesting documentation...")
    
    doc_files = [
        'README.md',
        'ROADMAP.md',
        'docs/QUICKSTART.md',
        'docs/USAGE.md',
    ]
    
    all_good = True
    for file_path in doc_files:
        if Path(file_path).is_file():
            size = Path(file_path).stat().st_size
            if size > 100:  # At least 100 bytes
                print(f"  ✓ {file_path} ({size} bytes)")
            else:
                print(f"  ✗ {file_path} is too small ({size} bytes)")
                all_good = False
        else:
            print(f"  ✗ {file_path} not found")
            all_good = False
    
    return all_good

def main():
    """Run all tests"""
    print("=" * 60)
    print("Grow Documentation Assistant - Structure Validation")
    print("=" * 60)
    print()
    
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    tests = [
        ("Directory Structure", test_directory_structure),
        ("Required Files", test_files_exist),
        ("Python Syntax", test_python_syntax),
        ("Configuration", test_config_file),
        ("Documentation", test_documentation),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n  Error running test: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    for test_name, result in results:
        status = "PASSED" if result else "FAILED"
        emoji = "✓" if result else "✗"
        print(f"{emoji} {test_name}: {status}")
    
    all_passed = all(result for _, result in results)
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✓ All tests passed!")
        print("=" * 60)
        return 0
    else:
        print("✗ Some tests failed")
        print("=" * 60)
        return 1

if __name__ == '__main__':
    sys.exit(main())
