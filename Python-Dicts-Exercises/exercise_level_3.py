# messy dict (some missing keys, inconsistent casing)
raw_contacts = {
    "Alice Smith ": {"email": "alice@work.com", "phone": "555-1234", "active": True},
    "bob": {"email": "bob@gmail.com"},
    "Charlie": {"email": "charlie@school.edu", "phone": "555-9999"}
}

# Tasks:
# 1. Normalize all keys: lowercase + strip spaces (create new dict)
# 2. For every contact, use .setdefault() to add "active": True if missing
# 3. Add a new contact "yourname" (use your real or fake name) with email and phone
# 4. Flatten all contacts so each person has only their email at top level
#    Final flat dict: {'alice smith': 'alice@work.com', 'bob': '...', ...}
# 5. Print a nice report:
#    - Number of active contacts
#    - List of all emails (formatted nicely)
#    - Total contacts after flattening

#1 

cleaned_contacts = {}
for name, info in raw_contacts.items():
    new_name = name.strip().lower()
    cleaned_contacts[new_name] = info
#2

for name, info in cleaned_contacts.items():
    info.setdefault("active", True)
#3

cleaned_contacts["yourname"] = {"email": "yourname@example.com", "phone": "555-0000"}

#4

nested_emails = {}
for name, info in cleaned_contacts.items():
    nested_emails[name] = info["email"]
    
#5
active_count = 0
for info in cleaned_contacts.values():
    if info["active"]:
        active_count += 1

print(f"Number of active contacts: {active_count}")
print("List of all emails:")
for email in nested_emails.values():
    print(f" - {email}")
print(f"Total contacts after flattening: {len(nested_emails)}") 
