# # BLKOUT Event Listings Agent

A comprehensive automated system for aggregating, evaluating, and distributing events relevant to the Black queer UK community. This project uses n8n workflows, Airtable databases, AI-powered relevance analysis, and a WordPress integration to create a complete event discovery and sharing solution.

## System Overview

![System Architecture Diagram](docs/images/architecture-diagram.png)

The BLKOUT Event Listings Agent consists of five main components:

1. **Daily Web Scraper**: Automatically collects events from up to 10 curated websites
2. **Google Calendar Integration**: Imports events from a dedicated community calendar
3. **Event Processor**: Uses AI to determine relevance and categorize events by theme
4. **Newsletter Generator**: Creates and distributes themed email newsletters
5. **WordPress Integration**: Displays events on the community website

All components are built using n8n workflows and Airtable databases, creating a flexible, maintainable system that can evolve with community needs.

## Project Goals

- **Reduce Manual Effort**: Automate the discovery and processing of community events
- **Improve Relevance**: Ensure events are appropriate for the Black queer UK audience
- **Increase Visibility**: Share events through multiple channels (email, web)
- **Build Community**: Foster connection through shared events and experiences
- **Create Structure**: Establish sustainable infrastructure for ongoing community support

## Key Features

- **Intelligent Event Scraping**: Automated collection from multiple sources
- **AI-Powered Relevance Analysis**: Smart filtering of events based on community relevance
- **Thematic Categorization**: Organization of events into meaningful themes
- **Customizable Newsletters**: Theme-based email distribution with personalization
- **Interactive Website Widget**: Responsive, filterable event display on WordPress
- **Google Calendar Integration**: Support for manually added community events
- **System Health Monitoring**: Automated checks and alerts for system maintenance

## Technologies Used

- **n8n**: Workflow automation platform for all processing logic
- **Airtable**: Database for event storage and management
- **OpenAI API**: AI-powered event analysis and content generation
- **Google Calendar API**: Calendar integration for manual event addition
- **WordPress**: Website integration for event display
- **SMTP**: Email delivery for newsletters

## Getting Started

See the [Implementation Guide](docs/implementation-guide.md) for complete setup instructions.

### Prerequisites

- n8n instance (self-hosted or cloud)
- Airtable account with API access
- OpenAI API key
- Google Calendar API credentials
- WordPress website with admin access
- SMTP server for email delivery

### Quick Start

1. Clone this repository
2. Set up the Airtable base using the [schema templates](airtable/base-templates/)
3. Import the n8n workflows from the [n8n-workflows](n8n-workflows/) directory
4. Configure API credentials in n8n
5. Install the WordPress plugin from the [wordpress](wordpress/) directory
6. Run the Master Coordinator workflow to verify system health

## Implementation Plan

This project uses a phased implementation approach:

1. **Phase 1**: Project Setup & Infrastructure
2. **Phase 2**: Airtable Database Implementation
3. **Phase 3**: n8n Workflow Implementation
4. **Phase 4**: WordPress Integration
5. **Phase 5**: Testing and Refinement
6. **Phase 6**: Documentation and Deployment
7. **Phase 7**: Launch and Feedback

See the [implementation tasks](implementation/tasks.md) for detailed task breakdowns.

## Contributing

Contributions to improve the BLKOUT Event Listings Agent are welcome! Please see our [Contributing Guide](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [BLKOUT UK](https://blkoutuk.com) for inspiring this project
- The Black queer community in the UK for their ongoing resilience and creativity
- All the event organizers who create spaces for community connection

## Support

For questions, issues, or feature requests, please [open an issue](https://github.com/yourusername/blkout-event-agent/issues/new/choose) on this repository.
