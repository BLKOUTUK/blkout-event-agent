"""
Canva MCP Server for BLKOUT NEXT Campaign
This module provides MCP server integration with Canva for design creation and management.
"""
import os
import json
import base64
import requests
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any, Union

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CanvaMCPServer:
    """MCP Server for Canva integration"""
    
    BASE_URL = "https://api.canva.com/v1"
    
    def __init__(self):
        """Initialize the Canva MCP Server with API credentials"""
        self.api_key = os.getenv("CANVA_API_KEY")
        self.brand_kit_id = os.getenv("CANVA_BRAND_KIT_ID")
        
        if not self.api_key:
            logger.error("Canva API key not found in environment variables")
            raise ValueError("Canva API key not found in environment variables")
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        # BLKOUT NEXT brand colors
        self.brand_colors = {
            "primary": "#000000",  # Black
            "secondary": "#2D1A45",  # Deep Purple
            "accent": "#39FF14",  # Electric Green
            "supporting": "#F2F2F2"  # Light Gray
        }
        
        # BLKOUT NEXT brand fonts
        self.brand_fonts = {
            "headings": "Montserrat Bold",
            "subheadings": "Montserrat Medium",
            "body": "Open Sans Regular",
            "accent": "Open Sans Italic"
        }
        
        logger.info("Canva MCP Server initialized")
    
    def create_design(self, design_type: str, title: str, template_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new design in Canva
        
        Args:
            design_type: Type of design (social_media_post, presentation, etc.)
            title: Title of the design
            template_id: Optional template ID to use as a starting point
            
        Returns:
            Dict containing design details including design_id
        """
        endpoint = f"{self.BASE_URL}/designs"
        
        payload = {
            "type": design_type,
            "title": title
        }
        
        if template_id:
            payload["template_id"] = template_id
        
        try:
            response = requests.post(endpoint, headers=self.headers, json=payload)
            response.raise_for_status()
            
            design_data = response.json()
            logger.info(f"Created new Canva design: {title}")
            
            return {
                "success": True,
                "design_id": design_data.get("id"),
                "edit_url": design_data.get("edit_url"),
                "title": title,
                "created_at": datetime.now().isoformat()
            }
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error creating Canva design: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def list_templates(self, category: Optional[str] = None, limit: int = 20) -> Dict[str, Any]:
        """
        List available Canva templates
        
        Args:
            category: Optional category to filter templates
            limit: Maximum number of templates to return
            
        Returns:
            Dict containing list of templates
        """
        endpoint = f"{self.BASE_URL}/templates"
        
        params = {
            "limit": limit
        }
        
        if category:
            params["category"] = category
        
        try:
            response = requests.get(endpoint, headers=self.headers, params=params)
            response.raise_for_status()
            
            templates_data = response.json()
            
            return {
                "success": True,
                "templates": templates_data.get("templates", []),
                "total": templates_data.get("total", 0)
            }
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error listing Canva templates: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def apply_brand_kit(self, design_id: str) -> Dict[str, Any]:
        """
        Apply BLKOUT NEXT brand kit to a design
        
        Args:
            design_id: ID of the design to apply brand kit to
            
        Returns:
            Dict containing result of operation
        """
        endpoint = f"{self.BASE_URL}/designs/{design_id}/brand"
        
        payload = {
            "brand_kit_id": self.brand_kit_id if self.brand_kit_id else None,
            "colors": self.brand_colors,
            "fonts": self.brand_fonts
        }
        
        try:
            response = requests.post(endpoint, headers=self.headers, json=payload)
            response.raise_for_status()
            
            logger.info(f"Applied brand kit to design: {design_id}")
            
            return {
                "success": True,
                "design_id": design_id,
                "message": "Brand kit applied successfully"
            }
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error applying brand kit: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def generate_social_post(self, 
                           platform: str, 
                           content_type: str, 
                           title: str, 
                           description: str,
                           template_category: Optional[str] = None) -> Dict[str, Any]:
        """
        Generate a social media post using Canva templates and BLKOUT NEXT branding
        
        Args:
            platform: Social media platform (instagram, facebook, twitter)
            content_type: Type of content (announcement, concept_explanation, etc.)
            title: Title/headline of the post
            description: Description/body text of the post
            template_category: Optional template category to use
            
        Returns:
            Dict containing generated design details
        """
        # Map platform to design type
        platform_design_types = {
            "instagram": "social_media_post",
            "facebook": "social_media_post",
            "twitter": "social_media_post"
        }
        
        design_type = platform_design_types.get(platform.lower(), "social_media_post")
        
        # Find appropriate template based on content type
        template_id = None
        if template_category:
            templates = self.list_templates(category=template_category, limit=5)
            if templates.get("success") and templates.get("templates"):
                template_id = templates["templates"][0]["id"]
        
        # Create the design
        design_result = self.create_design(
            design_type=design_type,
            title=f"BLKOUT NEXT - {content_type.title()} - {title}",
            template_id=template_id
        )
        
        if not design_result.get("success"):
            return design_result
        
        # Apply brand kit
        self.apply_brand_kit(design_result["design_id"])
        
        # Add content to the design
        # Note: This is a simplified version as actual content addition would require
        # more complex API calls specific to Canva's document structure
        
        return {
            "success": True,
            "design_id": design_result["design_id"],
            "edit_url": design_result["edit_url"],
            "title": design_result["title"],
            "platform": platform,
            "content_type": content_type,
            "created_at": datetime.now().isoformat(),
            "message": "Social media post design created successfully. Use the edit_url to customize in Canva."
        }
    
    def export_design(self, design_id: str, format: str = "png") -> Dict[str, Any]:
        """
        Export a Canva design as an image or PDF
        
        Args:
            design_id: ID of the design to export
            format: Export format (png, jpg, pdf)
            
        Returns:
            Dict containing export details including download URL
        """
        endpoint = f"{self.BASE_URL}/designs/{design_id}/exports"
        
        payload = {
            "format": format
        }
        
        try:
            response = requests.post(endpoint, headers=self.headers, json=payload)
            response.raise_for_status()
            
            export_data = response.json()
            
            return {
                "success": True,
                "export_id": export_data.get("id"),
                "download_url": export_data.get("download_url"),
                "format": format,
                "expires_at": export_data.get("expires_at")
            }
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error exporting design: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }

# MCP Server handler functions
def create_design(args):
    """MCP handler for create_design"""
    server = CanvaMCPServer()
    return server.create_design(
        design_type=args.get("design_type", "social_media_post"),
        title=args.get("title", "Untitled Design"),
        template_id=args.get("template_id")
    )

def list_templates(args):
    """MCP handler for list_templates"""
    server = CanvaMCPServer()
    return server.list_templates(
        category=args.get("category"),
        limit=args.get("limit", 20)
    )

def apply_brand_kit(args):
    """MCP handler for apply_brand_kit"""
    server = CanvaMCPServer()
    return server.apply_brand_kit(
        design_id=args.get("design_id")
    )

def generate_social_post(args):
    """MCP handler for generate_social_post"""
    server = CanvaMCPServer()
    return server.generate_social_post(
        platform=args.get("platform", "instagram"),
        content_type=args.get("content_type", "announcement"),
        title=args.get("title", "Untitled Post"),
        description=args.get("description", ""),
        template_category=args.get("template_category")
    )

def export_design(args):
    """MCP handler for export_design"""
    server = CanvaMCPServer()
    return server.export_design(
        design_id=args.get("design_id"),
        format=args.get("format", "png")
    )

# Main entry point for MCP server
if __name__ == "__main__":
    # This would be replaced by the MCP server framework code
    print("Canva MCP Server running...")
