"""
8. Max Difference in List (15 pts)
Write a function that finds the maximum difference between any two elements in a list.
Example: [10, 3, 5, 20] → 17 (20 - 3)
"""

def max_diff(l):
    return max(l) - min(l)

l = [10, 3, 5, 20]
print(max_diff(l))