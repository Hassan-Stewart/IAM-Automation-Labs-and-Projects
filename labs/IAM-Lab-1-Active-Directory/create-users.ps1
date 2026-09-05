<#
Script: 01-create-users.ps1
Purpose: Creates two users for Lab 1 using PowerShell.
#>

#Creating two new users
New-ADUser -Name "Hassan Stewart" -SamAccountName "Hassan Stewart" -AccountPassword(Read-Host -AsSecureString "Enter a Pasword") -Enabled $True
New-ADUser -Name "Kharii Easley" -SamAccountName "Kharii Easley" -AccountPassword(Read-Host -AsSecureString "Enter a Password") -Enabled $True
