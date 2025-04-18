"""
Canva Integration for BLKOUT NEXT Campaign
This module provides integration with Canva for design creation and management.
"""
import os
import json
import requests
import subprocess
from typing import Dict, List, Optional, Any, Union
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class CanvaIntegration:
    """Integration with Canva for design creation and management"""
    
    def __init__(self):
        """Initialize the Canva integration"""
        self.api_key = os.getenv("CANVA_API_KEY")
        self.brand_kit_id = os.getenv("CANVA_BRAND_KIT_ID")
        
        if not self.api_key:
            print("Warning: Canva API key not found in environment variables")
        
        # BLKOUT NEXT brand colors
        self.brand_colors = {
            "primary": "#000000",  # Black
            "secondary": "#2D1A45",  # Deep Purple
            "accent": "#39FF14",  # Electric Green
            "supporting": "#F2F2F2"  # Light Gray
        }
    
    def is_mcp_server_running(self) -> bool:
        """Check if the Canva MCP server is running"""
        # This is a simplified check - in a real implementation, you would
        # check if the server process is actually running
        try:
            result = subprocess.run(
                ["python", "-c", "import importlib.util; print(importlib.util.find_spec('mcp-server.integration-server.canva.canva_mcp_server') is not None)"],
                capture_output=True,
                text=True
            )
            return "True" in result.stdout
        except Exception:
            return False
    
    def start_mcp_server(self) -> bool:
        """Start the Canva MCP server if it's not already running"""
        if self.is_mcp_server_running():
            print("Canva MCP server is already running")
            return True
        
        try:
            # Start the server in a new process
            subprocess.Popen(
                ["python", "-m", "mcp-server.integration-server.canva.canva_mcp_server"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            print("Started Canva MCP server")
            return True
        except Exception as e:
            print(f"Error starting Canva MCP server: {str(e)}")
            return False
    
    def create_design_from_template(self, 
                                  content_type: str, 
                                  title: str, 
                                  description: str,
                                  platform: str = "instagram") -> Dict[str, Any]:
        """
        Create a design from a template based on content type
        
        Args:
            content_type: Type of content (announcement, concept_explanation, etc.)
            title: Title/headline of the post
            description: Description/body text of the post
            platform: Social media platform (instagram, facebook, twitter)
            
        Returns:
            Dict containing design details
        """
        # Map content types to template categories
        template_categories = {
            "announcement": "social_media_announcement",
            "concept_explanation": "educational_carousel",
            "community_question": "social_media_question",
            "historical_context": "biography_post",
            "call_to_action": "call_to_action",
            "community_spotlight": "profile_spotlight",
            "workshop_promotion": "event_promotion",
            "weekly_wrap_up": "weekly_update",
            "behind_the_scenes": "behind_the_scenes",
            "feedback_solicitation": "feedback_request"
        }
        
        template_category = template_categories.get(content_type.lower().replace(" ", "_"), "social_media_post")
        
        # Call the MCP server function
        try:
            # In a real implementation, you would use the MCP client to call the server
            # This is a simplified version that mimics the expected behavior
            
            # Ensure the server is running
            self.start_mcp_server()
            
            # Create a design using the appropriate template
            design_data = {
                "success": True,
                "design_id": f"mock-design-id-{content_type}",
                "edit_url": f"https://canva.com/design/mock-design-id-{content_type}/edit",
                "title": title,
                "platform": platform,
                "content_type": content_type,
                "template_category": template_category,
                "message": "Design created successfully. Use the edit_url to customize in Canva."
            }
            
            return design_data
            
        except Exception as e:
            print(f"Error creating design: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def generate_campaign_designs(self, content_calendar: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Generate designs for all items in the content calendar
        
        Args:
            content_calendar: List of content calendar items
            
        Returns:
            List of design details for each calendar item
        """
        designs = []
        
        for item in content_calendar:
            content_type = item.get("content_type", "").lower().replace(" ", "_")
            title = item.get("title", "Untitled")
            description = item.get("description", "")
            platform = item.get("platform", "instagram").lower()
            
            design = self.create_design_from_template(
                content_type=content_type,
                title=title,
                description=description,
                platform=platform
            )
            
            if design.get("success"):
                # Add design details to the calendar item
                item_with_design = item.copy()
                item_with_design["design_id"] = design.get("design_id")
                item_with_design["design_url"] = design.get("edit_url")
                designs.append(item_with_design)
        
        return designs
    
    def generate_design_prompt(self, content_type: str, platform: str) -> str:
        """
        Generate a design prompt for Canva or other design tools
        
        Args:
            content_type: Type of content
            platform: Social media platform
            
        Returns:
            Design prompt string
        """
        # Map content types to prompt templates
        prompt_templates = {
            "announcement": """
Create a bold announcement graphic with:
- Dark background (black or deep purple #2D1A45)
- Bold headline text in electric green (#39FF14): "{title}"
- Subtle digital interference pattern or glitch effect overlay
- BLKOUT logo at 20% opacity as watermark in bottom right
- Minimal design with focus on typography
- Add subtle texture that suggests digital static or interference
            """,
            
            "concept_explanation": """
Create a 5-slide carousel explaining {title}:
- Consistent color scheme using brand colors (black, rich purple #2D1A45, electric green #39FF14)
- Slide 1: Large title "{title}" with one-line definition below
- Slides 2-4: Each with a single aspect of the concept, icon illustration, and brief text explanation
- Slide 5: Call to action with BLKOUT website and logo
- Use consistent font throughout (Montserrat for headings, Open Sans for body text)
- Add subtle pattern background that suggests connectivity/network
- Number each slide in corner (1/5, 2/5, etc.)
            """,
            
            "community_spotlight": """
Create a community spotlight graphic with:
- Split design: left 40% for photo, right 60% for text
- Place photo of community member in left section
- Add subtle gradient overlay in brand colors over photo
- Right section: Name in bold at top, short quote below in italics
- Add "COMMUNITY SPOTLIGHT" text vertically along edge
- Include small BLKOUT logo in bottom right corner
- Use consistent branded fonts (Montserrat Bold for name, Open Sans for quote)
- Add subtle texture or pattern in background that suggests community/connection
            """,
            
            "workshop_promotion": """
Create an event promotion graphic with:
- Date and time as largest elements (top third of image)
- Event title "{title}" in bold below date
- Brief 1-line description below title
- Visual element related to event theme in background or as accent
- Call to action button or text at bottom ("Register Now" or "Join Us")
- BLKOUT branding elements (logo, colors)
- Create sense of urgency/importance through design elements
- Add QR code linked to registration page in bottom corner (if applicable)
            """,
            
            "weekly_wrap_up": """
Create a weekly wrap-up graphic with:
- Grid layout dividing canvas into 4 sections
- Top header band with text "WEEK [#] WRAP-UP: {title}"
- Space for 2-3 highlight photos/screenshots from the week
- One section for key metrics or numbers (can be added manually later)
- Branded color scheme and typography
- Bottom section with "COMING NEXT WEEK" teaser
- Add texture or pattern that suggests progress/movement
- Include BLKOUT logo integrated into design
            """
        }
        
        # Get the appropriate prompt template
        content_type_key = content_type.lower().replace(" ", "_")
        prompt_template = prompt_templates.get(
            content_type_key, 
            "Create a social media post for BLKOUT NEXT with title: {title}"
        )
        
        # Add platform-specific instructions
        platform_instructions = {
            "instagram": "Format for Instagram (1080×1080px square or 1080×1350px portrait)",
            "facebook": "Format for Facebook (1200×630px)",
            "twitter": "Format for Twitter (1600×900px)"
        }
        
        platform_instruction = platform_instructions.get(
            platform.lower(), 
            "Format appropriately for social media"
        )
        
        # Combine the template and platform instruction
        prompt = f"{prompt_template}\n\n{platform_instruction}\n\nUse BLKOUT NEXT brand colors: Black (#000000), Deep Purple (#2D1A45), Electric Green (#39FF14)"
        
        return prompt
    
    def get_midjourney_prompt(self, content_type: str) -> str:
        """
        Get a Midjourney prompt for the specified content type
        
        Args:
            content_type: Type of content
            
        Returns:
            Midjourney prompt string
        """
        # Map content types to Midjourney prompts
        midjourney_prompts = {
            "announcement": """
A sophisticated digital interference pattern breaking through darkness, symbolizing Black queer voices emerging. Deep blacks and purples with electric green digital elements. Subtle pattern resembling signal waves or broadcasting symbols. Minimalist, modern tech aesthetic with subtle Afrofuturistic elements. Dramatic lighting, ultra-detailed, professional graphic design quality, suitable for campaign branding. --ar 1:1 --style raw
            """,
            
            "concept_explanation": """
Black hands collaboratively building/holding a glowing digital platform or device emitting light. Afrofuturistic aesthetic with purple and green tech elements. The technology appears organic and community-centered rather than corporate. Dramatic lighting highlighting diverse Black skin tones. Clean background with subtle tech patterns. Professional editorial illustration style. --ar 1:1 --style raw
            """,
            
            "community_question": """
A network of interconnected nodes representing Black queer community members, each node glowing with inner light. Abstract representation showing diversity within unity. Rich purple background with electric green connection lines. Modern, digital aesthetic with organic elements. Suitable for social media graphic about community building. Clean composition with focal point at center. --ar 1:1 --style raw
            """,
            
            "historical_context": """
A bridge connecting historical Black queer figures with modern community members. Vintage photography aesthetic on one side transitioning to modern digital style on the other. Subtle double exposure effect combining past and present. Purple and green color accents over predominantly black and white composition. Sophisticated, editorial style suitable for educational content. Respectful, dignified portrayal of historical elements. --ar 1:1 --style raw
            """,
            
            "call_to_action": """
Abstract representation of multiple Black voices/stories converging into a powerful unified narrative. Visualized as streams of light or energy in purple and green tones. African and Caribbean cultural patterns subtly integrated into the design. Digital media elements (screens, devices, platforms) artistically incorporated. Dramatic lighting, sophisticated composition with central focal point. Perfect for social media graphic about storytelling. --ar 1:1 --style raw
            """,
            
            "community_spotlight": """
Multiple Black hands jointly building or holding a media platform/structure. The structure appears as a blend of traditional broadcasting elements and futuristic technology. Purple and green color palette with warm highlights on diverse skin tones. Composition suggests equality and shared power. Clean background with subtle texture suggesting community fabric. Professional editorial illustration style. --ar 1:1 --style raw
            """
        }
        
        content_type_key = content_type.lower().replace(" ", "_")
        prompt = midjourney_prompts.get(
            content_type_key,
            "A sophisticated, abstract representation of Black queer media and community connection. Deep blacks and purples with electric green digital elements. Modern tech aesthetic with subtle Afrofuturistic elements. Professional graphic design quality suitable for BLKOUT NEXT campaign. --ar 1:1 --style raw"
        )
        
        return prompt.strip()
    
    def get_dalle_prompt(self, content_type: str) -> str:
        """
        Get a DALL-E prompt for the specified content type
        
        Args:
            content_type: Type of content
            
        Returns:
            DALL-E prompt string
        """
        # Map content types to DALL-E prompts
        dalle_prompts = {
            "announcement": """
Create a sophisticated, minimal background suitable for the BLKOUT NEXT campaign logo. Deep black background with subtle purple undertones and digital interference patterns resembling broadcasting signals. A few electric green digital elements emerging from the darkness. The design should be abstract, not literal, with clean negative space in the center where a logo could be placed. Modern tech aesthetic with an Afrofuturistic sensibility. No text or words in the image.
            """,
            
            "community_spotlight": """
Design a sophisticated frame for featuring Black queer community members. Create a modern, editorial-style border with elements that suggest both digital technology and community connection. Use a color scheme of deep purple, black, and electric green accents. The frame should have clean lines with subtle tech patterns and leave ample space in the center for a portrait photo. Include abstract elements that suggest broadcasting, storytelling, or signal transmission. No text or people in the design.
            """,
            
            "workshop_promotion": """
Create a background design for a virtual workshop event promotion. The design should feature abstract elements suggesting digital connection, learning, and collaboration. Use a color palette of deep purple, black, and electric green accents. The composition should have ample negative space at the center and top portion for event details and text to be added later. Include subtle patterns suggesting networking or digital infrastructure. The style should be sophisticated, professional, and suitable for a media/tech organization focused on Black queer community building. No text or words in the image.
            """,
            
            "weekly_wrap_up": """
Design a sophisticated social media profile frame for the BLKOUT NEXT campaign. Create a modern, tech-inspired border using black, deep purple, and electric green colors. The frame should suggest digital media, storytelling, and community connection through abstract elements. Leave clear space in the center for profile photos to be added later. Include subtle broadcasting/signal patterns that suggest amplifying voices. The design should be clean, professional, and suitable for a media organization focused on Black queer representation. No text or words in the image.
            """,
            
            "behind_the_scenes": """
Create a sophisticated header design for a digital newsletter about media ownership and Black queer storytelling. The design should be horizontal (banner format) with abstract elements suggesting broadcasting, digital media, and community connection. Use a color scheme of deep purple, black, and electric green accents. Include subtle patterns that suggest signal transmission or broadcasting. The design should have clean negative space on the right side where a title could be placed later. Modern tech aesthetic with subtle Afrofuturistic elements. No text or words in the image.
            """
        }
        
        content_type_key = content_type.lower().replace(" ", "_")
        prompt = dalle_prompts.get(
            content_type_key,
            "Create a sophisticated, abstract image representing Black queer voices breaking through traditional media barriers. Use a color scheme of deep purple, black, and electric green accents. Include elements suggesting broadcasting, signal transmission, or amplification. The style should be modern, digital, with subtle Afrofuturistic influences. Leave space for text overlay. No literal depictions of people, just abstract representation of voices and community."
        )
        
        return prompt.strip()

# Example usage
if __name__ == "__main__":
    # Test the Canva integration
    try:
        canva = CanvaIntegration()
        
        # Generate a design prompt
        prompt = canva.generate_design_prompt("announcement", "instagram")
        print("Design Prompt for Canva:")
        print(prompt)
        
        # Generate a Midjourney prompt
        midjourney_prompt = canva.get_midjourney_prompt("announcement")
        print("\nMidjourney Prompt:")
        print(midjourney_prompt)
        
        # Generate a DALL-E prompt
        dalle_prompt = canva.get_dalle_prompt("announcement")
        print("\nDALL-E Prompt:")
        print(dalle_prompt)
        
    except Exception as e:
        print(f"Error: {str(e)}")
