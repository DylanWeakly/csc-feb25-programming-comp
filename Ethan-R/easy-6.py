"""
6. Count Unique Elements (15 pts)
Write a function that counts the number of unique elements in a list.
Example: [1, 2, 2, 3, 4, 4, 5] → 5
"""

def unique(l):
    return len(set(l))

print(unique([1, 2, 2, 3, 4, 4, 5]))