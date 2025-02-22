# Programming Competition File
# Programmer: Austin Long
# Challenge 18

import unittest


def second_smallest(the_list):
    smallest_val = None
    second_smallest_val = None

    for el in the_list:
        if smallest_val == None or el <= smallest_val:
            smallest_val = el
        elif  second_smallest_val == None or el <= second_smallest_val:
            second_smallest_val = el

    if smallest_val == None:
        return None
    if second_smallest_val == None:
        return smallest_val
    return second_smallest_val
    

class TestChallenge(unittest.TestCase):
    def test_challenge(self):
        self.assertEqual(second_smallest([1, 3, 4, 5, 2]), 2)
        self.assertEqual(second_smallest([3, 1, 4, 2, 5]), 2)


if __name__ == "__main__":
    unittest.main()
