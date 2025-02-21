import tkinter as tk

i = 0

def button_clicked():
    global i
    i += 1

    print("Button clicked!" + str(i))


root = tk.Tk()

# Creating a button with specified options
button = tk.Button(root, 
                   text="Click Me", 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)
if i == 10:
    button["state"] = "disabled"
    print("hurray you pressed the button 10 times")

button.pack(padx=30, pady=30)


root.mainloop()