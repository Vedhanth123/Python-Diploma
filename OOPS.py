# python file to practice with oops in python

class Dog():
  
  # class attribute
  no_of_legs = 4
  
  # declaring a constructor
  def __init__(self, name, age):
    
    # instance attributes
    self.name = name
    self.age = age
  
  # instance method
  def print(self):
    print(self.age, self.name)
    
    
# creating an obj
d1 = Dog("joker", 5)
d2 = Dog("idiot", 6)

d2.print()
