from lab3_identity_objects import users
import json
import requests

users_payload = {
    "users": users
}

payload_json = json.dumps(users_payload, indent = 4)
print("Formatted JSON Payload")
print(payload_json)

api_url = "https://example.com/api/users"

response = requests.post(
    api_url,
    headers={"Content-Type": "application/json"},
    data=payload_json
)

print("Status Code:", response.status_code)
print("Response Body:", response.text)

try:
    data = response.json()
    print("Parsed JSON Response.")
    print(json.dumps(data, indent = 4))
except:
    print("Response is not valid JSON.")
    data = {}

if response.status_code == 200: 
    print("Success: Users processed correctly.")
elif response.status_code == 201:
    print("Users created.")
elif response.status_code == 400:
    print("Bad Request: Check your payload.")
elif response.status_code == 401:
    print("Unauthorized: Check your token.")
elif response.status_code == 404:
    print("Endpoint not found")
else:
    print("Unexpected status code received")
