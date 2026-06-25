
"Script for debugging LeafNodes"

import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    """Unit test for debugging LeafNodes"""

    def test_to_html(self: LeafNode):
        """Tests LeafNode.to_html() method"""

        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_repr(self):
        """Tests LeafNode.__repr__() method"""
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(repr(node), "LeafNode[Tag(p), Value(Hello, world!), Props(None)]")


if __name__ == "__main__":
    unittest.main()
