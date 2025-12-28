# Starting messy data (with duplicates after normalization + conflicts)
raw_contacts = {
    "Alice Smith ": {"email": "alice@work.com", "phone": "555-1234", "active": True},
    "alice smith": {"email": "alice.private@email.com", "notes": "VIP client"},  # duplicate after lower+strip!
    "Bob": {"email": "bob@gmail.com"},
    "Charlie Brown": {"email": "charlie@school.edu", "phone": "555-9999"},
    "charlie brown ": {"email": "charlie.new@school.edu"}  # another duplicate case
}

# Tasks (harder version):
# 1. Normalize keys: lowercase + strip spaces
#    → If duplicate keys appear after normalization → merge them (keep the most complete info)
# 2. For every contact, use .setdefault() to add "active": True if missing
# 3. Add a new contact "yourname" (use real or fake name) with email, phone, and "active": True
# 4. Flatten all contacts so each person has only their email at top level
#    → If "email" conflicts during merge → keep the first one, add the second as "email_alt"
#    → Final flat dict example: {'alice smith': 'alice@work.com', 'email_alt': 'alice.private@email.com', ...}
# 5. Print a beautiful report:
#    - Total unique contacts after normalization
#    - Number of active contacts
#    - List of all emails (with alt if any) in nice table format
#    - Bonus: count how many had conflicts during normalization/flattening

# Your turn — try to build this step by step!

#1

#2

#3

#4

#5
# Starting messy data (with duplicates after normalization + conflicts)
raw_contacts = {
    "Alice Smith ": {"email": "alice@work.com", "phone": "555-1234", "active": True},
    "alice smith": {"email": "alice.private@email.com", "notes": "VIP client"},  # duplicate after lower+strip!
    "Bob": {"email": "bob@gmail.com"},
    "Charlie Brown": {"email": "charlie@school.edu", "phone": "555-9999"},
    "charlie brown ": {"email": "charlie.new@school.edu"}  # another duplicate case
}

# Tasks (harder version):
# 1. Normalize keys: lowercase + strip spaces
#    → If duplicate keys appear after normalization → merge them (keep the most complete info)
# 2. For every contact, use .setdefault() to add "active": True if missing
# 3. Add a new contact "yourname" (use real or fake name) with email, phone, and "active": True
# 4. Flatten all contacts so each person has only their email at top level
#    → If "email" conflicts during merge → keep the first one, add the second as "email_alt"
#    → Final flat dict example: {'alice smith': 'alice@work.com', 'email_alt': 'alice.private@email.com', ...}
# 5. Print a beautiful report:
#    - Total unique contacts after normalization
#    - Number of active contacts
#    - List of all emails (with alt if any) in nice table format
#    - Bonus: count how many had conflicts during normalization/flattening