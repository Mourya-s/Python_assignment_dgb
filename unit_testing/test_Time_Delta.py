import unittest
from datetime import datetime

def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    return int(abs((dt1 - dt2).total_seconds()))


class TestTimeDelta(unittest.TestCase):

    def test_basic(self):
        t1 = "Sun 10 May 2015 13:54:36 -0700"
        t2 = "Sun 10 May 2015 13:54:36 -0000"
        self.assertEqual(time_delta(t1, t2), 25200)

    def test_same_time(self):
        t1 = "Mon 01 Jan 2024 00:00:00 +0000"
        t2 = "Mon 01 Jan 2024 00:00:00 +0000"
        self.assertEqual(time_delta(t1, t2), 0)

    def test_one_day(self):
        t1 = "Tue 02 Jan 2024 00:00:00 +0000"
        t2 = "Mon 01 Jan 2024 00:00:00 +0000"
        self.assertEqual(time_delta(t1, t2), 86400)

    def test_timezone_difference(self):
        t1 = "Sun 10 May 2015 13:54:36 -0700"
        t2 = "Sun 10 May 2015 20:54:36 +0000"
        self.assertEqual(time_delta(t1, t2), 0)


if __name__ == "__main__":
    unittest.main()
