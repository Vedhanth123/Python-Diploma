# creating a class

class Student():

    def __init__(self, name:str, pin:int, course:str):

        self.__name = name
        self.pin = pin
        self.course = course
    
    # This is to get name
    @property
    def name(self):
        return self.__name
    
    @property.setter
    def name(self, n):
        self.name = n

s1 = Student("vedhanth",111, "CME")

print(s1.name)