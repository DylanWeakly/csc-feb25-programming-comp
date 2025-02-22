# Programming Competition File
# Programmer: Austin Long

import unittest

def rotate_matrix(matrix: list[list[int]]):
    rows = len( matrix[0] )
    cols = len(matrix)
    new_matrix = [[None] * cols for x in range(rows)]
    for ci in range(len(matrix)):
        for ri in range(len(matrix[ci])):
            new_matrix[( ri   )][-( ci + 1 )] = matrix[ci][ri]
    return new_matrix

class TestChallenge(unittest.TestCase):
    def test_challenge(self):
        self.assertEqual(rotate_matrix([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]), [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3],
        ])


if __name__ == "__main__":
    unittest.main()
