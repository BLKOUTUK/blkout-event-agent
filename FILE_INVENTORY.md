# BLKOUT Project File Inventory

This document provides an inventory of key files in the repository and identifies which project component they belong to.

## Events Curator System

- `events-system/scrapers/` - Event scraping scripts
  - `eventbrite_scraper.py` - Scrapes events from Eventbrite
  - `outsavvy_scraper.py` - Scrapes events from Outsavvy
  - `organization_scraper.py` - Scrapes events from organization websites

- `events-system/processors/` - Event processing scripts
  - `event_categorizer.py` - Categorizes events by type and relevance
  - `event_enhancer.py` - Enhances event descriptions using AI

- `events-system/integrations/` - Integration scripts
  - `wordpress_calendar.py` - Integrates with WordPress calendar
  - `airtable_events.py` - Manages events in Airtable

- `events-system/workflows/` - n8n workflows
  - `community-surveys.json` - Main event scraping workflow
  - `event_processor.json` - Event processing workflow

## BQM Member Management System

- `bqm-members/registration/` - BQM registration processing
  - `bqm_registration_processor.py` - Processes BQM registrations
  - `eligibility_verification.py` - Verifies eligibility for BQM membership

- `bqm-members/profiling/surveys/` - BQM survey definitions and processing
  - `bqm_survey_processor.py` - Processes BQM survey responses
  - `bqm_survey_templates/` - Survey templates for BQM members

- `bqm-members/engagement/email-templates/` - BQM email templates
  - `bqm_welcome_email.html` - BQM welcome email template
  - `bqm_reminder_email.html` - BQM reminder email template
  - `bqm_confirmation_email.html` - BQM confirmation email template

- `bqm-members/engagement/drip-campaigns/` - BQM email drip campaign workflows
  - `bqm_drip.json` - Drip campaign for BQM members

- `bqm-members/retention/` - BQM retention strategies
  - `bqm_reengagement.py` - Re-engagement strategies for BQM members
  - `bqm_leadership_pathways.py` - Leadership development for BQM members

## Social Media Campaign

- `social-media/templates/` - Content templates
  - `announcement_template.md` - Template for announcements
  - `spotlight_template.md` - Template for community spotlights

- `social-media/schedulers/` - Posting schedulers
  - `content_scheduler.py` - Schedules content for posting
  - `posting_calendar.json` - Content calendar

- `social-media/analytics/` - Analytics scripts
  - `engagement_tracker.py` - Tracks engagement metrics
  - `campaign_reporter.py` - Generates campaign reports

- `social-media/design-integrations/` - Design tool integrations
  - `canva_integration.py` - Integrates with Canva
  - `design_prompt_generator.py` - Generates design prompts

## Network Recognition System

- `network-recognition/point-system/` - Network contribution tracking
  - `contribution_schema.json` - Schema for the network contribution system
  - `contribution_calculator.py` - Calculates recognition for network contributions

- `network-recognition/achievement-tracking/` - Collaborative achievement tracking
  - `collaborative_achievements.json` - Definitions for collaborative achievements
  - `partnership_milestones.py` - Tracks partnership milestones

- `network-recognition/redemption/` - Partnership benefits
  - `partnership_benefits.json` - Available benefits for network partners
  - `resource_sharing.py` - Manages resource sharing between partners

- `network-recognition/recognition/` - Network spotlight
  - `network_spotlight.py` - Manages spotlights for network contributors
  - `recognition_templates.html` - Templates for network recognition

- `network-recognition/reporting/` - Ecosystem impact reporting
  - `network_impact_metrics.py` - Tracks impact of network contributions
  - `ecosystem_health_dashboard.py` - Dashboard for ecosystem health

## Shared Resources

- `shared/config/` - Configuration files
  - `.env.example` - Example environment variables
  - `blkout_nxt_config.json` - Configuration for NXT system

- `shared/utils/` - Utility functions
  - `date_utils.py` - Date/time handling utilities
  - `text_processor.py` - Text processing utilities

- `shared/email/` - Email functionality
  - `email_sender.py` - Email sending utilities
  - `template_renderer.py` - Email template rendering

- `shared/api/` - API clients
  - `airtable_client.py` - Airtable API client
  - `supabase_client.py` - Supabase API client

## MCP Server

- `mcp-server/tools/` - MCP tool definitions
  - `event_tools.py` - Tools for event processing
  - `content_tools.py` - Tools for content generation

- `mcp-server/resources/` - MCP resources
  - `events_resource.py` - Resource for accessing events
  - `members_resource.py` - Resource for accessing members

- `mcp-server/integrations/` - Service integrations
  - `n8n_integration.py` - Integration with n8n
  - `openrouter_integration.py` - Integration with OpenRouter

- `mcp-server/n8n/` - n8n specific implementations
  - `n8n_server.py` - MCP server for n8n
  - `n8n_client.py` - MCP client for n8n

## Cross-Project Files

- `README.md` - Main repository documentation
- `LICENSE` - MIT license file
- `requirements.txt` - Python dependencies
- `package.json` - Node.js dependencies
- `.env.example` - Example environment variables
- `.gitignore` - Git ignore file

## Note on File Organization

This inventory represents the ideal organization of files. As part of the repository reorganization, files will be moved to their appropriate locations according to this structure. Some files may need to be renamed or refactored to fit this organization.

## Cross-Repository References

Some files in this repository are referenced by other repositories:

- `mcp-server/n8n/n8n_server.py` - Referenced by the BLKOUT WordPress repository
- `events-system/integrations/wordpress_calendar.py` - Referenced by the BLKOUT WordPress repository
- `onboarding/form-integrations/tally_webhook.py` - Referenced by external form providers
