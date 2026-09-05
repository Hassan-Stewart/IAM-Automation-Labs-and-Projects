<#
Script: 01-get-group-members.ps1
Purpose: Gets the members of the "Retail Clothing" group for Lab 1 using PowerShell.
#>

#Getting user 1 with attributes
Get-ADUser "Hassan Stewart" -Department, Title

#Getting user 2 with attributes
Get-ADUser "Kharii Easley" -Department, Title
