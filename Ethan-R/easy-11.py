"""
11. Capitalize First and Last Letter (15 pts)
Write a function that capitalizes only the first and last letter of each word in a sentence.
Example: "hello world" → "HellO WorlD"
"""

def cap_ends(s):
    s = s[0].capitalize() + s[1:]
    s = s[:len(s)-1] + s[len(s)-1].capitalize()
    return s


print(cap_ends("hello world"))