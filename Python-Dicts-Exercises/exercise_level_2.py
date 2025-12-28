contacts = {
    "alice": {"email": "alice@work.com", "phone": "555-1234", "active": True},
    "bob": {"email": "bob@gmail.com", "phone": None, "active": False},
    "charlie": {"email": "charlie@school.edu", "phone": "555-9999"}
    # Note: charlie has no "active" key , we should handle this safely
}

for key,value in contacts.items() :
    new_key = key.strip().lower()
    contacts[new_key] = value
print(contacts)

for key,value in contacts.items() :
    
    if key in contacts and "active" not in contacts[key] :
      contacts["charlie"]["active"] = True
    
print(contacts)