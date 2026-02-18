import unittest
import re

def is_valid(email):
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return bool(re.match(pattern, email))


def filter_emails(emails):
    return sorted(list(filter(is_valid, emails)))


class TestEmailValidation(unittest.TestCase):

    def test_case1(self):
        emails = ["abc@gmail.com", "invalid@.com", "user-1@domain.co"]
        result = filter_emails(emails)
        self.assertEqual(result, ["abc@gmail.com", "user-1@domain.co"])

    def test_case2(self):
        emails = ["test@domain.com", "wrong@domain.toolong"]
        result = filter_emails(emails)
        self.assertEqual(result, ["test@domain.com"])

    def test_case3(self):
        emails = ["bad@", "good@ok.in"]
        result = filter_emails(emails)
        self.assertEqual(result, ["good@ok.in"])


if __name__ == "__main__":
    unittest.main()
