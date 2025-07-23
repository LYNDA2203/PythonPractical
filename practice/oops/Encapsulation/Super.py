#super class
class Super:
    #public data member
    var1 = None
    
    #protected data member
    _var2 = None
    
    #private data member
    __var3 = None
    
    #constructor
    def __init__(self,var1,var2,var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3
    
    #public member function
    def displayPublicMembers(self):
        #accessing public data members
        print("Public Data Member:",self.var1)
        
    #protected member function
    def _displayProtectedMembers(self):
        #accessing private data members
        print("Protected Data Member:",self._var2)
        
    #private mamber funtion
    def __displayPrivateMembers(self):
        #accessing protected data members
        print("Private Data Member:",self.__var3)
        
    #public member function
    def accessPrivateMembers(self):
        #accessing private member funtion
        self.__displayPrivateMembers()
        
#derived class
class Sub(Super):
    
    #construtor
    def __init__(self,var1,var2,var3):
        super().__init__(var1,var2,var3)
            
    #public member funtion
    def accessProtectedMembers(self):
        #acccessing protected member functions of super class
        self._displayProtectedMembers()

obj = Sub("public","protected","private")

obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()
print()

# Can also be accessed using
obj._displayProtectedMembers()
obj._Super__displayPrivateMembers()#accessing by name mangling
print()

# Object can access protected member
print("Object is accessing protected member:", obj._var2)
print("Object is accessing private member:", obj._Super__var3)

