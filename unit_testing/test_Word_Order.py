import unittest
from collections import OrderedDict

def word_order(words):
    d = OrderedDict()
    for word in words:
        d[word] = d.get(word, 0) + 1
    return len(d), list(d.values())


class TestWordOrder(unittest.TestCase):

    def test_case1(self):
        words = ["bcdef", "abcdefg", "bcde", "bcdef"]
        self.assertEqual(word_order(words), (3, [2, 1, 1]))

    def test_case2(self):
        words = ["apple", "banana", "apple"]
        self.assertEqual(word_order(words), (2, [2, 1]))

    def test_case3(self):
        words = ["one", "two", "three"]
        self.assertEqual(word_order(words), (3, [1, 1, 1]))


if __name__ == "__main__":
    unittest.main()
