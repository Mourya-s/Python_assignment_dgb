import unittest

def can_stack(cubes):
    cubes = cubes[:]  # avoid modifying original list
    last = float('inf')

    while cubes:
        if cubes[0] >= cubes[-1]:
            pick = cubes.pop(0)
        else:
            pick = cubes.pop()

        if pick > last:
            return "No"

        last = pick

    return "Yes"


class TestPilingUp(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(can_stack([4, 3, 2, 1, 3, 4]), "Yes")

    def test_case2(self):
        self.assertEqual(can_stack([1, 3, 2]), "No")

    def test_case3(self):
        self.assertEqual(can_stack([1, 1, 1, 1]), "Yes")


if __name__ == "__main__":
    unittest.main()
