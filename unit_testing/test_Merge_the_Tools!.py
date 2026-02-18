import unittest

def merge_the_tools(string, k):
    result = []
    for i in range(0, len(string), k):
        part = string[i:i+k]
        unique = ""
        for ch in part:
            if ch not in unique:
                unique += ch
        result.append(unique)
    return result


class TestMergeTools(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(
            merge_the_tools("AABCAAADA", 3),
            ["AB", "CA", "AD"]
        )

    def test_no_duplicates(self):
        self.assertEqual(
            merge_the_tools("ABCDEF", 2),
            ["AB", "CD", "EF"]
        )

    def test_all_same(self):
        self.assertEqual(
            merge_the_tools("AAAAAA", 2),
            ["A", "A", "A"]
        )

    def test_single_length(self):
        self.assertEqual(
            merge_the_tools("ABC", 1),
            ["A", "B", "C"]
        )

    def test_large_k(self):
        self.assertEqual(
            merge_the_tools("ABCDE", 5),
            ["ABCDE"]
        )


if __name__ == "__main__":
    unittest.main()
