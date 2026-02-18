
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

import unittest


class TestMutations(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(
            mutate_string("abracadabra", 5, "k"),
            "abrackdabra"
        )

    def test_first_position(self):
        self.assertEqual(
            mutate_string("hello", 0, "H"),
            "Hello"
        )

    def test_last_position(self):
        self.assertEqual(
            mutate_string("world", 4, "D"),
            "worlD"
        )

    def test_middle(self):
        self.assertEqual(
            mutate_string("python", 2, "X"),
            "pyXhon"
        )


if __name__ == "__main__":
    unittest.main()
