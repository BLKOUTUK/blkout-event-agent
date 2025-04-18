# BLKOUT Events Calendar System

This directory contains the components of the BLKOUT Events Calendar system, which automatically discovers, processes, and distributes events relevant to the Black LGBTQ+ community.

## System Outcomes

### Event Discovery
Automatically finds events from various sources that are relevant to the Black LGBTQ+ community:
- Scrapes events from Eventbrite, Outsavvy, and organization websites
- Imports events from Google Calendar
- Accepts manual submissions via webhooks

### Event Processing
Enhances and categorizes event data to make it more useful:
- Categorizes events by type (community, social, workshop, etc.)
- Scores events by relevance to the BLKOUT audience
- Enhances event descriptions for clarity and completeness
- Normalizes date/time information across different sources

### Event Storage
Stores event data in a structured format:
- Maintains a database of events in Airtable/Supabase
- Tracks event metadata like categories, relevance scores, and relationships
- Provides a consistent data schema for all events

### Event Display
Makes events accessible to the community:
- Integrates with WordPress calendar for web display
- Provides embeddable calendar components
- Offers filtering and search capabilities

### Event Notification
Keeps the community informed about upcoming events:
- Generates newsletters with upcoming events
- Sends targeted notifications based on event categories
- Provides email alerts for new high-relevance events

## Event Sources

The system currently scrapes events from:
- UK Black Pride
- Stonewall
- Eventbrite LGBTQ+ Events
- Outsavvy
- QX Magazine
- TimeOut
- QueerAF
- Attitude Magazine
- GayLondonLife
- Queer Britain
- LGBT Consortium
- Lesbian and Gay Foundation
- Google Calendar

## Event Categories

Events are categorized into:
- community: Community-building, meetups, networking
- social: Parties, social gatherings, entertainment
- workshop: Skill-building, interactive learning sessions
- art: Performances, exhibitions, film screenings, creative events
- health: Wellness, mental health, physical health
- education: Talks, panels, discussions, lectures
- support: Support groups, peer support, counseling
- activism: Protests, campaigns, political events
- pride: Pride-related celebrations and events

## BLKOUT Relationships

Events are tagged with their relationship to BLKOUT:
- partner: Official BLKOUT partner organizations
- QTIPOC ally: Organizations focused on QTIPOC communities
- other: General LGBTQ+ or other organizations

## Setup and Configuration

1. Configure event sources in the appropriate scraper configuration files
2. Set up database credentials in the `.env` file
3. Configure WordPress integration if using the calendar feature
4. Set up email notifications for new events

## Usage

The system runs automatically based on scheduled triggers, but can also be manually triggered through the n8n interface.

## Dependencies

- n8n for workflow automation
- MCP server for AI agent integration
- Airtable/Supabase for data storage
- WordPress for calendar display (optional)
