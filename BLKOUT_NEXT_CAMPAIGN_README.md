# BLKOUT NEXT Campaign Implementation Guide

This guide provides instructions for implementing the BLKOUT NEXT social media campaign using the tools and scripts in this repository.

## Table of Contents

1. [Overview](#overview)
2. [Setup](#setup)
3. [Content Management](#content-management)
4. [Design Tools Integration](#design-tools-integration)
5. [Social Media Integration](#social-media-integration)
6. [Email Campaign Integration](#email-campaign-integration)
7. [Automation Workflows](#automation-workflows)
8. [Metrics Tracking](#metrics-tracking)
9. [Troubleshooting](#troubleshooting)

## Overview

The BLKOUT NEXT campaign implementation includes:

- Content calendar management
- Design tools integration (Canva, Midjourney, DALL-E)
- Social media platform integration
- Email campaign integration with SendFox
- Automation workflows with n8n
- Metrics tracking and reporting

## Setup

### Prerequisites

- Python 3.7+
- n8n installed and running
- API keys for:
  - SendFox
  - Canva (optional)
  - Social media platforms (Instagram, Twitter, Facebook)

### Installation

1. Install required Python packages:

```bash
pip install -r requirements.txt
```

2. Configure the campaign environment by editing the `.env.campaign` file:

```
# Campaign Settings
CAMPAIGN_NAME="The Signal"
CAMPAIGN_START_DATE="2023-04-14"

# API Keys
SENDFOX_API_KEY=your_sendfox_api_key
INSTAGRAM_ACCESS_TOKEN=your_instagram_access_token
INSTAGRAM_PAGE_ID=your_instagram_page_id
INSTAGRAM_ACCOUNT_ID=your_instagram_account_id
TWITTER_BEARER_TOKEN=your_twitter_bearer_token
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_SECRET=your_twitter_access_secret
FACEBOOK_ACCESS_TOKEN=your_facebook_access_token
FACEBOOK_PAGE_ID=your_facebook_page_id
CANVA_API_KEY=your_canva_api_key
CANVA_BRAND_KIT_ID=your_canva_brand_kit_id

# Campaign Brand Colors
BRAND_COLOR_PRIMARY="#000000"
BRAND_COLOR_SECONDARY="#2D1A45"
BRAND_COLOR_ACCENT="#39FF14"
```

This dedicated environment file keeps your campaign configuration separate from other projects.

3. Set up Canva integration (optional):

```bash
python setup_canva_integration.py
```

4. Initialize the campaign:

```bash
python initialize_campaign.py --start-date 2023-04-14 --name "The Signal"
```

## Content Management

The content management system helps you organize, schedule, and track your campaign content.

### Initialize Content Calendar

To create an initial content calendar based on the campaign plan:

```bash
python -c "from integrations.content_manager import ContentManager; ContentManager().create_initial_content_calendar('2023-04-14')"
```

Replace `'2023-04-14'` with your campaign start date.

### View Content Calendar

The content calendar is stored in `data/content_calendar.csv`. You can view it using any spreadsheet application or with Python:

```bash
python -c "import pandas as pd; print(pd.read_csv('data/content_calendar.csv'))"
```

### Add Content to Calendar

To add new content to the calendar:

```python
from integrations.content_manager import ContentManager

content_manager = ContentManager()
content_manager.add_content_to_calendar(
    date='2023-04-15',
    platform='Instagram',
    content_type='Campaign Announcement',
    title='THE SIGNAL IS BREAKING THROUGH',
    description='Launch announcement for BLKOUT NEXT campaign'
)
```

## Design Tools Integration

### Generate Design Prompts

To generate design prompts for your content calendar:

```bash
python generate_design_prompts.py --start-date 2023-04-14 --end-date 2023-04-21 --format csv
```

This will create design prompts for Canva, Midjourney, and DALL-E for all content in the specified date range.

### Using Canva Integration

If you have set up the Canva API integration:

```python
from integrations.canva_integration import CanvaIntegration

canva = CanvaIntegration()

# Create a design for a specific content type
design = canva.create_design_from_template(
    content_type='announcement',
    title='THE SIGNAL IS BREAKING THROUGH',
    description='Launch announcement for BLKOUT NEXT campaign',
    platform='instagram'
)

print(f"Design created: {design.get('edit_url')}")
```

### Using Design Prompts

The design prompts can be used with:

1. **Canva**: Copy the Canva prompt into Canva's editor or use with Canva's AI features
2. **Midjourney**: Use the Midjourney prompt in Discord with the Midjourney bot
3. **DALL-E**: Use the DALL-E prompt with OpenAI's DALL-E interface

## Social Media Integration

### Post to Social Media

To post content to social media platforms:

```python
from integrations.social_media_config import InstagramAPI, TwitterAPI, FacebookAPI

# Post to Instagram
instagram = InstagramAPI()
media_container = instagram.create_media_container(
    image_url='https://example.com/your-image.jpg',
    caption='THE SIGNAL IS BREAKING THROUGH\n\nFor too long, Black queer men in the UK have been defined by others. BLKOUT NEXT is creating a new reality.\n\n#BLKOUTNEXT #BlackQueerVoices #LiberationTech'
)
instagram.publish_media(media_container.get('creation_id'))

# Post to Twitter
twitter = TwitterAPI()
twitter.create_tweet(
    text='THE SIGNAL IS BREAKING THROUGH\n\nBLKOUT NEXT is creating a new reality: platforms for power, visibility, and economic opportunity.\n\n#BLKOUTNEXT #BlackQueerVoices'
)

# Post to Facebook
facebook = FacebookAPI()
facebook.create_post(
    message='THE SIGNAL IS BREAKING THROUGH\n\nFor too long, Black queer men in the UK have been defined by others. BLKOUT NEXT is creating a new reality.\n\n#BLKOUTNEXT #BlackQueerVoices #LiberationTech',
    photo_url='https://example.com/your-image.jpg'
)
```

## Email Campaign Integration

### Create Email Lists

To create email lists in SendFox:

```python
from integrations.sendfox_config import SendFoxAPI

sendfox = SendFoxAPI()

# Create a list for the campaign
list_result = sendfox.create_list(
    name='BLKOUT NEXT - The Signal Campaign',
    description='Subscribers for The Signal campaign launch'
)

print(f"List created with ID: {list_result.get('id')}")
```

### Send Campaign Email

To send a campaign email:

```python
from integrations.sendfox_config import SendFoxAPI

sendfox = SendFoxAPI()

# Create and send a campaign
campaign_result = sendfox.create_campaign(
    name='BLKOUT NEXT: The Signal Launch',
    subject='The Signal is Breaking Through - Join the Revolution',
    email_html='<h1>THE SIGNAL IS BREAKING THROUGH</h1><p>For too long, Black queer men in the UK have been defined by others...</p>',
    list_ids=[your_list_id]
)

print(f"Campaign created: {campaign_result}")
```

## Automation Workflows

### Create n8n Workflows

You can create n8n workflows for automating various aspects of the campaign:

1. Content scheduling and posting
2. Engagement monitoring
3. Metrics collection
4. Email campaign automation

Example workflow creation:

```python
import json
from pathlib import Path

# Load a workflow template
workflow_path = Path('n8n json rb/social_media_workflow_template.json')
with open(workflow_path, 'r') as f:
    workflow_data = json.load(f)

# Customize the workflow
workflow_data['name'] = 'BLKOUT NEXT - Social Media Posting'

# Save the customized workflow
output_path = Path('n8n json rb/blkout_next_social_media_workflow.json')
with open(output_path, 'w') as f:
    json.dump(workflow_data, f, indent=2)

print(f"Workflow saved to {output_path}")
```

## Metrics Tracking

### Update Campaign Metrics

To update campaign metrics:

```python
from integrations.content_manager import ContentManager

content_manager = ContentManager()

# Update metrics for a specific date
content_manager.update_campaign_metrics(
    date='2023-04-15',
    engagements=125,
    social_reach=2500,
    membership_conversions=3
)
```

### Generate Weekly Report

To generate a weekly report:

```python
from integrations.content_manager import ContentManager

content_manager = ContentManager()

# Generate report for a specific week
report = content_manager.generate_weekly_report('2023-04-14')
print(json.dumps(report, indent=2))
```

## Troubleshooting

### Common Issues

1. **API Connection Errors**
   - Check that your API keys are correctly set in the `.env` file
   - Verify that the APIs are accessible from your network

2. **Content Calendar Issues**
   - Ensure the `data` directory exists and is writable
   - Check that the CSV files are not open in another application

3. **Design Tool Integration**
   - For Canva API issues, verify your API key and permissions
   - For design prompt generation, ensure the content types match the expected values

### Getting Help

If you encounter issues not covered in this guide:

1. Check the error messages for specific details
2. Review the API documentation for the service you're trying to use
3. Consult the code comments for additional information

---

This implementation guide provides the foundation for running the BLKOUT NEXT social media campaign. Customize the tools and scripts as needed to fit your specific requirements and workflow.
