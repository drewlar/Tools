from NodeClass.Node import Node 

class AhoCorasick():
    def __init__(self, word):
        assert isinstance(word,str)
        self.size = len(word)
        self.root = Node(word[0])
        current_node = self.root
        for letter in word[1:]:
            current_node.addChild(element=letter)
            current_node = current_node._children[0]
    
    @classmethod
    def add(cls,word):
        assert isinstance(word,str)
        current_Node = cls.root



    def __repr__(self):
        if self.root :
            current_node = self.root
            final_string = ''
            while current_node:
                final_string += current_node.__repr__()
                current_node = current_node._children[0]
            return final_string
        else:
            return "hi"





test_str = 'hello'
test = AhoCorasick(test_str)
print(test)
