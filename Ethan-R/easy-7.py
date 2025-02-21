"""
7. Alternating Case String (15 pts)
Write a function that converts a string to alternating uppercase and lowercase characters.
Example: "hello" → "HeLlO"
"""

def alternate_case(s, up = False):
    s2 = ''
    for i in s:
        up = not up
        if up:
            s2 += i.upper()
        else:
            s2 += i.lower()

    return s2

print(alternate_case("hello world"))
