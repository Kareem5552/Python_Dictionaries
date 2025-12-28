"""
Exercise 1 – Safe Nested Contact Updater

Starting data:
contacts = {
    "alice": {"email": "alice@work.com", "phone": "555-1234"},
    "bob": {"email": "bob@gmail.com"}
}

Tasks:
1. Use .setdefault() to safely add "active": True to every contact (even if missing)
2. Update Bob's email to "new.bob@gmail.com" using safe nested access
3. Add a new contact "diana" with email "diana@home.com" and phone "555-7777" 
   (use .setdefault() for the whole entry if you want to be extra safe)
4. Print all contacts in this nice format (use formatting for alignment):
   Diana     | Email: diana@home.com     | Phone: 555-7777     | Active: True
"""

# Solution
contacts = {
    "alice": {"email": "alice@work.com", "phone": "555-1234"},
    "bob": {"email": "bob@gmail.com"}
}

# 1. Add "active": True safely
for info in contacts.values():
    info.setdefault("active", True)

# 2. Update Bob safely
if "bob" in contacts:
    contacts["bob"]["email"] = "new.bob@gmail.com"

# 3. Add "diana" safely
diana_data = {"email": "diana@home.com", "phone": "555-7777", "active": True}
contacts.setdefault("diana", diana_data)

# 4. Print formatted report
print("\nAll Contacts:")
print("-" * 70)
for name, info in contacts.items():
    email = info.get("email", "N/A")
    phone = info.get("phone", "N/A")
    active = info.get("active", "N/A")
    print(f"{name.capitalize():<10} | Email: {email:<25} | Phone: {phone:<15} | Active: {active}")
print("-" * 70)
