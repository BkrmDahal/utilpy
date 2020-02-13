import unittest
from ..utilpy import utils


class Testutils(unittest.TestCase):
    def test_page_soup(self):
        self.soup = utils.page_soup("https://twitter.com")
        self.len = len(self.soup.get_text())
        self.assertGreater(self.len, 100)

    def test_format_filename(self):
        self.name = utils.format_filename("hello_@#.jpg")
        self.assertEqual(self.name, "hello_.jpg")

    def test_walk_directory(self):
        self.files = utils.walk_directory(".")
        self.assertIsNotNone(self.files)


if __name__ == "__main__":
    unittest.main()
