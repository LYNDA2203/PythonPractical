class Animal:
    
    def __init__(self,name):
        self.name = name #initialize the name attributes
        
    def sound(self):
        return "Animal makes sound"
        
#single inheritance
class Dog(Animal):
    #overridding the sound method
    def sound(self):
        return f"{self.name} barks!!!"
    
#multiple inheritance
class Cat(Animal):
    #overridding the sound method
    def sound(self):
        return  f"{self.name} meowww!!!!"

animal1 = Dog("jackyy")
animal2 = Cat("messy")
print(animal1.sound())
print(animal2.sound())