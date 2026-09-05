<#
Script: 01-users-attributes.ps1
Purpose: Sets attributes for two users in Lab 1 using PowerShell.
#>

#Enriching attributes for the two users created
Set-ADUser -Identity "Hassan Stewart" -Department "Retail Clothing" -Title "Co-Founder"
Set-ADUser -Identity "Kharii Easley" -Department "Retail  Clothing" -Title "Co-Founder"
