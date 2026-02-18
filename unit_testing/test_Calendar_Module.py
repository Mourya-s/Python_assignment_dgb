import unittest
import calendar

def find_day(month, day, year):
    weekday = calendar.weekday(year, month, day)
    return calendar.day_name[weekday].upper()


class TestCalendarModule(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(find_day(8, 5, 2015), "WEDNESDAY")

    def test_leap_year(self):
        self.assertEqual(find_day(2, 29, 2020), "SATURDAY")

    def test_new_year(self):
        self.assertEqual(find_day(1, 1, 2023), "SUNDAY")

    def test_random(self):
        self.assertEqual(find_day(12, 25, 2021), "SATURDAY")


if __name__ == "__main__":
    unittest.main()
