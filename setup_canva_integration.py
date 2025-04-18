"""
Setup script for Canva integration with BLKOUT NEXT Campaign
This script helps set up the necessary environment variables and configuration for Canva integration.
"""
import os
import json
import argparse
from dotenv import load_dotenv, set_key

def setup_canva_integration(api_key=None, brand_kit_id=None):
    """
    Set up Canva integration by adding environment variables to .env file
    
    Args:
        api_key: Canva API key
        brand_kit_id: Canva Brand Kit ID
    """
    # Load existing .env file
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(env_path)
    
    # Get API key from user if not provided
    if not api_key:
        api_key = input("Enter your Canva API key: ")
    
    # Get Brand Kit ID from user if not provided
    if not brand_kit_id:
        brand_kit_id = input("Enter your Canva Brand Kit ID (leave blank if not available): ")
    
    # Update .env file
    set_key(env_path, "CANVA_API_KEY", api_key)
    if brand_kit_id:
        set_key(env_path, "CANVA_BRAND_KIT_ID", brand_kit_id)
    
    print("Canva integration environment variables added to .env file")
    
    # Create directory for Canva MCP server if it doesn't exist
    canva_dir = os.path.join(os.path.dirname(__file__), 'mcp-server', 'integration-server', 'canva')
    os.makedirs(canva_dir, exist_ok=True)
    
    print("Canva MCP server directory created")
    
    # Update settings.json to include Canva MCP server
    vscode_dir = os.path.join(os.path.dirname(__file__), '.vscode')
    settings_path = os.path.join(vscode_dir, 'settings.json')
    
    if os.path.exists(settings_path):
        with open(settings_path, 'r') as f:
            settings = json.load(f)
        
        # Add Canva MCP server to settings
        if 'mcp' not in settings:
            settings['mcp'] = {}
        
        if 'servers' not in settings['mcp']:
            settings['mcp']['servers'] = {}
        
        settings['mcp']['servers']['canva-mcp-server'] = {
            "command": "python",
            "args": [
                "-m",
                "mcp-server.integration-server.canva.canva_mcp_server"
            ],
            "env": {
                "CANVA_API_KEY": "${env:CANVA_API_KEY}",
                "CANVA_BRAND_KIT_ID": "${env:CANVA_BRAND_KIT_ID}"
            }
        }
        
        with open(settings_path, 'w') as f:
            json.dump(settings, f, indent=4)
        
        print("Updated VS Code settings.json with Canva MCP server configuration")
    
    print("\nCanva integration setup complete!")
    print("\nTo use the Canva integration:")
    print("1. Start the Canva MCP server")
    print("2. Use the Canva MCP tools in your workflows")
    print("3. Access the Canva API through the provided functions")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Set up Canva integration for BLKOUT NEXT Campaign")
    parser.add_argument("--api-key", help="Canva API key")
    parser.add_argument("--brand-kit-id", help="Canva Brand Kit ID")
    
    args = parser.parse_args()
    
    setup_canva_integration(args.api_key, args.brand_kit_id)
