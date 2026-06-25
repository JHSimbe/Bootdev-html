
"Script for debugging ParentNodes"

import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):

    """Unit test for debugging ParentNodes"""

    def test_to_html_with_children(self):

        """Tests ParentNode.to_html() method"""

        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):

        """Tests ParentNode.to_html() method"""

        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_multiple_children(self):
        """Checks output when multiple children passed."""

        child_node1 = LeafNode("span", "LeafNode1 Test")
        child_node2 = LeafNode("div", "LeafNode2 Test")
        child_node3 = LeafNode("b", "LeafNode3 Test")
        parent_node = ParentNode("p", [child_node1, child_node2, child_node3])
        self.assertEqual(
            parent_node.to_html(),
            "<p><span>LeafNode1 Test</span><div>LeafNode2 Test</div><b>LeafNode3 Test</b></p>"
        )

    def test_to_html_with_no_tag(self):
        """Tests ParentNode.to_html() method"""

        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        #parent_node.to_html()
        self.assertRaises(ValueError)

    def test_to_html_with_no_children(self):
        """Checks output when no children passed. Expects: 'ValueError' """

        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", None)
        self.assertRaises(ValueError)



if __name__ == "__main__":
    unittest.main()
