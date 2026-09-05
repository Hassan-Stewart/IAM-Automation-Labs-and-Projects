from lab3_identity_objects import users
import json

users_payload = {
    "users": users
}

print(json.dumps(users_payload, indent=4))
