from  abc import ABC,abstractmethod 
class Animal(ABC):
    @abstractmethod
    def sound(ABC):
        pass
    
class Dog(Animal):
    def sound(ABC):
        return "Bark!!!!"
    
class Cat(Animal):
    def sound(ABC):
        return "Meow!!!!!"
    
dog = Dog()
print(dog.sound())

cat = Cat()
print(cat.sound())

