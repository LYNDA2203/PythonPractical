from abc import ABC,abstractmethod

class Car(ABC):
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    
    @abstractmethod #mandatory to use in the sub_class   
    def printDetails(self):
        pass
    
    #concrete method -->ignored or overridden or directly used in sub class
    def accelerate(self):
        print("Speed up.....")
        
    def break_applied(self):
        print("Car stopped")
        
class Hatchback(Car):
    def printDetails(self):
        print("Brand: ",self.brand)
        print("Model:",self.model)
        print("Year:",self.year)
        
    def sunroof(self):
        print("Sunroof: Not available ")
        
class Suv(Car):
    def printDetails(self):
        print("Brand: ",self.brand)
        print("Model:",self.model)
        print("Year:",self.year)
        
    def sunroof(self):
        print("Sunroof: Available")
        
car1 = Hatchback("Maruti","Alto","2022")

car1.printDetails()
car1.accelerate()
car1.sunroof()
car1.break_applied()
print("----------------------------------")

car2 = Suv("boxy city","mahindra","2024")

car2.printDetails()
car2.accelerate()
car2.sunroof()
car2.break_applied()
print("----------------------------------")