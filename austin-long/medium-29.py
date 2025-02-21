# Programming Competition File
# Programmer: Austin Long
# Challenge 29

import unittest

PAREN_MAPPINGS = {
    "(": ")",
    "[": "]",
    "{": "}",
}

def balanced_parens(the_str):
    paren_stack = []

    for ch in the_str:
        if ch in PAREN_MAPPINGS.keys():
            paren_stack.append(PAREN_MAPPINGS[ch])
        elif ch in PAREN_MAPPINGS.values():
            if paren_stack.pop() != ch:
                return False

    if len(paren_stack):
        return False
    return True

class TestChallenge(unittest.TestCase):
    def test_challenge(self):
        self.assertTrue(balanced_parens("({[()]})"))
        self.assertFalse(balanced_parens("({[)]}"))


if __name__ == "__main__":
    unittest.main()
