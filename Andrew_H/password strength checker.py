# password strength checker Andrew Hayes 2/21/2025
# I found the majority of this code on a website called https://www.w3resource.com/python-exercises/cybersecurity/python-cybersecurity-exercise-3.php. I made some minor changes to the code to make it work for me.
import re
import tkinter as tk
from tkinter import messagebox

def validate_password(password):
    # Check if the password has at least 10 characters
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

def check_password():
    password = entry.get()
    is_valid = validate_password(password)
    if is_valid:
        messagebox.showinfo("Result", "Your password is valid.")
    else:
        messagebox.showerror("Result", "Your password does not meet requirements.")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place the widgets
label = tk.Label(root, text="Input your password of a length of ten:")
label.pack(pady=10)

entry = tk.Entry(root, show="*")
entry.pack(pady=10)

button = tk.Button(root, text="Check Password", command=check_password)
button.pack(pady=10)

# Run the application
root.mainloop()