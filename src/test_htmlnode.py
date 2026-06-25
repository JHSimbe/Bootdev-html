
"""Tests for debugging HTML nodes"""

import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    """Unit tests for debugging HTML nodes"""

    def test_props_to_html(self: HTMLNode):
        """Does props_to_html() actually convert HTMLNode.props into proper html?"""

        node1 = HTMLNode(
            "p",
            "This is a html node",
            props={"href": "https://www.reeeeeeee.gov"},
        )
        node2 = node1
        node3 = HTMLNode(
            "p",
            "This is a html node but not like ^^^ those html nodes...... i have children",
            [node2, node1],
            {"href": "https://www.reeeeeeee.gov"},
        )

        self.assertEqual(node1.props_to_html(), ' href="https://www.reeeeeeee.gov"')
        self.assertNotEqual(node1, node3)


if __name__ == "__main__":
    unittest.main()
