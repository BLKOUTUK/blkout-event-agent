#!/usr/bin/env python3
"""
Test script to validate the repository reorganization.
"""

import os
import json
import sys
from pathlib import Path

def check_directory_exists(directory):
    """Check if a directory exists."""
    if os.path.isdir(directory):
        print(f"✅ Directory exists: {directory}")
        return True
    else:
        print(f"❌ Directory does not exist: {directory}")
        return False

def check_file_exists(file_path):
    """Check if a file exists."""
    if os.path.isfile(file_path):
        print(f"✅ File exists: {file_path}")
        return True
    else:
        print(f"❌ File does not exist: {file_path}")
        return False

def check_json_valid(file_path):
    """Check if a JSON file is valid."""
    try:
        with open(file_path, 'r') as f:
            json.load(f)
        print(f"✅ JSON is valid: {file_path}")
        return True
    except json.JSONDecodeError as e:
        print(f"❌ JSON is invalid: {file_path} - {str(e)}")
        return False
    except Exception as e:
        print(f"❌ Error reading file: {file_path} - {str(e)}")
        return False

def main():
    """Main function to run tests."""
    print("Testing repository reorganization...")
    
    # Check directories
    directories = [
        "bqm-members",
        "events-system",
        "network-recognition",
        "social-media",
        "shared",
        "mcp-server"
    ]
    
    dir_results = [check_directory_exists(d) for d in directories]
    
    # Check key files
    files = [
        "bqm-members/README.md",
        "bqm-members/bqm_member_management_workflow.json",
        "network-recognition/README.md",
        "network-recognition/point-system/network_contribution_schema.json",
        "README.md",
        "DIRECTORY_STRUCTURE_CHANGES.md",
        "PROJECT_OUTCOMES.md",
        "MIGRATION_PLAN.md"
    ]
    
    file_results = [check_file_exists(f) for f in files]
    
    # Check JSON validity
    json_files = [
        "bqm-members/bqm_member_management_workflow.json",
        "network-recognition/point-system/network_contribution_schema.json"
    ]
    
    json_results = [check_json_valid(f) for f in json_files]
    
    # Print summary
    print("\nTest Summary:")
    print(f"Directories: {sum(dir_results)}/{len(dir_results)} passed")
    print(f"Files: {sum(file_results)}/{len(file_results)} passed")
    print(f"JSON Validation: {sum(json_results)}/{len(json_results)} passed")
    
    total_passed = sum(dir_results) + sum(file_results) + sum(json_results)
    total_tests = len(dir_results) + len(file_results) + len(json_results)
    
    print(f"\nOverall: {total_passed}/{total_tests} tests passed")
    
    if total_passed == total_tests:
        print("\n✅ All tests passed! The repository reorganization is valid.")
        return 0
    else:
        print("\n❌ Some tests failed. Please check the output above for details.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
