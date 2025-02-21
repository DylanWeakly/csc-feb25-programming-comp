# Programming Competition File
# Programmer: Austin Long
# Challenge 10

import unittest


def product_elements(the_arr):
    result = 1
    for elem in the_arr:
        result *= elem
    return result

class TestChallenge(unittest.TestCase):
    def test_challenge(self):
        self.assertEqual(product_elements([2,3,4]), 24)


if __name__ == "__main__":
    unittest.main()
