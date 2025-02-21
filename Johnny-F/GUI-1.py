# Johnathan Fester GUI 1

import tkinter as tk

class Gui:
    def __init__(self):

        self.main_window = tk.Tk()
        self.frame = tk.Frame(self.main_window)
        self.clickme = tk.Button(self.frame, text="Click Me!", command=self.change_button)
        self.clickme.pack(side='top')
        self.frame.pack()

        tk.mainloop()

    def change_button(self):
        self.clickme["text"] = "Button Clicked!"

if __name__ == "__main__":
    Gui()