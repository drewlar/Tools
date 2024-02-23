class Node:
    
    def __init__(self, element=None, parent=None, 
                 Lchild= None, Rchild = None):
        self._element = element
        self._parent = parent
        self._Lchild = Lchild
        self._Rchild = Rchild

    def __repr__(self) -> str:
        return f'Element = {self._element}\n 
                Parent = {self._parent}\n 
                Left Child = {self._Lchild}\n 
                Right Child = {self._Rchild}'

    def __str__(self) -> str:
        return self.__repr__() 

    def addChild(self, element=None, cnode=None):
        assert not (self._Lchild and self._Rchild)

        if cnode and not element:
            assert isinstance(cnode, Node)
        
        try:
            self.addLeft(cnode=cnode) if cnode else self.addLeft(element=element)
        except:
            self.addRight(cnode=cnode) if cnode else self.addRight(element=element)

    def addRight(self,element=None, cnode=None):
        assert not self._Rchild
        self._Rchild = cnode if cnode else Node(element)

    def addLight(self,element=None, cnode=None):
        assert not self._Lchild
        self._Lchild = cnode if cnode else Node(element)
    


class NodeDescriptor:
    def __init__(self):
        self.data = dict()

    def __get__(self,instance,owner):
        return self.data[instance]
    
    def __set__(self, instance, value):
        assert isinstance(value,Node)
        self.data[instance] = value