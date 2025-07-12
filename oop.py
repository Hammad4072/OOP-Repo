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

#inheritence

class Dog(pet):
    def show_info(self):
        print("the dog name is :", self.get_name())


obj = Dog("labre", 3)
obj.show_info()

# obj = pet("labre" , "2 years")   
# print(obj.get_name())




# print("My pet name is :", obj.get_name())
# print("My pet age is :", obj.get_age())