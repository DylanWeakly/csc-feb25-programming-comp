"""
13. Sum of Odd Numbers (20 pts)
Write a function that returns the sum of all odd numbers in a given list.
Example: [1, 2, 3, 4, 5] → 9
"""

def sum_odd(l):
    s = 0
    for i in l:
        if (i % 2) != 0:
            s += i
    return s


print(sum_odd([1, 2, 3, 4, 5]))