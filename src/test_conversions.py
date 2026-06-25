
"""Script for debugging conversion functions"""

import unittest
from textnode import TextType, TextNode, text_node_to_html_node

class TestConversions(unittest.TestCase):
    """
    Unit Tests
    """

    def test_text_node_to_html_node_text(self: TextNode):
        """
        TextType.TEXT converts to raw text and no tag
        """
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


    def test_text_node_to_html_node_bold(self: TextNode):
        """
        TextType.BOLD converts to tag and text.
        """

        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")


    def test_text_node_to_html_node_italic(self: TextNode):
        """
        TextType.ITALICS converts to tag and text.
        """

        node = TextNode("This is a italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic text node")


    def test_text_node_to_html_node_link(self: TextNode):
        """
        TextType.LINK converts to tag, text if any, and props dict().
        """

        node = TextNode("This is a link leafnode", TextType.LINK, "www.url.com/web/link")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link leafnode")
        self.assertEqual(html_node.props, {"href": "www.url.com/web/link"})


    def test_text_node_to_html_node_image(self: TextNode):
        """
        TextType.IMAGE converts to tag, text if any, and props dict().
        """

        node = TextNode("This is a img leafnode", TextType.IMAGE, "www.url.com/web/link")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {
                "src": "www.url.com/web/link",
                "alt": "This is a img leafnode"
            }
        )


if __name__ == "__main__":
    unittest.main()
