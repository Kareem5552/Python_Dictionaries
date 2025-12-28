contacts = {
    "alice": {"email": "alice@work.com", "phone": "555-1234"},
    "bob": {"email": "bob@gmail.com"}
}

# 1. Use .setdefault() to safely add "active": True to every contact
for contact_info in contacts.values():
    contact_info.setdefault("active", True)

# 2. Update Bob's email safely
contacts["bob"]["email"] = "new.bob@gmail.com"  # safe because "bob" exists

# 3. Add new contact "diana" (using .setdefault() for extra safety)
diana_data = {"email": "diana@home.com", "phone": "555-7777", "active": True}
contacts.setdefault("diana", diana_data)

# 4. Print all contacts in nice aligned format
print("\nAll Contacts:")
print("-" * 70)
for name, info in contacts.items():
    email = info.get("email", "N/A")
    phone = info.get("phone", "N/A")
    active = info.get("active", "N/A")
    print(f"{name.capitalize():<10} | Email: {email:<25} | Phone: {phone:<15} | Active: {active}")
print("-" * 70)