import unittest
import numpy as np

def matrix_determinant(arr):
    return round(np.linalg.det(arr), 2)


class TestLinearAlgebra(unittest.TestCase):

    def test_basic(self):
        arr = np.array([[1, 2],
                        [3, 4]])
        self.assertEqual(matrix_determinant(arr), -2.00)

    def test_identity(self):
        arr = np.array([[1, 0],
                        [0, 1]])
        self.assertEqual(matrix_determinant(arr), 1.00)

    def test_zero_matrix(self):
        arr = np.array([[0, 0],
                        [0, 0]])
        self.assertEqual(matrix_determinant(arr), 0.00)


if __name__ == "__main__":
    unittest.main()
