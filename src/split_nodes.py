
from textnode import TextNode, TextType

types = {
    TextType.BOLD: "**",
    TextType.CODE: "`",
    TextType.ITALIC: "_",
}

def to_text_node(text: str, text_type: TextType) -> list[TextNode]:

    nodes = text.split(types[text_type])

    if len(nodes) < 2:
        return [TextNode(nodes[0], text_type),]
    elif len(nodes) == 2:
        node_1 = TextNode(nodes[0], text_type)
        node_2 = TextNode(nodes[1], TextType.TEXT)
        return [node_1, node_2]
    else:
        raise Exception("ERROR: Invalid markdown syntax")


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    converted = []

    for node in old_nodes:

        if node.text.startswith(delimiter):
            results = to_text_node(node.text, text_type)
            converted.extend(results)

        else:
            for i, char in enumerate(node.text):
                if char == delimiter or char + node.text[i + 1] == delimiter:
                    if i != 0:
                        node_0 = TextNode(node.text[::i], TextType.TEXT)
                        converted.append(node_0)
                        break

                    converted.extend(to_text_node(node.text[i::], text_type))
                    break

    return converted
