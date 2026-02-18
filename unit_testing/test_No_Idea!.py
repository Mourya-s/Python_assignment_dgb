import unittest

def calculate_happiness(arr, A, B):
    happiness = 0
    for num in arr:
        if num in A:
            happiness += 1
        elif num in B:
            happiness -= 1
    return happiness


class TestHappiness(unittest.TestCase):

    def test_case1(self):
        arr = [1, 5, 3]
        A = {3, 1}
        B = {5, 7}
        self.assertEqual(calculate_happiness(arr, A, B), 1)

    def test_case2(self):
        arr = [1, 2, 3]
        A = {1, 2}
        B = {3}
        self.assertEqual(calculate_happiness(arr, A, B), 1)

    def test_case3(self):
        arr = [4, 5]
        A = {1, 2}
        B = {3}
        self.assertEqual(calculate_happiness(arr, A, B), 0)


if __name__ == "__main__":
    unittest.main()
