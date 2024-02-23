class StringDescriptor:
    def __init__(self):
        self.data = dict()

    def __get__(self,instance,owner):
        return self.data[instance]
    
    def __set__(self, instance, value):
        assert isinstance(value,str)
        self.data[instance] = value