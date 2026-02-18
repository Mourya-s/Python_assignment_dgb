import unittest
from itertools import combinations

def probability_a(arr, k):
    comb = list(combinations(arr, k))
    total = len(comb)

    count = 0
    for c in comb:
        if 'a' in c:
            count += 1

    return round(count / total, 3)


class TestIterables(unittest.TestCase):

    def test_case1(self):
        arr = ['a', 'b', 'c']
        self.assertEqual(probability_a(arr, 2), 0.667)

    def test_case2(self):
        arr = ['a', 'a', 'b']
        self.assertEqual(probability_a(arr, 2), 1.0)

    def test_case3(self):
        arr = ['b', 'c', 'd']
        self.assertEqual(probability_a(arr, 2), 0.0)


if __name__ == "__main__":
    unittest.main()
