# Programming Competition File
# Programmer: Austin Long
# Challenge 8

import unittest


def max_diff(elements):
    return max(elements) - min(elements)

class TestChallenge(unittest.TestCase):
    def test_challenge(self):
        self.assertEqual(max_diff([10,3,5,20]), 17)


if __name__ == "__main__":
    unittest.main()
