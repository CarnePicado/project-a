import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).parent.parent))

from date_string_utils import (
    format_date,
    get_year,
    reverse_string,
    count_words,
    capitalize_words
)


class TestDateUtils(unittest.TestCase):

    def test_format_date(self):
        self.assertEqual(format_date("2026-11-18"), "18.11.2026")

    def test_get_year(self):
        self.assertEqual(get_year("2026-11-18"), 2026)


class TestStringUtils(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_count_words(self):
        self.assertEqual(count_words("Hello world Python"), 3)

    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")


if __name__ == "__main__":
    unittest.main()
