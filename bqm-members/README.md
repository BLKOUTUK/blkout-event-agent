# BLKOUT BQM Member Management System

This directory contains the components of the BLKOUT Black Queer Men (BQM) Member Management system, which handles the complete lifecycle of BLKOUT's core Black queer men membership from registration to ongoing engagement.

## System Outcomes

### BQM Registration
Captures new Black queer men member information and initiates the onboarding process:
- Processes form submissions from Tally and other providers
- Validates and normalizes member data
- Verifies eligibility for BQM membership
- Triggers the initial welcome sequence

### BQM Profiling
Builds comprehensive profiles of Black queer men members to better serve their needs:
- Collects detailed information through targeted surveys
- Identifies specific interests, needs, and potential contributions
- Maps skills, experiences, and areas of expertise
- Maintains privacy and data security compliance

### BQM Engagement
Maintains ongoing communication with Black queer men members to keep them involved:
- Delivers personalized email sequences tailored to BQM members
- Provides relevant content and opportunities specific to Black queer men
- Encourages participation in BQM-focused events and initiatives
- Solicits feedback and input to improve the BQM experience

### BQM Retention
Encourages continued participation and prevents disengagement of Black queer men members:
- Identifies at-risk BQM members showing signs of disengagement
- Implements targeted re-engagement strategies
- Creates pathways for increasing involvement in leadership
- Develops peer support mechanisms for sustained engagement

### BQM Analytics
Provides insights into the Black queer men membership base and program effectiveness:
- Tracks key metrics on registration, engagement, and retention
- Identifies trends and patterns in BQM member behavior
- Measures the effectiveness of BQM-specific engagement strategies
- Informs decisions about program improvements for Black queer men

## BQM Focus

While the system tracks information about the broader community network, its primary focus is on Black queer men (BQM) members:

- **Core BQM Members**: Individual Black LGBTQ+ men who are the primary focus of BLKOUT's mission
- **BQM Leaders**: Black queer men who take on leadership roles within the community
- **BQM Mentors**: Experienced Black queer men who provide guidance to newer members
- **BQM Specialists**: Black queer men with specific skills or expertise to share

## BQM Onboarding Flow

1. Black queer man signs up through a dedicated BQM web form
2. System verifies eligibility for BQM membership
3. System sends a welcome email (6-hour delay)
4. System sends the BQM-specific survey
5. If no response, system sends a reminder after 3 days
6. Upon survey completion, member is added to the BQM drip campaign
7. Member receives personalized recommendations based on profile

## Setup and Configuration

1. Configure SMTP settings in the `.env` file
2. Set up survey links in `blkout_nxt_config.json`
3. Configure webhook endpoints for form providers
4. Set up Google Sheets integration for data storage

## Usage

The system processes new signups automatically through webhook endpoints, but can also be manually triggered for specific members.

## Dependencies

- n8n for workflow automation
- Tally for form creation and submission
- Google Sheets for data storage
- SMTP server for email sending
