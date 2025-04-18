# This script creates symbolic links for backward compatibility
# Run this script with administrator privileges

# Create symlink from old onboarding directory to new bqm-members directory
New-Item -ItemType SymbolicLink -Path .\onboarding -Target .\bqm-members -Force

# Create symlink from old rewards directory to new network-recognition directory
New-Item -ItemType SymbolicLink -Path .\rewards -Target .\network-recognition -Force

Write-Host "Symbolic links created successfully for backward compatibility."
