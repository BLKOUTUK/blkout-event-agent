#!/usr/bin/env python3
"""
Test script to validate the Network Recognition system.
"""

import os
import json
import sys
from pathlib import Path

def validate_schema_json(file_path):
    """Validate the schema JSON file."""
    try:
        with open(file_path, 'r') as f:
            schema = json.load(f)
        
        # Check for required fields
        required_fields = ['networkContributions', 'collaborativeAchievements', 'pendingContributions']
        for field in required_fields:
            if field not in schema:
                print(f"❌ Missing required field: {field}")
                return False
        
        # Check for network-specific content
        network_references = 0
        for field in schema:
            if 'network' in field.lower() or 'contribution' in field.lower() or 'collaborative' in field.lower():
                network_references += 1
        
        if network_references == 0:
            print("❌ No network references found in schema")
            return False
        
        # Check for BQM impact fields
        bqm_impact_fields = 0
        for field in schema:
            if isinstance(schema[field], dict):
                for subfield in schema[field]:
                    if 'bqm' in subfield.lower() and 'impact' in subfield.lower():
                        bqm_impact_fields += 1
        
        if bqm_impact_fields == 0:
            print("❌ No BQM impact fields found in schema")
            return False
        
        print(f"✅ Schema JSON is valid: {file_path}")
        print(f"✅ Found {network_references} network references in the schema")
        print(f"✅ Found {bqm_impact_fields} BQM impact fields in the schema")
        return True
    
    except json.JSONDecodeError as e:
        print(f"❌ JSON is invalid: {file_path} - {str(e)}")
        return False
    except Exception as e:
        print(f"❌ Error reading file: {file_path} - {str(e)}")
        return False

def check_directory_structure(directory):
    """Check for the expected directory structure."""
    expected_dirs = [
        os.path.join(directory, 'point-system'),
        os.path.join(directory, 'achievement-tracking'),
        os.path.join(directory, 'redemption'),
        os.path.join(directory, 'recognition'),
        os.path.join(directory, 'reporting')
    ]
    
    missing_dirs = [d for d in expected_dirs if not os.path.exists(d)]
    
    if missing_dirs:
        print("❌ Missing expected directories:")
        for d in missing_dirs:
            print(f"  - {d}")
        return False
    
    print("✅ All expected directories exist:")
    for d in expected_dirs:
        print(f"  - {d}")
    
    return True

def main():
    """Main function to run tests."""
    print("Testing Network Recognition system...")
    
    # Check schema file
    schema_path = "network-recognition/point-system/network_contribution_schema.json"
    schema_valid = validate_schema_json(schema_path)
    
    # Check directory structure
    structure_valid = check_directory_structure("network-recognition")
    
    # Print summary
    print("\nTest Summary:")
    print(f"Schema Validation: {'Passed' if schema_valid else 'Failed'}")
    print(f"Directory Structure: {'Passed' if structure_valid else 'Failed'}")
    
    if schema_valid and structure_valid:
        print("\n✅ All tests passed! The Network Recognition system is valid.")
        print("\nNext steps:")
        print("1. Create sample network contribution data")
        print("2. Test the contribution tracking functionality")
        print("3. Test the collaborative achievement recognition")
        return 0
    else:
        print("\n❌ Some tests failed. Please check the output above for details.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
