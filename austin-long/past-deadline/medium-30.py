# Programming Competition File
# Programmer: Austin Long
# Challenge 30

import unittest


def next_greater_elems(the_arr: list[int]):
    result: list[int] = []
    for i in range(len(the_arr)):
        num = the_arr[i]
        next_greater_num = -1
        for i in range(i+1, len(the_arr)):
            if the_arr[i] > num:
                next_greater_num = the_arr[i]
                break
        result.append(next_greater_num)


    return result

class TestChallenge(unittest.TestCase):
    def test_challenge(self):
        self.assertEqual(next_greater_elems([4,5,2,10]), [5, 10, 10, -1])


if __name__ == "__main__":
    unittest.main()
