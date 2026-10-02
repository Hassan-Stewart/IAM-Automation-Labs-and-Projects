from lab3_identity_objects import users
import json
import requests

api_url = "https://httpbin.org/post"

successful_users = 0
unsuccessful_users = 0

for user in users:
    payload_json = json.dumps(user, indent = 4)
    print(f"\nProcessing User: {user['username']}")

    try:
        response = requests.post(
            api_url,
            headers = {"Content-Type": "application/json"},
            data = payload_json
        )

        if response.status_code == 200:
            successful_users += 1
            print("Success: Users processed correctly.")

        elif response.status_code == 201:
            successful_users += 1
            print("Success: Users created correctly.")

        else:
            unsuccessful_users += 1
            print("Provisioning failed")

    except requests.exceptions.RequestException as e:
        unsuccessful_users += 1
        print("Error:", e)

print(f"\nProvisioning Summary")
print("---------------------")
print("Successful Users:", successful_users)
print("Unsuccessful Users:", unsuccessful_users)
