# IAM Lab 1 – Active Directory User Provisioning

## Overview
This lab demonstrates the fundamentals of user provisioning within Identity and Access Management (IAM). I manually created users, enriched their attributes, created a security group, assigned access through group membership, and verified the results in Active Directory.

## Skills Demonstrated
- Active Directory administration  
- Identity lifecycle concepts  
- User provisioning  
- Attribute enrichment  
- Group management  
- RBAC fundamentals  
- Organizational Unit (OU) design  

## Lab Steps
1. Provisioned two new users  
2. Enriched user attributes (Department, Title)  
3. Created a security group  
4. Added users to the group  
5. Retrieved the group and verified user membership and attributes  

## Files Included
- **create-users.ps1** – Creates the two users  
- **set-user-attributes.ps1** – Enriches user attributes (Department, Title)  
- **create-group.ps1** – Creates the security group  
- **add-users-to-group.ps1** – Adds the users to the group  
- **get-group-members.ps1** – Retrieves the group and displays user attributes  

## Screenshots
- Verification of user creation in Active Directory Users and Computers (ADUC) GUI  

## Lessons Learned
- How identity data flows into Active Directory  
- How RBAC is implemented using security groups  
- How OUs help organize and manage identities  
- How manual provisioning works before automation  
