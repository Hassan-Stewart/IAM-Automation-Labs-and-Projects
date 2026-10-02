# Project 1 - Bulk User Provisioning Automation

## Real-World Application

This workflow mirrors bulk provisioning patterns used in enterprise IAM platforms (e.g., CyberArk, Microsoft Entra ID, Okta), where new hires, contractors, or service accounts are programmatically onboarded and their provisioning status tracked for auditing and compliance.

## Objective
 
This project simulates a real-world IAM provisioning workflow by processing multiple identity records, converting them into JSON payloads, submitting them through an API, validating responses, handling errors, and generating a provisioning summary.

## Note 

This project uses httpbin.org as a mock API endpoint to safely simulate provisioning calls without requiring live credentials or production systems.
 
## Technologies Used
 
- Python
- JSON
- Requests Library
- REST APIs
 
## Skills Demonstrated
 
- Identity Object Modeling
- JSON Payload Construction
- API Submission
- Response Validation
- Error Handling
- Bulk User Provisioning
- Automation Workflow Development
 
## Workflow
 
1. Import identity objects
2. Convert users into JSON payloads
3. Submit payloads to an API endpoint
4. Validate API responses
5. Track successful and failed provisioning attempts
6. Generate a final provisioning summary
 
## Project Outcome
 
Successfully provisioned multiple user records while tracking successes and failures through automated response validation and error handling logic.
