import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq_a(self):
        node = HTMLNode("a", "google", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("a", "google", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("a", "google", None, {"href": "https://www.google.com", "target": "_blank"})
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_none(self):
        node = HTMLNode("p", "test")
        self.assertEqual(node.props_to_html(), "")
        
    def test_eq_p(self):
        node = HTMLNode("p", "This is a test")
        node2 = HTMLNode("p", "This is a test")
        self.assertEqual(node, node2)
