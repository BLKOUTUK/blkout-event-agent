# BLKOUT NEXT Campaign Quickstart Guide

This guide provides a consolidated reference of all key code snippets and commands for implementing the BLKOUT NEXT social media campaign.

## Table of Contents

1. [Setup Commands](#setup-commands)
2. [Content Management Snippets](#content-management-snippets)
3. [Design Tools Snippets](#design-tools-snippets)
4. [Social Media Snippets](#social-media-snippets)
5. [Email Campaign Snippets](#email-campaign-snippets)
6. [Metrics Tracking Snippets](#metrics-tracking-snippets)
7. [File Locations](#file-locations)

## Setup Commands

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Campaign Environment

Edit the `.env.campaign` file to set your API keys and campaign settings:

```
# Example of .env.campaign configuration
CAMPAIGN_NAME="The Signal"
CAMPAIGN_START_DATE="2023-04-14"
SENDFOX_API_KEY="your_sendfox_api_key"
INSTAGRAM_ACCESS_TOKEN="your_instagram_access_token"
# ... other settings
```

### Initialize Campaign

```bash
python initialize_campaign.py --start-date 2023-04-14 --name "The Signal"
```

### Set Up Canva Integration

```bash
python setup_canva_integration.py
```

### Generate Design Prompts

```bash
python generate_design_prompts.py --start-date 2023-04-14 --end-date 2023-04-21 --format json
```

## Content Management Snippets

### Initialize Content Calendar

```python
from integrations.content_manager import ContentManager

content_manager = ContentManager()
content_manager.create_initial_content_calendar('2023-04-14')
```

### Add Content to Calendar

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

### Get Content for a Date

```python
from integrations.content_manager import ContentManager

content_manager = ContentManager()
content_for_date = content_manager.get_content_for_date('2023-04-15')
print(content_for_date)
```

### Update Content Status

```python
from integrations.content_manager import ContentManager

content_manager = ContentManager()
content_manager.update_content_status(
    date='2023-04-15',
    platform='Instagram',
    title='THE SIGNAL IS BREAKING THROUGH',
    status='published',
    post_id='12345'
)
```

## Design Tools Snippets

### Create Design from Template

```python
from integrations.canva_integration import CanvaIntegration

canva = CanvaIntegration()
design = canva.create_design_from_template(
    content_type='announcement',
    title='THE SIGNAL IS BREAKING THROUGH',
    description='Launch announcement for BLKOUT NEXT campaign',
    platform='instagram'
)

print(f"Design created: {design.get('edit_url')}")
```

### Generate Design Prompt for Canva

```python
from integrations.canva_integration import CanvaIntegration

canva = CanvaIntegration()
prompt = canva.generate_design_prompt('announcement', 'instagram')
print(prompt.format(title='THE SIGNAL IS BREAKING THROUGH'))
```

### Generate Midjourney Prompt

```python
from integrations.canva_integration import CanvaIntegration

canva = CanvaIntegration()
midjourney_prompt = canva.get_midjourney_prompt('announcement')
print(midjourney_prompt)
```

### Generate DALL-E Prompt

```python
from integrations.canva_integration import CanvaIntegration

canva = CanvaIntegration()
dalle_prompt = canva.get_dalle_prompt('announcement')
print(dalle_prompt)
```

## Social Media Snippets

### Post to Instagram

```python
from integrations.social_media_config import InstagramAPI

instagram = InstagramAPI()
media_container = instagram.create_media_container(
    image_url='https://example.com/your-image.jpg',
    caption='THE SIGNAL IS BREAKING THROUGH\n\nFor too long, Black queer men in the UK have been defined by others. BLKOUT NEXT is creating a new reality.\n\n#BLKOUTNEXT #BlackQueerVoices #LiberationTech'
)
result = instagram.publish_media(media_container.get('creation_id'))
print(result)
```

### Post to Twitter

```python
from integrations.social_media_config import TwitterAPI

twitter = TwitterAPI()
result = twitter.create_tweet(
    text='THE SIGNAL IS BREAKING THROUGH\n\nBLKOUT NEXT is creating a new reality: platforms for power, visibility, and economic opportunity.\n\n#BLKOUTNEXT #BlackQueerVoices'
)
print(result)
```

### Post to Facebook

```python
from integrations.social_media_config import FacebookAPI

facebook = FacebookAPI()
result = facebook.create_post(
    message='THE SIGNAL IS BREAKING THROUGH\n\nFor too long, Black queer men in the UK have been defined by others. BLKOUT NEXT is creating a new reality.\n\n#BLKOUTNEXT #BlackQueerVoices #LiberationTech',
    photo_url='https://example.com/your-image.jpg'
)
print(result)
```

## Email Campaign Snippets

### Create Email List

```python
from integrations.sendfox_config import SendFoxAPI

sendfox = SendFoxAPI()
list_result = sendfox.create_list(
    name='BLKOUT NEXT - The Signal Campaign',
    description='Subscribers for The Signal campaign launch'
)
print(f"List created with ID: {list_result.get('id')}")
```

### Add Contact to List

```python
from integrations.sendfox_config import SendFoxAPI

sendfox = SendFoxAPI()
contact_result = sendfox.add_contact(
    email='example@email.com',
    first_name='John',
    last_name='Doe',
    lists=[123]  # Replace with your list ID
)
print(contact_result)
```

### Create and Send Campaign

```python
from integrations.sendfox_config import SendFoxAPI

sendfox = SendFoxAPI()
campaign_result = sendfox.create_campaign(
    name='BLKOUT NEXT: The Signal Launch',
    subject='The Signal is Breaking Through - Join the Revolution',
    email_html='<h1>THE SIGNAL IS BREAKING THROUGH</h1><p>For too long, Black queer men in the UK have been defined by others...</p>',
    list_ids=[123]  # Replace with your list ID
)
print(campaign_result)
```

## Metrics Tracking Snippets

### Update Campaign Metrics

```python
from integrations.content_manager import ContentManager

content_manager = ContentManager()
content_manager.update_campaign_metrics(
    date='2023-04-15',
    engagements=125,
    social_reach=2500,
    membership_conversions=3
)
```

### Generate Weekly Report

```python
from integrations.content_manager import ContentManager
import json

content_manager = ContentManager()
report = content_manager.generate_weekly_report('2023-04-14')
print(json.dumps(report, indent=2))
```

## File Locations

### Key Implementation Files

| File | Path | Description |
|------|------|-------------|
| Implementation Guide | `BLKOUT_NEXT_CAMPAIGN_README.md` | Comprehensive guide for the campaign implementation |
| Quickstart Guide | `BLKOUT_NEXT_CAMPAIGN_QUICKSTART.md` | This file - consolidated snippets and commands |
| Campaign Environment | `.env.campaign` | Campaign-specific environment variables and settings |
| Content Manager | `integrations/content_manager.py` | Content calendar and metrics management |
| Canva Integration | `integrations/canva_integration.py` | Design tools integration |
| Social Media Config | `integrations/social_media_config.py` | Social media platform integration |
| SendFox Config | `integrations/sendfox_config.py` | Email campaign integration |
| Canva MCP Server | `mcp-server/integration-server/canva/canva_mcp_server.py` | MCP server for Canva integration |
| Initialize Campaign | `initialize_campaign.py` | Script to set up the campaign |
| Generate Design Prompts | `generate_design_prompts.py` | Script to generate design prompts |
| Setup Canva Integration | `setup_canva_integration.py` | Script to configure Canva integration |

### Data Files

| File | Path | Description |
|------|------|-------------|
| Content Calendar | `data/content_calendar.csv` | Campaign content calendar |
| Campaign Metrics | `data/campaign_metrics.csv` | Campaign metrics tracking |
| Campaign Config | `data/campaign_config.json` | Campaign configuration |
| Design Prompts | `data/design_prompts.json` | Generated design prompts |

---

This quickstart guide provides a consolidated reference of all key code snippets and commands for implementing the BLKOUT NEXT social media campaign. For more detailed information, refer to the comprehensive implementation guide in `BLKOUT_NEXT_CAMPAIGN_README.md`.
