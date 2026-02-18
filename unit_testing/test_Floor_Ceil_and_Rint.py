import unittest
import numpy as np

def floor_ceil_rint(arr):
    floor_vals = np.floor(arr)
    ceil_vals = np.ceil(arr)
    rint_vals = np.rint(arr)
    return floor_vals, ceil_vals, rint_vals


class TestFloorCeilRint(unittest.TestCase):

    def test_basic(self):
        arr = np.array([1.1, 2.5, -3.7])
        floor_vals, ceil_vals, rint_vals = floor_ceil_rint(arr)

        np.testing.assert_array_equal(floor_vals, np.array([1., 2., -4.]))
        np.testing.assert_array_equal(ceil_vals, np.array([2., 3., -3.]))
        np.testing.assert_array_equal(rint_vals, np.array([1., 2., -4.]))

    def test_integers(self):
        arr = np.array([1, 2, 3])
        floor_vals, ceil_vals, rint_vals = floor_ceil_rint(arr)

        np.testing.assert_array_equal(floor_vals, arr)
        np.testing.assert_array_equal(ceil_vals, arr)
        np.testing.assert_array_equal(rint_vals, arr)

    def test_zero(self):
        arr = np.array([0.0, -0.0])
        floor_vals, ceil_vals, rint_vals = floor_ceil_rint(arr)

        np.testing.assert_array_equal(floor_vals, np.array([0., 0.]))
        np.testing.assert_array_equal(ceil_vals, np.array([0., 0.]))
        np.testing.assert_array_equal(rint_vals, np.array([0., 0.]))


if __name__ == "__main__":
    unittest.main()
