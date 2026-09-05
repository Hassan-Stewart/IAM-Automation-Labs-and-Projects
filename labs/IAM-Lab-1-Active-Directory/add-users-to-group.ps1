<#
Script: 01-add-users-to-group.ps1
Purpose: Adds users to the "Retail Clothing" group for Lab 1 using PowerShell.
#>

#Adding group members to the "Retail Clothing" group
Add-ADGroupMember -Identity "Retail Clothing" -Members "Hassan Stewart", "Kharii Easley"
