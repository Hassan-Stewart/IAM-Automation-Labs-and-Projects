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

try:
    response = requests.post(
        api_url,
        headers = {"Content-Type": "application/json"},
        data = payload_json,
        timeout = 10
    )

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    try:
        data = response.json()
        print("Parsed JSON Response.")
        print(json.dumps(data, indent = 4))

    except json.JSONDecodeError:
        print("Response is not valid JSON.")
        data = {}

except requests.exceptions.Timeout:
    print("Connection timed out.")

except requests.exceptions.ConnectionError:
    print("Could not connect to the API.")

except requests.exceptions.RequestsExceptions as e:
    print("Request failed: {e}")

if requests.status_code == 200:
    print("Success: Users processed correctly.")

elif requests.status_code == 201:
    print("Success: Users created successfully.")

elif requests.status_code == 400:
    print("Bad Request: Check your payload.")

elif requests.status_code == 401:
    print("Unauthorized: Check your token.")

elif requests.status_code == 403:
    print("Forbidden: You don't have permission.")

elif requests.status_code == 404:
    print("Endpoint not found.")

elif requests.status_code == 500:
    print("Server Error: Try again later.")

else:
    print("Unexpected status code received.")

    if isinstance(response.status_code, int):
        print(f"Final Status Code Confirmed: {response.status_code}")
