
"""debug tests for split_nodes function"""

import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter

text_nodes = [
    TextNode("Some words, _some italics_, more words!", TextType.TEXT),
    TextNode("**Some bold words**, some words.", TextType.TEXT),
    TextNode("Some words `print('Some code!')`", TextType.TEXT),
    TextNode("**SOME HARSH WORDS, POSSIBLY EVEN EXPLETIVES**", TextType.TEXT),
    TextNode("Some link", TextType.LINK, url="https://www.somelink.link/stilllink1")
]

class TestTextNode(unittest.TestCase):
    """Class for unit tests"""

    def test_type(self: TextNode):
        """These are equal"""

        correct = [
            TextNode("Some words", TextType.TEXT),
            TextNode("some italics", TextType.ITALIC),
            TextNode("more words!", TextType.TEXT),
        ]
        nodes = [text_nodes[0], text_nodes[4]]

        result = [split_nodes_delimiter(nodes, "_", TextType.TEXT)]

        self.assertEqual(correct[0], result[0])
        self.assertEqual(correct[1], result[1])
        self.assertEqual(correct[2], result[2])