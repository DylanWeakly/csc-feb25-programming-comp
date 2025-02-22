# Programming Competition File
# Programmer: Austin Long
# Challenge 31

import unittest

def num_digits(num):
    counter = 0
    while (10 ** counter) <= num:
        counter += 1
    return counter


def reverse_integer(num):
    if num == 0:
        return 0

    negative = num < 0

    num = abs(num)

    digit = 10

    counter = 0
    num_dg = num_digits(num)

    result = 0
    
    while (digit ** counter) < num:
        digit_at_counter_pre = (num // (digit ** counter))
        digit_at_counter = digit_at_counter_pre % digit
        multiplied =  digit_at_counter * (digit ** (num_dg - counter - 1))
        result += multiplied
    
        counter += 1

    if negative:
        result = -result
    return result

class TestChallenge(unittest.TestCase):
    def test_num_digits(self):
        self.assertEqual(num_digits(0), 0)
        self.assertEqual(num_digits(1), 1)
        self.assertEqual(num_digits(11), 2)
        self.assertEqual(num_digits(3021), 4)
    
    def test_challenge(self):
        self.assertEqual(reverse_integer(9284), 4829)
        self.assertEqual(reverse_integer(1234), 4321)
        self.assertEqual(reverse_integer(-456), -654)
        self.assertEqual(reverse_integer(0), 0)


if __name__ == "__main__":
    unittest.main()
