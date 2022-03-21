class Calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Calculator2(Calculator):

    def add(self):
        print(self.a + self.b)
    def sub(self):
        print(self.a - self.b)
    def mul(self):
        print(self.a * self.b)
    def div(self):
        print(self.a / self.b)

obj = Calculator2(10, 200)

obj.add()
obj.sub()
obj.mul()
obj.div()
