
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox



def check_pass(text: str):
    long_pass = len(text) > 10
    has_symbol = False
    has_num = False

    for c in text:
        if c in "!@#$%^&*()_+~<>?:":
            has_symbol = True
        
        if c in "1234567890":
            has_num = True
    
    if not long_pass:
        return "Too short"
    elif not has_num:
        return "No numbers"
    elif not has_symbol:
        return "No symbols"
    else:
        return "You have a great password"
    


user_input = simpledialog.askstring(prompt="Enter a password", title='Password')
messagebox.showinfo(title='Password', message=check_pass(user_input))
