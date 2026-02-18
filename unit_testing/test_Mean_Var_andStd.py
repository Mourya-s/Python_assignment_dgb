import unittest
import numpy as np

def stats(arr):
    mean = np.mean(arr)
    var = np.var(arr)
    std = np.std(arr)
    return mean, var, std


class TestStats(unittest.TestCase):

    def test_mean(self):
        arr = np.array([1, 2, 3, 4])
        mean, _, _ = stats(arr)
        self.assertEqual(mean, 2.5)

    def test_variance(self):
        arr = np.array([1, 2, 3, 4])
        _, var, _ = stats(arr)
        self.assertAlmostEqual(var, 1.25)

    def test_std(self):
        arr = np.array([1, 2, 3, 4])
        _, _, std = stats(arr)
        self.assertAlmostEqual(std, 1.1180, places=3)


if __name__ == "__main__":
    unittest.main()
