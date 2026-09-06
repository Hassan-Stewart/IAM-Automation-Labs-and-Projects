# IAM Lab 5 — API Response Validation

## Overview
IAM Lab 5 focuses on validating API responses during identity automation workflows.
This lab builds on the previous API payload and identity modeling labs by introducing structured response handling, JSON parsing, and status code verification. These skills are essential for building reliable IAM automation in environments such as Okta, Entra ID, AWS IAM, and custom identity platforms.

## Objectives
- Validate API responses using status codes  
- Parse JSON response bodies  
- Extract key identity attributes from API output  
- Handle success, failure, and unexpected responses  
- Produce clean, readable output for logging and audit purposes  

## Key Concepts
- **HTTP Status Codes:** 200, 201, 400, 401, 404  
- **JSON Parsing**  
- **API Response Handling**  
- **IAM Automation Reliability**  
- **Error Messaging & Logging**  

## What This Lab Demonstrates
This lab simulates how IAM automation interacts with provisioning APIs.
You will validate whether a user creation request succeeded, failed, or returned unexpected data.
This mirrors real-world IAM workflows such as:

- Okta / Entra ID SCIM provisioning  
- AWS IAM role/user automation  
- Identity lifecycle API integrations  
- Access governance automation  

## Files Included
- `lab5_api_error_handling.py`
- `lab5 screenshot`
