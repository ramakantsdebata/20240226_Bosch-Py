# class MyType(BaseType):
class MyType:
    # Methods
    def Print(self):
        print("Data")

    # def __constructor__():
    #     pass
        
    def __init__(self):
        self.x = 10
    
    # Instance Methods
    def Process(self):
        self.y = 20

    


obj = MyType()

obj.Process()    ##  MyType::Process(obj)
