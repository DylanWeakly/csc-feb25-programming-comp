"""
3. Cumulative Sum List (10 pts)
Write a function that returns a list where each element is the cumulative sum of the elements before it.
Example: [1, 2, 3] → [1, 3, 6]
"""

def cumulative_sum(l):
    l2 = []
    s = 0
    for i in l:
        s += i
        l2.append(s)
    return l2

print(cumulative_sum([1, 2, 3, 4, 5, 6]))
