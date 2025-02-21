"""
4. String Expansion (10 pts)
Write a function that repeats each character in a string n times.
Example: "abc", n=3 → "aaabbbccc"
"""

def expansion(s, n):
    new = ""
    for i in s:
        for j in range(n):
            new += i
    return new

print(expansion("abc",3))