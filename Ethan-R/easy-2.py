<<<<<<< Updated upstream
=======
"""
2. List Alternator (10 pts)
Write a function that merges two lists by alternating their elements.
Example: [1, 2, 3] and [4, 5, 6] → [1, 4, 2, 5, 3, 6]
"""

def alternator(l1, l2):
    if len(l1)>len(l2):
        length = len(l1)
    else:
        length = len(l2)
    l3 = []
    for i in range(length):
        l3.append(l1[i])
        l3.append(l2[i])
    return l3

def main():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    print(alternator(l1, l2))

if __name__ == '__main__':
    main()

>>>>>>> Stashed changes
