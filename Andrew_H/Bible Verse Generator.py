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
        "The Lord is my shepherd; I shall not want.",
        "The fear of the Lord is the beginning of knowledge: but fools despise wisdom and instruction.",
        "For the Lord giveth wisdom: out of his mouth cometh knowledge and understanding.",
        "The Lord is nigh unto all them that call upon him, to all that call upon him in truth.",
        " The Lord is my light and my salvation; whom shall I fear? the Lord is the strength of my life; of whom shall I be afraid?",
        "The Lord is my strength and my shield; my heart trusted in him, and I am helped: therefore my heart greatly rejoiceth; and with my song will I praise him.",
        "The Lord is on my side; I will not fear",
        "The Lord is my rock, and my fortress, and my deliverer; my God, my strength, in whom I will trust; my buckler, and the horn of my salvation, and my high tower.",
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