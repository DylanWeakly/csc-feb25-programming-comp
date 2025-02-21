"""
5. Remove Vowels from String (10 pts)
Write a function that removes all vowels from a given string.
Example: "hello world" → "hll wrld"
"""

def vowel_strip(s, is_y_vowel = False):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if is_y_vowel:
        vowels.append('y')
        vowels.append('Y')
    for i in vowels:
        s = s.replace(i,'')
    return s


print(vowel_strip("hello world"))