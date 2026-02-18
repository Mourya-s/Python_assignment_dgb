def calculate_avg(dic, query_name):
    avg = sum(dic[query_name]) / len(dic[query_name])
    return round(avg, 2)


import unittest

class TestAverage(unittest.TestCase):

    def test_average(self):
        dic = {
            "Krishna": [67, 68, 69]
        }
        self.assertEqual(calculate_avg(dic, "Krishna"), 68.00)


if __name__ == "__main__":
    unittest.main()
