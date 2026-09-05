users = [
    {
        "username": "hstewart",
        "first_name": "Hassan",
        "last_name": "Stewart",
        "department": "IT",
        "role": "IAM Engineer",
        "enabled": True,
        "mfa_enabled": True,
    },
    {
        "username": "mandrews",
        "first_name": "Melissa",
        "last_name": "Andrews",
        "department": "Finance",
        "role": "Analyst",
        "enabled": True,
        "mfa_enabled": True,
    },
    {
        "username": "awilliams",
        "first_name": "Adrien",
        "last_name": "Williams",
        "department": "Marketing",
        "role": "Manager",
        "enabled": True,
        "mfa_enabled": True,
    },
    {
        "username": "lsalters",
        "first_name": "Lisa",
        "last_name": "Salters",
        "department": "Operations",
        "role": "Specialist",
        "enabled": True,
        "mfa_enabled": True,
    },

]

for user in users:
    print("-----USER RECORDS-----")
    print(f"UserName: {user['username']}")
    print(f"Name: {user['first_name']} {user['last_name']}")
    print(f"Department: {user['department']}")
    print(f"Role: {user['role']}")
    print(f"Enabled: {user['enabled']}")
    print(f"Mfa_Enabled: {user['mfa_enabled']}")
    print()
