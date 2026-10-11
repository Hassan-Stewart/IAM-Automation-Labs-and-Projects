from lab3_identity_objects import users
import logging
import json
import requests

logging.basicConfig(
    filename = "iam_log.txt",
    level = logging.INFO,
    format = "%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("Provisioning process started")

for user in users:
    logging.info(f"User loaded: {user['username']} | Department: {user['department']} | Role: {user['role']}")

    if not user["mfa_enabled"]:
        logging.warning(f"MFA not enabled for user = {user['username']}")

users_payload = {
    "users": users
}

payload_json = json.dumps(users_payload, indent = 4)
logging.info(f"Payload is built for {len(users)} users")

api_url = "https://httpbin.org/post"

response = None

try:
    response = requests.post(
        api_url,
        headers = {"Content-Type": "application/json"},
        data = payload_json,
        timeout = 10
    )

except requests.exceptions.Timeout:
    logging.info("Connection timed out")

except requests.exceptions.ConnectionError:
    logging.info("Could not connect to the API")

except requests.exceptions.RequestException as e:
    logging.info(f"Request failed: {e}")

if response is not None:
    if response.status_code == 200:
        logging.info("Success: Users processed correctly")

    elif response.status_code == 201:
        logging.info("Success: Users created successfully")

    elif response.status_code == 400:
        logging.error("Bad Request: Check your payload")

    elif response.status_code == 401:
        logging.error("Unauthorized: Check your token")

    elif response.status_code == 403:
        logging.error("Forbidden: You do not have permission")

    elif response.status_code == 404:
        logging.error("Endpoint not found")

    elif response.status_code == 500:
        logging.error("Server Error: Try again later")

    else:
        logging.error(f"Unexpected status code received {response.status_code}")

logging.info("Provisioning process finished")
