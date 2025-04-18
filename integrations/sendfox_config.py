"""
SendFox API Integration for BLKOUT NEXT Campaign
This module handles the connection to SendFox for email campaign management.
"""
import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class SendFoxAPI:
    """SendFox API client for managing email campaigns"""
    
    BASE_URL = "https://api.sendfox.com/v1"
    
    def __init__(self):
        """Initialize the SendFox API client with API key from environment variables"""
        self.api_key = os.getenv("SENDFOX_API_KEY")
        if not self.api_key:
            raise ValueError("SendFox API key not found in environment variables")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def get_lists(self):
        """Get all lists from SendFox"""
        endpoint = f"{self.BASE_URL}/lists"
        response = requests.get(endpoint, headers=self.headers)
        return self._handle_response(response)
    
    def create_list(self, name, description=None):
        """Create a new list in SendFox"""
        endpoint = f"{self.BASE_URL}/lists"
        payload = {
            "name": name
        }
        if description:
            payload["description"] = description
        
        response = requests.post(endpoint, headers=self.headers, json=payload)
        return self._handle_response(response)
    
    def add_contact(self, email, first_name=None, last_name=None, lists=None):
        """Add a contact to SendFox and optionally to specific lists"""
        endpoint = f"{self.BASE_URL}/contacts"
        payload = {
            "email": email
        }
        
        if first_name:
            payload["first_name"] = first_name
        if last_name:
            payload["last_name"] = last_name
        if lists:
            payload["lists"] = lists if isinstance(lists, list) else [lists]
        
        response = requests.post(endpoint, headers=self.headers, json=payload)
        return self._handle_response(response)
    
    def get_contacts(self, page=1):
        """Get contacts from SendFox"""
        endpoint = f"{self.BASE_URL}/contacts?page={page}"
        response = requests.get(endpoint, headers=self.headers)
        return self._handle_response(response)
    
    def create_campaign(self, name, subject, email_html, list_ids):
        """Create a new email campaign"""
        endpoint = f"{self.BASE_URL}/campaigns"
        payload = {
            "name": name,
            "subject": subject,
            "email_html": email_html,
            "lists": list_ids if isinstance(list_ids, list) else [list_ids]
        }
        
        response = requests.post(endpoint, headers=self.headers, json=payload)
        return self._handle_response(response)
    
    def _handle_response(self, response):
        """Handle API response and errors"""
        if response.status_code in (200, 201):
            return response.json()
        else:
            error_msg = f"Error {response.status_code}: {response.text}"
            print(error_msg)
            return {"error": error_msg}

# Example usage
if __name__ == "__main__":
    # Test the API connection
    try:
        sendfox = SendFoxAPI()
        lists = sendfox.get_lists()
        print(f"Successfully connected to SendFox API. Found {len(lists.get('data', []))} lists.")
    except Exception as e:
        print(f"Failed to connect to SendFox API: {str(e)}")
