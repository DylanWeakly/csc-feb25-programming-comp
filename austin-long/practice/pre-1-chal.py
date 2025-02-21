# Programming Competition File
# Programmer: Austin Long

import unittest

def palindrome(item):
    for ch1, ch2 in zip(item, reversed(item)):
        if ch1 != ch2:
            return False
    
    return True

class TestChallenge(unittest.TestCase):
    def test_challenge(self):
        self.assertTrue(palindrome("TACOCAT"))
        self.assertFalse(palindrome("ABCDEF"))


if __name__ == "__main__":
    unittest.main()
