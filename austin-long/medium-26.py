# Programming Competition File
# Programmer: Austin Long
# Challenge 26

import unittest


def bin_convert(num):
    if num == 0:
        return "0"

    result = ""

    digit = 2
    counter = 0
    while (digit ** counter) <= num:
        bitwise_and = num & (digit ** counter)
        if bitwise_and > 0:
            result = "1" + result
        else:
            result = "0" + result
        counter += 1

    return result
    

class TestChallenge(unittest.TestCase):
    def test_challenge(self):
        self.assertEqual(bin_convert(10), "1010")
        self.assertEqual(bin_convert(255), "11111111")


if __name__ == "__main__":
    unittest.main()
