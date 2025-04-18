#!/usr/bin/env python3
"""
Test script to validate the BQM Member Management workflow.
"""

import os
import json
import sys
from pathlib import Path

def validate_workflow_json(file_path):
    """Validate the workflow JSON file."""
    try:
        with open(file_path, 'r') as f:
            workflow = json.load(f)

        # Check for required fields
        required_fields = ['name', 'nodes', 'connections']
        for field in required_fields:
            if field not in workflow:
                print(f"❌ Missing required field: {field}")
                return False

        # Check workflow name
        if workflow['name'] != "BLKOUT BQM Member Management":
            print(f"❌ Incorrect workflow name: {workflow['name']}")
            return False

        # Check for BQM-specific content
        bqm_references = 0
        for node in workflow['nodes']:
            if 'parameters' in node and 'functionCode' in node['parameters']:
                if 'BQM' in node['parameters']['functionCode']:
                    bqm_references += 1
            if 'name' in node and 'BQM' in node['name']:
                bqm_references += 1

        if bqm_references == 0:
            print("❌ No BQM references found in workflow")
            return False

        print(f"✅ Workflow JSON is valid: {file_path}")
        print(f"✅ Found {bqm_references} BQM references in the workflow")
        return True

    except json.JSONDecodeError as e:
        print(f"❌ JSON is invalid: {file_path} - {str(e)}")
        return False
    except Exception as e:
        print(f"❌ Error reading file: {file_path} - {str(e)}")
        return False

def check_email_templates(directory):
    """Check for email templates in the directory."""
    email_templates = []
    template_dir = os.path.join(directory, 'engagement', 'email-templates')
    if os.path.exists(template_dir):
        for file in os.listdir(template_dir):
            if file.endswith('.html'):
                email_templates.append(os.path.join(template_dir, file))
    else:
        # Fallback to searching the entire directory
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.html') and 'email' in file.lower():
                    email_templates.append(os.path.join(root, file))

    if not email_templates:
        print(f"❌ No email templates found in {directory}")
        return False

    print(f"✅ Found {len(email_templates)} email templates:")
    for template in email_templates:
        print(f"  - {template}")

    return True

def main():
    """Main function to run tests."""
    print("Testing BQM Member Management workflow...")

    # Check workflow file
    workflow_path = "bqm-members/bqm_member_management_workflow.json"
    workflow_valid = validate_workflow_json(workflow_path)

    # Check email templates
    templates_valid = check_email_templates("bqm-members")

    # Print summary
    print("\nTest Summary:")
    print(f"Workflow Validation: {'Passed' if workflow_valid else 'Failed'}")
    print(f"Email Templates: {'Passed' if templates_valid else 'Failed'}")

    if workflow_valid and templates_valid:
        print("\n✅ All tests passed! The BQM Member Management workflow is valid.")
        print("\nNext steps:")
        print("1. Open n8n in your browser (http://localhost:5678)")
        print("2. Import the workflow from bqm-members/bqm_member_management_workflow.json")
        print("3. Test the workflow with sample data")
        return 0
    else:
        print("\n❌ Some tests failed. Please check the output above for details.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
