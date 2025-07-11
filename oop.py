class pet:
    def __init__(self, name , age):
        #encapsulation:
        self.__name = name
        self.__age = age
    def get_name(self):
        return f"{self.__name}"
    def get_age(self):
        return f"{self.__age}"
    
obj = pet("labre", "2 years")
print("My pet name is :", obj.get_name())
print("My pet age is :", obj.get_age())