# Programming Competition File
# Programmer: Austin Long
# Challenge 3

import unittest


def challenge_3(str_list: list[str]):
    str_list.sort()
    longest_match = ""
    prev_item = None

    for string in str_list:
        match = ""
        if prev_item != None:
            for c1, c2 in zip(string, prev_item):
                if c1 == c2:
                    match += c1
                else:
                    break;

        if len(match) >= len(longest_match):
            longest_match = match

        prev_item = string

    return longest_match


class TestChallenge(unittest.TestCase):
    def test_challenge(self):
        self.assertEqual(challenge_3([
            "ABC",
            "DEF",
            "ABCDEF",
            "GHIJ",
            "GHIJABCD",
        ]),
            "GHIJ"
        )


if __name__ == "__main__":
    unittest.main()
