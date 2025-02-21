# Andrew Hayes python program 2025 
from tkinter import *
from tkinter.ttk import *

# importing strftime function to
# retrieve system's time
from time import strftime

# creating tkinter window
root = Tk()
root.title('Clock')

# display time on the label

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)
    


#UNW colors for the clock
lbl = Label(root, font=('Sans Serif', 40, 'bold'),
            background='purple',
            foreground='yellow')

#centering the clock
lbl.pack(anchor='center')
time()

mainloop()