import unittest
import numpy as np

def min_and_max(arr):
    min_vals = np.min(arr, axis=1)
    return np.max(min_vals)


class TestMinAndMax(unittest.TestCase):

    def test_basic(self):
        arr = np.array([[2, 5], 
                        [3, 7], 
                        [1, 3], 
                        [4, 0]])
        self.assertEqual(min_and_max(arr), 3)

    def test_single_row(self):
        arr = np.array([[5, 10, 15]])
        self.assertEqual(min_and_max(arr), 5)

    def test_negative_values(self):
        arr = np.array([[-1, -2], 
                        [-3, -4]])
        self.assertEqual(min_and_max(arr), -3)


if __name__ == "__main__":
    unittest.main()
