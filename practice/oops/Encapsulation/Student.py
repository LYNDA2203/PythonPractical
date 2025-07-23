#super class
class Student:
    
    #protected data members
    _name = None
    _roll = None
    _branch = None
    
    #constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch
        
    # protected member function
    def _displayRollAndBranch(self):
        
        #accessing protected data members
        print("Roll:",self._roll)
        print("Branch:",self._branch)
        
# derived class
class School(Student):
    
    #constructor
    def __init__(self,name,roll,branch):
        Student.__init__(self,name,roll,branch)
        
    #public member function
    def displayDetails(self):
        #accessing protected data members of super class
        print("Name:",self._name)
        #accessing protected member fuctions of super class
        self._displayRollAndBranch()
        
stu =School("VOC",345678,"Information technology")
print("Attributes and Methods of Student",dir(stu))
print("Students details:")
stu.displayDetails()
input("\nPress Enter to exit...")