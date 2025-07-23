class Shape:
    def __init__(self,length,breadth):
        self._length = length
        self._breadth = breadth
        
    def dispalySides(self):
        #accessing protected data members
        print("Length: ",self._length)
        print("Breadth: ",self._breadth)

class Rectangle(Shape):
    def __init__(self,length,breadth):
        #calling the constructor of super class
        super().__init__(length,breadth)
        
    def calculateArea(self):
        print("Area: ",self._length * self._breadth)
        
area = Rectangle(80,50)
area.dispalySides()
area.calculateArea()
