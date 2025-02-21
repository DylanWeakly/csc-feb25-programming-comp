# Programming Competition File
# Programmer: Austin Long
# Challenge 35

import unittest


def decode_run_lenth(the_str):
    need_count = True
    count = -1
    result = ""
    for ch in the_str:
        if need_count:
            count = int(ch)
            need_count = False
        else:
            result += ch * count
            need_count = True

    if not need_count:
        raise ValueError("Run Length string cannot end with a count")

    return result
            

class TestChallenge(unittest.TestCase):
    def test_challenge(self):
        self.assertEqual(decode_run_lenth("3a2b4c"), "aaabbcccc")
        self.assertEqual(decode_run_lenth("2b5c44"), "bbccccc4444")


if __name__ == "__main__":
    unittest.main()
