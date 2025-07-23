class Base:
    
    def fun(self):
        print("Inside Base class of public method")
        
    def __fun(self):
        print("Inside the basse class of private method")
        
    def display_private_method(self):
        self.__fun()
        
class Detrived(Base):
    
    def __init__(self):
        super().__init__()
        
    def call_public(self):
        print("\n Inside the derived class calling the public method")
        self.fun()
        
    def call_private(self):
        print("\n Inside derived class calling the private method")
        self.display_private_method
        
object = Detrived()
object.call_public()
object.call_private()