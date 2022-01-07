# declaring a class which stores goods stored in an electronics store

class Goods():

    '''
    Each good has attributes of:
        1) name
        2) price
        3) quantity
    '''

    # creating a constructor
    def __init__(self, name: str, price: float, quantity: int): # name: str denotes that name parameter given should only contain str other than that datatype will not be accepted, similar to type congestion in C++, Java

        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # assert: assert statement in python is used to check condition and return an assertion error if the statement is false.
        assert quantity >= 0, f"The quantity can't be less than zero" # we can also add messages to assertion error
        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        
        self.name = name
        self.price = price
        self.quantity = quantity

    # creating a method to find out total value of the each good
    def ValueCalculator(self):
        return self.price * self.quantity
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# creating objects of this class

good1 = Goods('phone', 5000, -5)
good2 = Goods('Laptop', 30000, 2)


print(good1.ValueCalculator())
print(good2.ValueCalculator())
