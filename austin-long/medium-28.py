# Programming Competition File
# Programmer: Austin Long
# Challenge 28

import unittest


def pascals_triangle(n: int):
    result: list[list[int]] = []

    for i in range(n):
        if i == 0:
            result.append([1])
            continue
        partial_result = []
        prev_row = result[-1]
        for i2 in range(i+1):
            if i2 == 0 or i2 >= len(prev_row):
                partial_result.append(1)
                continue
            partial_result.append(prev_row[i2 - 1] + prev_row[i2])
        result.append(partial_result)

    return result

class TestChallenge(unittest.TestCase):
    def test_challenge(self):
        self.assertEqual(pascals_triangle(5),
            [
                [1],  
                [1, 1],  
                [1, 2, 1],  
                [1, 3, 3, 1],  
                [1, 4, 6, 4, 1]
            ]
         )


if __name__ == "__main__":
    unittest.main()
