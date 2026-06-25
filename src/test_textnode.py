
"""debug tests for TextNode class"""

import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    """Class for unit tests"""

    def test_eq(self: TextNode):
        """These nodes are the same!?"""

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_text_type(self: TextNode):
        """These text types aren't the same?!"""

        node = TextNode("This is a text node", TextType.TEXT, "https//www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https//www.boot.dev")
        self.assertNotEqual(node, node2)


    def test_url(self):
        """Tests Textnode.url"""

        node = TextNode("This is a text node", TextType.ITALIC, "https//www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC)
        node3 = TextNode(
            "This is a text node",
            TextType.ITALIC,
            "https//www.I_NEED_MORE_SALMON.ree"
        )
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node, node3) #Dont Know if this works!!

if __name__ == "__main__":
    unittest.main()
