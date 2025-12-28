"""
Exercise 4 – Hard: Advanced Cleanup & Report (Capstone)

Starting data (very messy):
raw_contacts = {
    " Alice Smith  ": {"email": "alice@work.com", "phone": "555-1234", "active": True},
    "alice smith": {"email": "alice.private@email.com", "notes": "VIP"},
    "Bob": {"email": "bob@gmail.com"},
    "charlie brown ": {"email": "charlie@school.edu", "phone": "555-9999"},
    "Charlie Brown": {"email": "charlie.new@school.edu"}  # duplicate
}

Tasks:
1. Normalize keys: lowercase + strip spaces
   → If duplicates → merge (prefer existing values, add missing from new)
2. Add "active": True if missing
3. Add new contact "yourname" with email, phone, active=True
4. Flatten to emails only
   → If email conflict → keep first, add second as "email_alt"
5. Print beautiful report:
   - Total unique contacts
   - Number of active
   - List of emails (with alt if any) in table format
   - Bonus: count conflicts
"""

print("Solve this capstone yourself!")
print("Use everything you learned: normalize, merge, setdefault, flatten with alt, formatted print.")
