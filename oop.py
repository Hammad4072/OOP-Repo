#Abstraction:
from abc import ABC , abstractmethod
class pet(ABC):
    def __init__(self, name , age):
     
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age
    @abstractmethod
    def show_info(self): #polymorphism creation (definition or method)
        pass

#inheritence + polymorphism

class Dog(pet):
    def show_info(self):
        print("the dog name is :", self.get_name(), "\nAnd its age is :" , self.get_age())

# Inheritance + Polymorphism
class Cat(pet):
    def show_info(self):  # Polymorphic method
        print("The cat named ", self.get_name(), "loves to sleep")
        print(self.get_name(), "is ", self.get_age(), "years old")

#polymorphism called

Dogg = Dog("labre", 3)
Dogg.show_info()

Catt = Cat("Persian", 1)
Catt.show_info()

# obj = pet("labre" , "2 years")   
# print(obj.get_name())




# print("My pet name is :", obj.get_name())
# print("My pet age is :", obj.get_age())