import unittest
from collections import namedtuple

def average_marks(n, columns, students):
    Student = namedtuple("Student", columns)
    total = 0

    for data in students:
        s = Student(*data)
        total += int(s.MARKS)

    return round(total / n, 2)


class TestNamedTuple(unittest.TestCase):

    def test_basic(self):
        n = 3
        columns = ["ID", "MARKS", "NAME", "CLASS"]
        students = [
            ["1", "97", "Raymond", "7"],
            ["2", "50", "Steven", "4"],
            ["3", "91", "Adrian", "9"]
        ]
        self.assertEqual(average_marks(n, columns, students), 79.33)

    def test_single(self):
        n = 1
        columns = ["ID", "MARKS", "NAME", "CLASS"]
        students = [["1", "100", "John", "10"]]
        self.assertEqual(average_marks(n, columns, students), 100.00)

    def test_zero_marks(self):
        n = 2
        columns = ["ID", "MARKS", "NAME", "CLASS"]
        students = [
            ["1", "0", "A", "1"],
            ["2", "0", "B", "2"]
        ]
        self.assertEqual(average_marks(n, columns, students), 0.00)


if __name__ == "__main__":
    unittest.main()
