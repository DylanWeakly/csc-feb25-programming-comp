import tkinter as tk
import random
i = 0
# how many times the button was pressed
def button_clicked():


    print("Button clicked!" + str(i))


def verse_label(random_verse):
    verse_label = tk.Label(root, text=random_verse, font=("Arial", 18))
    verse_label.pack(pady=20)

def random_verse():
    verses = [
        "In my distress I called upon the Lord, and cried unto my God: he heard my voice out of his temple, and my cry came before him, even into his ears.",
        "Death and life are in the power of the tongue: and they that love it shall eat the fruit thereof.",
        "Thy word is a lamp unto my feet, and a light unto my path.",
        "He that loveth silver shall not be satisfied with silver; nor he that loveth abundance with increase: this is also vanity."
    ]
    return random.choice(verses)

root = tk.Tk()


Bible_Verse = tk.Label(root, text="Bible Verse Generator", font=("Arial", 24))
Bible_Verse.pack(padx=30, pady=30)

# it works but it doesn't clear the previous verse
def on_button_click():
    verse_label(random_verse())
    global i
    i += 1

button = tk.Button(root, text="Generate Verse", command=on_button_click)
button.pack(pady=20)




root.mainloop()