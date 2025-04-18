"""
Initialize BLKOUT NEXT Campaign
This script sets up the necessary components for the BLKOUT NEXT social media campaign.
"""
import os
import argparse
import json
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load campaign environment variables
env_campaign_path = os.path.join(os.path.dirname(__file__), '.env.campaign')
load_dotenv(env_campaign_path)

# Also load regular .env file as fallback
load_dotenv()

def initialize_campaign(start_date=None, campaign_name="The Signal"):
    """
    Initialize the BLKOUT NEXT campaign

    Args:
        start_date: Campaign start date in YYYY-MM-DD format (default: today)
        campaign_name: Name of the campaign (default: "The Signal")
    """
    # Set default start date if not provided
    if not start_date:
        start_date = datetime.now().strftime("%Y-%m-%d")

    print(f"Initializing BLKOUT NEXT campaign '{campaign_name}' starting on {start_date}")

    # Create necessary directories
    directories = [
        "data",
        "data/content",
        "data/designs",
        "data/metrics",
        "data/reports"
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

    # Initialize content calendar
    try:
        from integrations.content_manager import ContentManager
        content_manager = ContentManager()
        content_manager.create_initial_content_calendar(start_date)
        print("Content calendar initialized successfully")
    except Exception as e:
        print(f"Error initializing content calendar: {str(e)}")

    # Create campaign configuration file
    campaign_config = {
        "name": campaign_name,
        "start_date": start_date,
        "phases": [
            {
                "name": "The Signal Campaign Launch",
                "start_date": start_date,
                "duration_days": 7,
                "goals": {
                    "engagements": 500,
                    "membership_conversions": 50,
                    "social_reach": 100000,
                    "content_co_creation": 20,
                    "strategic_partnerships": 5
                }
            },
            {
                "name": "Amplification & Engagement",
                "start_date": (datetime.strptime(start_date, "%Y-%m-%d").replace(day=datetime.strptime(start_date, "%Y-%m-%d").day + 7)).strftime("%Y-%m-%d"),
                "duration_days": 7,
                "goals": {
                    "engagements": 750,
                    "membership_conversions": 75,
                    "social_reach": 150000,
                    "content_co_creation": 30,
                    "strategic_partnerships": 8
                }
            },
            {
                "name": "Momentum Building",
                "start_date": (datetime.strptime(start_date, "%Y-%m-%d").replace(day=datetime.strptime(start_date, "%Y-%m-%d").day + 14)).strftime("%Y-%m-%d"),
                "duration_days": 7,
                "goals": {
                    "engagements": 1000,
                    "membership_conversions": 100,
                    "social_reach": 200000,
                    "content_co_creation": 40,
                    "strategic_partnerships": 10
                }
            },
            {
                "name": "Transition to Next Phase",
                "start_date": (datetime.strptime(start_date, "%Y-%m-%d").replace(day=datetime.strptime(start_date, "%Y-%m-%d").day + 21)).strftime("%Y-%m-%d"),
                "duration_days": 7,
                "goals": {
                    "engagements": 1250,
                    "membership_conversions": 125,
                    "social_reach": 250000,
                    "content_co_creation": 50,
                    "strategic_partnerships": 12
                }
            }
        ],
        "brand_colors": {
            "primary": "#000000",  # Black
            "secondary": "#2D1A45",  # Deep Purple
            "accent": "#39FF14",  # Electric Green
            "supporting": "#F2F2F2"  # Light Gray
        },
        "brand_fonts": {
            "headings": "Montserrat Bold",
            "subheadings": "Montserrat Medium",
            "body": "Open Sans Regular",
            "accent": "Open Sans Italic"
        },
        "hashtags": [
            "#BLKOUTNEXT",
            "#BlackQueerVoices",
            "#LiberationTech",
            "#OurStoriesOurTerms",
            "#BlackQueerFutures",
            "#CommunityOwnership",
            "#MediaRevolution"
        ]
    }

    # Save campaign configuration
    config_path = Path("data/campaign_config.json")
    with open(config_path, 'w') as f:
        json.dump(campaign_config, f, indent=2)

    print(f"Campaign configuration saved to {config_path}")

    # Generate design prompts
    try:
        # Import here to avoid circular imports
        import sys
        sys.path.append(os.path.dirname(__file__))
        from generate_design_prompts import generate_prompts_for_calendar

        # Generate prompts for the first week
        end_date = (datetime.strptime(start_date, "%Y-%m-%d").replace(day=datetime.strptime(start_date, "%Y-%m-%d").day + 7)).strftime("%Y-%m-%d")
        generate_prompts_for_calendar(start_date, end_date, "json")
        print(f"Design prompts generated for {start_date} to {end_date}")
    except Exception as e:
        print(f"Error generating design prompts: {str(e)}")

    print("\nBLKOUT NEXT campaign initialization complete!")
    print("\nNext steps:")
    print("1. Review the content calendar in data/content_calendar.csv")
    print("2. Check the design prompts in data/design_prompts.json")
    print("3. Set up social media platform integrations")
    print("4. Configure email campaign in SendFox")
    print("5. Create automation workflows in n8n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize BLKOUT NEXT Campaign")
    parser.add_argument("--start-date", help="Campaign start date in YYYY-MM-DD format")
    parser.add_argument("--name", default="The Signal", help="Campaign name")

    args = parser.parse_args()

    initialize_campaign(args.start_date, args.name)
