"""
Generate Design Prompts for BLKOUT NEXT Campaign
This script generates design prompts for different content types and platforms.
"""
import os
import csv
import json
import argparse
from datetime import datetime, timedelta
from integrations.canva_integration import CanvaIntegration
from integrations.content_manager import ContentManager

def generate_prompts_for_calendar(start_date=None, end_date=None, output_format="text"):
    """
    Generate design prompts for all items in the content calendar within the date range
    
    Args:
        start_date: Start date in YYYY-MM-DD format (default: today)
        end_date: End date in YYYY-MM-DD format (default: start_date + 7 days)
        output_format: Output format (text, csv, json)
    """
    # Initialize the content manager and Canva integration
    content_manager = ContentManager()
    canva = CanvaIntegration()
    
    # Set default dates if not provided
    if not start_date:
        start_date = datetime.now().strftime("%Y-%m-%d")
    
    if not end_date:
        end_date = (datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=7)).strftime("%Y-%m-%d")
    
    # Get content calendar items for the date range
    calendar_df = pd.read_csv(content_manager.content_calendar_path)
    mask = (
        (calendar_df['date'] >= start_date) & 
        (calendar_df['date'] <= end_date)
    )
    calendar_items = calendar_df[mask].to_dict('records')
    
    if not calendar_items:
        print(f"No content calendar items found for date range {start_date} to {end_date}")
        return
    
    # Generate prompts for each item
    prompts = []
    
    for item in calendar_items:
        content_type = item.get("content_type", "").lower().replace(" ", "_")
        platform = item.get("platform", "instagram").lower()
        title = item.get("title", "Untitled")
        
        # Generate prompts for different design tools
        canva_prompt = canva.generate_design_prompt(content_type, platform).format(title=title)
        midjourney_prompt = canva.get_midjourney_prompt(content_type)
        dalle_prompt = canva.get_dalle_prompt(content_type)
        
        prompt_data = {
            "date": item.get("date"),
            "platform": platform,
            "content_type": content_type,
            "title": title,
            "canva_prompt": canva_prompt,
            "midjourney_prompt": midjourney_prompt,
            "dalle_prompt": dalle_prompt
        }
        
        prompts.append(prompt_data)
    
    # Output the prompts in the requested format
    if output_format.lower() == "text":
        output_text_prompts(prompts)
    elif output_format.lower() == "csv":
        output_csv_prompts(prompts)
    elif output_format.lower() == "json":
        output_json_prompts(prompts)
    else:
        print(f"Unknown output format: {output_format}")

def output_text_prompts(prompts):
    """Output prompts in text format"""
    for prompt in prompts:
        print("=" * 80)
        print(f"Date: {prompt['date']}")
        print(f"Platform: {prompt['platform']}")
        print(f"Content Type: {prompt['content_type']}")
        print(f"Title: {prompt['title']}")
        print("-" * 40)
        print("Canva Prompt:")
        print(prompt['canva_prompt'])
        print("-" * 40)
        print("Midjourney Prompt:")
        print(prompt['midjourney_prompt'])
        print("-" * 40)
        print("DALL-E Prompt:")
        print(prompt['dalle_prompt'])
        print("=" * 80)
        print()

def output_csv_prompts(prompts):
    """Output prompts in CSV format"""
    output_path = os.path.join(os.path.dirname(__file__), "data", "design_prompts.csv")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'date', 'platform', 'content_type', 'title', 
            'canva_prompt', 'midjourney_prompt', 'dalle_prompt'
        ])
        
        for prompt in prompts:
            writer.writerow([
                prompt['date'],
                prompt['platform'],
                prompt['content_type'],
                prompt['title'],
                prompt['canva_prompt'],
                prompt['midjourney_prompt'],
                prompt['dalle_prompt']
            ])
    
    print(f"CSV output saved to {output_path}")

def output_json_prompts(prompts):
    """Output prompts in JSON format"""
    output_path = os.path.join(os.path.dirname(__file__), "data", "design_prompts.json")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(prompts, f, indent=2)
    
    print(f"JSON output saved to {output_path}")

if __name__ == "__main__":
    # Import pandas here to avoid dependency issues
    import pandas as pd
    
    parser = argparse.ArgumentParser(description="Generate design prompts for BLKOUT NEXT Campaign")
    parser.add_argument("--start-date", help="Start date in YYYY-MM-DD format")
    parser.add_argument("--end-date", help="End date in YYYY-MM-DD format")
    parser.add_argument("--format", choices=["text", "csv", "json"], default="text",
                        help="Output format (text, csv, json)")
    parser.add_argument("--initialize", action="store_true",
                        help="Initialize content calendar before generating prompts")
    
    args = parser.parse_args()
    
    # Initialize content calendar if requested
    if args.initialize:
        content_manager = ContentManager()
        start_date = args.start_date or datetime.now().strftime("%Y-%m-%d")
        content_manager.create_initial_content_calendar(start_date)
        print(f"Initialized content calendar starting from {start_date}")
    
    # Generate prompts
    generate_prompts_for_calendar(args.start_date, args.end_date, args.format)
