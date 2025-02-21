"""
10. Product of List Elements (15 pts)
Write a function that calculates the product of all elements in a list.
Example: [2, 3, 4] → 24
"""

def product(l):
    f = 1
    for i in l:
        f *= i
    return f

print(product([2, 3, 4]))