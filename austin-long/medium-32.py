# Programming Competition File
# Programmer: Austin Long
# Challenge 32

import unittest


def string_compress(the_str):
    last_ch = ""
    last_ch_count = 0
    result = ""

    for ch in the_str:
        if ch == last_ch:
            last_ch_count += 1
        else:
            if last_ch_count > 0:
                result += last_ch + str(last_ch_count)
            last_ch = ch
            last_ch_count = 1
    
    result += last_ch + str(last_ch_count) if last_ch_count > 0 else ""
    return result


class TestChallenge(unittest.TestCase):
    def test_challenge(self):
        self.assertEqual(string_compress("aabcccccaaa"), "a2b1c5a3")
        self.assertEqual(string_compress(""), "")
        self.assertEqual(string_compress("ababbbbbcccxxxxxccaaab"), "a1b1a1b5c3x5c2a3b1")



if __name__ == "__main__":
    unittest.main()
