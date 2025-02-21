# Programming Competition File
# Programmer: Austin Long
# Challenge 37

import unittest


# I did mine so if there are duplicates, the duplicates are counted as one. Removing "set" does the opposite behavior
def kth_largest_elem(the_arr, k):
    sorted_arr = [x for x in set(the_arr)]
    sorted_arr.sort()
    return sorted_arr[-k]

class TestChallenge(unittest.TestCase):
    def test_challenge(self):
        self.assertEqual(kth_largest_elem([3,2,1,5,6,4], 2), 5)
        self.assertEqual(kth_largest_elem([3,6,1,5,6,4], 2), 5)


if __name__ == "__main__":
    unittest.main()
