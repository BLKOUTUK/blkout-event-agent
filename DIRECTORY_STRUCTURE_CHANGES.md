# Directory Structure Changes

This document explains the changes made to the directory structure of the BLKOUT Community Ecosystem repository.

## Overview of Changes

The repository has been reorganized to focus on community outcomes rather than technical components. The following changes have been made:

1. **Renamed Directories**:
   - `onboarding/` → `bqm-members/`
   - `rewards/` → `network-recognition/`

2. **Updated Directory Structure**:
   - `events-system/` - Events Calendar system
   - `bqm-members/` - BQM Member Management system
   - `social-media/` - Campaign Communications system
   - `network-recognition/` - Network Recognition system
   - `shared/` - Shared infrastructure components
   - `mcp-server/` - MCP server implementation

## Backward Compatibility

To maintain backward compatibility with external references, symbolic links have been created:

- `onboarding/` → `bqm-members/`
- `rewards/` → `network-recognition/`

To create these symbolic links, run the `create_symlinks.ps1` script with administrator privileges.

## Updated File Locations

### BQM Member Management (formerly Onboarding)

Files related to BQM Member Management have been moved to the `bqm-members/` directory and organized into subdirectories:

- `bqm-members/registration/` - BQM registration processing
- `bqm-members/profiling/surveys/` - BQM survey definitions and processing
- `bqm-members/engagement/email-templates/` - BQM email templates
- `bqm-members/engagement/drip-campaigns/` - BQM email drip campaign workflows
- `bqm-members/retention/` - BQM retention strategies

### Network Recognition (formerly Rewards)

Files related to Network Recognition have been moved to the `network-recognition/` directory and organized into subdirectories:

- `network-recognition/point-system/` - Network contribution tracking
- `network-recognition/achievement-tracking/` - Collaborative achievement tracking
- `network-recognition/redemption/` - Partnership benefits
- `network-recognition/recognition/` - Network spotlight
- `network-recognition/reporting/` - Ecosystem impact reporting

## Key File Migrations

1. **BQM Member Management**:
   - `blkout_nxt_onboarding_workflow.json` → `bqm-members/bqm_member_management_workflow.json`
   - `BLKOUT_NXT_ONBOARDING_GUIDE.md` → `bqm-members/BQM_MEMBER_MANAGEMENT_GUIDE.md`

2. **Network Recognition**:
   - `rewards_schema.json` → `network-recognition/point-system/network_contribution_schema.json`
   - `data/rewards.json` → `network-recognition/point-system/network_contributions.json`

## Updating References

If you encounter references to the old directory structure in your code or documentation, please update them to use the new directory structure. If you cannot update the references (e.g., in external systems), you can use the symbolic links for backward compatibility.

## Rationale for Changes

The directory structure changes were made to:

1. **Focus on Outcomes**: Organize code around community outcomes rather than technical components
2. **Clarify Distinctions**: Make a clearer distinction between BQM Member Management (focused on Black queer men) and Network Recognition (focused on the broader networks and communities)
3. **Improve Maintainability**: Create a more logical and intuitive structure for ongoing development
4. **Enhance Documentation**: Provide clearer documentation about the purpose and relationships of each component
