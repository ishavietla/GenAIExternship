import string

password = input("Enter password: ")

missing_requirements = []

if len(password) < 8:
    missing_requirements.append("at least 8 characters long")
if not any(c.isupper() for c in password):
    missing_requirements.append("at least one uppercase letter")
if not any(c.islower() for c in password):
    missing_requirements.append("at least one lowercase letter")
if not any(c.isdigit() for c in password):
    missing_requirements.append("at least one digit")
if not any(c in string.punctuation for c in password):
    missing_requirements.append("at least one special character")

if not missing_requirements:
    print("Password is strong!")
    
else:
    print("Your password needs: " + ", ".join(missing_requirements))
    
