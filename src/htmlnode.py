class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
        
    def props_to_html(self):
        if self.props is None:
            return ""
        
        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        
        return result

    def __repr__(self):
        return f"HTMLNode(Tag={self.tag}, Value={self.value}, Children={self.children}, Props={self.props})"

    def __eq__(self, other):
        return (
            self.tag == other.tag 
            and self.value == other.value 
            and self.children == other.children
            and self.props == other.props
        )
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        elif self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        elif self.children is None:
            raise ValueError("invalid HTML: no children")
        else:
            child_html = ""
            for child in self.children:
                child_html += child.to_html()
            return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    