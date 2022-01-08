from oops import Goods

class Goods2(Goods):

    # -----------------------------------------------------------------------------------------------------------------
    # class methods: class methods are the special type methods which send class itself as their first parameter
    # The use of class method is used to instantiate objects by the data which is outside of python file.
    # -----------------------------------------------------------------------------------------------------------------
    @classmethod
    def inputter(cls):
        return cls

    # -----------------------------------------------------------------------------------------------------------------
    # static method: Static method is are the methods which can be called without instantiating the class 
    # -----------------------------------------------------------------------------------------------------------------

    @staticmethod
    def printer():
        return "This is a method which can be called without instantiating class"

if __name__ == '__main__':

    print(Goods2.inputter())
    print(Goods2.printer())
