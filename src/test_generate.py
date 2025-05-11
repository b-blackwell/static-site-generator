import unittest

from generate import *

class TestGenerate(unittest.TestCase):
    def test_generate_header(self):
        markdown = "# This is the header\n**This is bold text**"
        title = extract_title(markdown)
        self.assertEqual(title, "This is the header")

    def test_generate_no_header(self):
        markdown = "This is plain text with no header"
        with self.assertRaises(ValueError):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()