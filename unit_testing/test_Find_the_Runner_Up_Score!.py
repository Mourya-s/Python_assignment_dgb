

def runner_up(arr):
    unique = list(set(arr))
    unique.sort()
    return unique[-2]

import unittest

class TestRunnerUp(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(runner_up([2,3,6,6,5]), 5)

    def test_duplicates(self):
        self.assertEqual(runner_up([10,20,20,5,30,30]), 20)

    def test_negative(self):
        self.assertEqual(runner_up([-1,-2,-3,-4,-5]), -2)


if __name__ == "__main__":
    unittest.main()
