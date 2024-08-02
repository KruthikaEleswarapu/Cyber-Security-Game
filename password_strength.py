import re

def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    return True

password = input("Enter a password: ")
if is_strong_password(password):
    print("Strong password!")
else:
    print("Weak password. Please use at least 8 characters, including uppercase, lowercase, and numbers.")
