import unittest

def string_formatting(n):
    width = len(bin(n)[2:])
    result = []

    for i in range(1, n + 1):
        line = (
            str(i).rjust(width) + " " +
            oct(i)[2:].rjust(width) + " " +
            hex(i)[2:].upper().rjust(width) + " " +
            bin(i)[2:].rjust(width)
        )
        result.append(line)

    return result


class TestStringFormatting(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(
            string_formatting(2),
            [
                " 1  1  1  1",
                " 2  2  2 10"
            ]
        )

    def test_single(self):
        self.assertEqual(
            string_formatting(1),
            ["1 1 1 1"]
        )

    def test_three(self):
        self.assertEqual(
            string_formatting(3),
            [
                " 1  1  1  1",
                " 2  2  2 10",
                " 3  3  3 11"
            ]
        )


if __name__ == "__main__":
    unittest.main()
