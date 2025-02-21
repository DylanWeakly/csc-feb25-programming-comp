"""
#### 1. Reverse Words and Change Case (10 pts)
   - Write a function that reverses the order of words in a sentence and toggles the case of each letter.
   - Example: `"Hello World" → "wORLD hELLO"`
"""

def reverse(s):
    s = s.swapcase()
    s = s.split()
    s.reverse()
    s = " ".join(str(i) for i in s)
    return s


def main():
    print(reverse("Hello World"))
    while True:
        print(reverse(input("Reverse :")))

if __name__ == '__main__':
    main()