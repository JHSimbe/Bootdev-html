
"Home of HTMLNode"

class HTMLNode:
    """Class representing an HTML node"""

    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list | None = None,
        props: dict[str:str] | None = None,

    ) -> None:

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        """Function defined elsewhere"""

        raise NotImplementedError("Not Ready Yet")


    def props_to_html(self):
        """Function that converts node elements to html"""

        html = str()
        if not self.props:
            return html
        for prop in self.props:
            html = html + f' {prop}="{self.props[prop]}"'
        return html

    def __repr__(self):
        if not self.children:
            return f"HTMLNode({self.tag, self.value, self.props})"
        children = ""
        for child in self.children:
            children += f", HTMLNode({child.value})"
        return f"HTMLNode(Tag={self.tag}, value={self.value}, Children={children}, Props={self.props})"



class LeafNode(HTMLNode):
    """
    A HTMLNode with no children
    """

    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        props: dict[str:str] | None = None,

    ) -> None:
        if value is None:
            raise ValueError("LeafNode must have a value")

        super().__init__(tag= tag, value= value, props= props)


    def to_html(self) -> str:
        """Converts a LeafNode obj to html"""

        if not self.value:
            raise ValueError("All LeafNodes must have a value")

        elif not self.tag:
            return f"{self.value}"

        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


    def __repr__(self) -> str:
        return f"LeafNode[Tag({self.tag}), Value({self.value}), Props({self.props})]"



class ParentNode(HTMLNode):
    """
    An HTMLNode that has children
    """

    def __init__(
        self,
        tag: str,
        children: list,
        props: dict[str:str] | None = None,
    ) -> None:

        super().__init__(tag= tag, children= children, props= props )


    def to_html(self):
        if not self.tag:
            raise ValueError("ERROR: No tag found")
        if not self.children:
            raise ValueError("ERROR: No children found")

        descendants = ""
        for child in self.children:
            descendants = descendants + child.to_html()

        return f"<{self.tag}>{descendants}</{self.tag}>"
