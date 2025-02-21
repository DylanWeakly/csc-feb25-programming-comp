# password strength checker Andrew Hayes 2/21/2025
# I found the majority of this code on a website called https://www.w3resource.com/python-exercises/cybersecurity/python-cybersecurity-exercise-3.php. I made some minor changes to the code to make it work for me.
import re

def validate_password(password):
    # Check if the password has at least 8 characters
    if len(password) < 10:
        return False
    
    # Check if the password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    
    # Check if the password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    
    # Check if the password contains at least one digit
    if not re.search(r'\d', password):
        return False
    
    # Check if the password contains at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    # If all the conditions are met, the password is valid
    return True

# user input statment for the password
password = input("Input your password of a length of ten: ")
is_valid = validate_password(password)

# checks if the password is valid or not
if is_valid:
    print(" your password is valid.")
else:
    print("Your password does not meet requirements.")