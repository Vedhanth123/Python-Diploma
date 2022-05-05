# creating a class
class Car():

    def __init__(self):
        self.type = "petrol"

    def drive(self):
        print("Start and drive")
    
# single inheritance
class Tata(Car):

    def __init__(self):
        super().__init__()
        self.wheels = 4
    
# creating an object
c1 = Tata()
c1.drive()