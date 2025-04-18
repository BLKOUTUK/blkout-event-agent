import requests
import json
import time

# Configuration
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MzZjNTEyZC1lYmM3LTRiYzYtYWM5MS0zMzI3ZDgzY2UwMjMiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzQzNzg1NTY0LCJleHAiOjE3NTE1MTUyMDB9.ZWbR5bp1jtaB7yfxn-kg4ASNHgXuRIe5QKv5O9ccUJI"
HOST_URL = "http://localhost:5678/api/v1"

# Headers for API requests
headers = {
    "X-N8N-API-KEY": API_KEY,
    "Content-Type": "application/json"
}

def create_direct_append_workflow():
    """Create a workflow that directly appends a single row to the Google Sheet."""
    
    # Define the workflow
    workflow = {
        "name": "Direct Sheet Append Test",
        "nodes": [
            {
                "parameters": {
                    "rule": {
                        "interval": [
                            {
                                "field": "seconds",
                                "secondsInterval": 10
                            }
                        ]
                    }
                },
                "name": "Schedule Trigger",
                "type": "n8n-nodes-base.scheduleTrigger",
                "typeVersion": 1,
                "position": [0, 0]
            },
            {
                "parameters": {
                    "jsCode": """// Create a simple test object with the current timestamp
return {
  json: {
    Email: "direct.append." + Date.now() + "@example.com",
    FirstName: "Direct",
    LastName: "Append",
    Role: "Test",
    Organisation: "Test Org",
    Status: "Active",
    DateAdded: new Date().toISOString().split('T')[0],
    LastEmailSent: "",
    EmailHistory: "[]",
    OptOut: false,
    Source: "Direct Test " + new Date().toISOString()
  }
};"""
                },
                "name": "Create Test Data",
                "type": "n8n-nodes-base.code",
                "typeVersion": 1,
                "position": [220, 0]
            },
            {
                "parameters": {
                    "resource": "spreadsheet",
                    "operation": "append",
                    "documentId": "1EDTTmhBGiZdhKuLwCQLDduRuIE2oQmXfeJvoiowU4bs",
                    "sheetName": "Welcome",
                    "options": {
                        "valueInputMode": "RAW"
                    }
                },
                "name": "Google Sheets",
                "type": "n8n-nodes-base.googleSheets",
                "typeVersion": 4,
                "position": [440, 0],
                "credentials": {
                    "googleSheetsOAuth2Api": {
                        "id": "NzGLdLkWxHz8wqeq",
                        "name": "Google Sheets account"
                    }
                }
            }
        ],
        "connections": {
            "Schedule Trigger": {
                "main": [
                    [
                        {
                            "node": "Create Test Data",
                            "type": "main",
                            "index": 0
                        }
                    ]
                ]
            },
            "Create Test Data": {
                "main": [
                    [
                        {
                            "node": "Google Sheets",
                            "type": "main",
                            "index": 0
                        }
                    ]
                ]
            }
        },
        "settings": {
            "executionOrder": "v1"
        }
    }
    
    # Create the workflow
    try:
        response = requests.post(
            f"{HOST_URL}/workflows",
            headers=headers,
            json=workflow
        )
        response.raise_for_status()
        workflow_id = response.json()["id"]
        
        print(f"Created workflow with ID: {workflow_id}")
        
        # Activate the workflow
        activate_response = requests.post(
            f"{HOST_URL}/workflows/{workflow_id}/activate",
            headers=headers
        )
        activate_response.raise_for_status()
        
        print(f"Activated workflow with ID: {workflow_id}")
        print(f"The workflow will run every 10 seconds and add test data to the Google Sheet.")
        print(f"Check the Google Sheet in about 10-20 seconds to see if the test data was added.")
        
        return workflow_id
    except Exception as e:
        print(f"Error creating workflow: {str(e)}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response: {e.response.text}")
        return None

def execute_workflow_manually(workflow_id):
    """Execute the workflow manually."""
    try:
        response = requests.post(
            f"{HOST_URL}/workflows/{workflow_id}/execute",
            headers=headers
        )
        response.raise_for_status()
        execution_id = response.json()["executionId"]
        
        print(f"Manually executed workflow with execution ID: {execution_id}")
        
        # Wait for the execution to complete
        time.sleep(5)
        
        # Check the execution status
        execution_response = requests.get(
            f"{HOST_URL}/executions/{execution_id}",
            headers=headers
        )
        execution_response.raise_for_status()
        execution = execution_response.json()
        
        if execution["status"] == "success":
            print("Execution completed successfully!")
        else:
            print(f"Execution failed with status: {execution['status']}")
            if "error" in execution:
                print(f"Error: {execution['error']['message']}")
        
        return execution
    except Exception as e:
        print(f"Error executing workflow: {str(e)}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response: {e.response.text}")
        return None

if __name__ == "__main__":
    workflow_id = create_direct_append_workflow()
    
    if workflow_id:
        print("\nWaiting for the scheduled execution...")
        time.sleep(15)
        
        print("\nExecuting the workflow manually...")
        execution = execute_workflow_manually(workflow_id)
        
        print("\nWaiting for another scheduled execution...")
        time.sleep(15)
        
        # Deactivate the workflow
        try:
            deactivate_response = requests.post(
                f"{HOST_URL}/workflows/{workflow_id}/deactivate",
                headers=headers
            )
            deactivate_response.raise_for_status()
            
            print(f"Deactivated workflow with ID: {workflow_id}")
        except Exception as e:
            print(f"Error deactivating workflow: {str(e)}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response: {e.response.text}")
