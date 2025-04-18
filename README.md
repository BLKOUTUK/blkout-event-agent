# BLKOUT Community Ecosystem

This repository contains the interconnected systems that power BLKOUT UK's community ecosystem. These systems work together to create a comprehensive platform focused on key community outcomes.

## Community Outcomes

### 1. Events Calendar
Connects the community with relevant events and opportunities.
- **Discovery**: Automatically finds events from various sources
- **Curation**: Enhances and categorizes events for relevance
- **Access**: Makes events accessible through WordPress calendar
- **Notification**: Keeps the community informed about upcoming events

[Learn more about the Events Calendar](./events-system/README.md)

### 2. BQM Member Management
Builds and nurtures BLKOUT's core Black queer men membership.
- **BQM Registration**: Captures new Black queer men member information
- **BQM Profiling**: Builds comprehensive profiles of Black queer men
- **BQM Engagement**: Maintains ongoing communication with BQM members
- **BQM Retention**: Encourages continued participation of Black queer men

[Learn more about BQM Member Management](./bqm-members/README.md)

### 3. Campaign Communications
Amplifies BLKOUT's message and engages the broader community.
- **Planning**: Strategically plans communication campaigns
- **Creation**: Produces high-quality, engaging content
- **Distribution**: Delivers content to the right audiences
- **Analysis**: Evaluates campaign effectiveness

[Learn more about Campaign Communications](./social-media/README.md)

### 4. Network Recognition
Encourages, tracks, and rewards contributions from the broader network supporting Black queer men.
- **Contribution Tracking**: Recognizes support from allies, organizations, and QTIPOC organizers
- **Collaborative Achievements**: Acknowledges cross-community initiatives
- **Partnership Benefits**: Provides advantages for active network participants
- **Network Spotlight**: Highlights exceptional contributors to the ecosystem

[Learn more about Network Recognition](./network-recognition/README.md)

## Shared Infrastructure

All these systems are powered by a common infrastructure that provides:
- **System Configuration**: Centralized configuration management
- **Communication Services**: Shared communication capabilities
- **Data Management**: Centralized data handling services
- **External Integrations**: Connections to third-party services
- **AI Services**: Shared artificial intelligence capabilities

[Learn more about Shared Infrastructure](./shared/README.md)

## MCP Server Integration

The Multi-Agent Collaboration Protocol (MCP) server provides AI agent capabilities across all systems:
- AI-powered event discovery and categorization
- Personalized member communications
- Content generation for campaigns
- Intelligent reward recommendations

[Learn more about the MCP Server](./mcp-server/README.md)

## Repository Structure

- `/events-system/` - Events Calendar system
- `/bqm-members/` - BQM Member Management system
- `/social-media/` - Campaign Communications system
- `/network-recognition/` - Network Recognition system
- `/shared/` - Shared infrastructure components
- `/mcp-server/` - MCP server implementation

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Node.js 14 or higher
- n8n installed locally or in a Docker container
- Airtable and/or Supabase account
- OpenRouter API key for AI model access

### Installation

1. Clone this repository
2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Install Node.js dependencies:
   ```
   npm install
   ```
4. Configure environment variables in `.env`
5. Start the MCP server:
   ```
   python mcp-server/integration-server/n8n/n8n_server.py
   ```
6. Import the n8n workflows

### Configuration

Create a `.env` file with the following variables:

```
OPENROUTER_API_KEY=your_api_key
AIRTABLE_API_KEY=your_airtable_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
SMTP_USERNAME=your_email@example.com
SMTP_PASSWORD=your_email_password
```

For the Member Management system, create a `blkout_nxt_config.json` file with your configuration:
```json
{
  "google_sheets": {
    "document_id": "BLKOUT NXT Subscriber Management",
    "sheet_name": "Welcome"
  },
  "email": {
    "from_email": "nxt@blkoutuk.com",
    "admin_email": "blkoutuk@gmail.com"
  },
  "survey_links": {
    "ally_survey": "https://forms.gle/DerFGtG8vrZVPZaB7",
    "bqm_survey": "https://forms.gle/DerFGtG8vrZVPZaB7",
    "qtipoc_organiser_survey": "https://forms.gle/bvZm2UkcsL4LGSq17",
    "organisation_survey": "https://forms.gle/w3mZSj8KPiVnW3Zx7"
  }
}
```

## Key Integrations

### Events Calendar Integrations
- WordPress Calendar for event display
- Airtable/Supabase for event storage
- Eventbrite/Outsavvy for event discovery
- Google Calendar for event import/export

### BQM Member Management Integrations
- Tally for Black queer men registration forms
- Google Sheets for BQM member data storage
- SMTP for targeted email communications
- Survey platforms for detailed BQM profiling

### Campaign Communications Integrations
- Social media platforms (Instagram, Twitter, Facebook, etc.)
- Canva for design creation
- SendFox for email campaigns
- Analytics platforms for performance tracking

### Network Recognition Integrations
- Events system for collaborative event tracking
- BQM Member system for network connection mapping
- Campaign system for cross-community engagement metrics
- WordPress for network partner showcase
- Partnership management tools for collaboration tracking

## API Endpoints

### BQM Member Management Endpoints
- `POST /webhook/blkout-bqm-signup` - Handle BQM member signup
- `POST /webhook/blkout-bqm-survey` - Process BQM survey responses
- `GET /api/bqm-members` - Get all BQM members
- `GET /api/bqm-members/{member_id}` - Get a specific BQM member
- `POST /api/send-bqm-reminders` - Send BQM reminder emails

### Events Calendar Endpoints
- `GET /api/events` - Get all events
- `GET /api/events/{event_id}` - Get a specific event
- `POST /api/events` - Create a new event
- `PUT /api/events/{event_id}` - Update an event

### Webhook Integration

This system supports integration with Tally forms and other webhook providers. To integrate with Tally:

1. Go to your Tally form settings
2. Navigate to the "Integrations" tab
3. Select "Webhooks"
4. Add a new webhook with the URL: `http://your-server-address/webhook/blkout-nxt-signup`
5. For survey forms, use: `http://your-server-address/webhook/blkout-nxt-survey`
6. Copy the signing secret provided by Tally
7. Add the signing secret to your `.env` file as `TALLY_SIGNING_SECRET=your_signing_secret`

## Development

### Adding New Features

When adding new features, consider:
1. Which community outcome the feature supports
2. How it integrates with existing components
3. Whether it could be a shared infrastructure component
4. How it will be maintained and updated

### Testing

Each system has its own testing procedures. See the system-specific README files for details.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

BLKOUT UK