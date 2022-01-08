# declaring a class which stores goods stored in an electronics store

class Goods():

    '''
    Each good has attributes of:
        1) name
        2) price
        3) quantity
    '''

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Class attributes: class attributes are the attributes which are shard among all the instances of a class. These attributes are fetched by instances only if instances don't have that attribute.
    discount = 10
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # creating a constructor
    def __init__(self, name: str, price: float, quantity: int): # name: str denotes that name parameter given should only contain str other than that datatype will not be accepted, similar to type congestion in C++, Java

        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # assert: assert statement in python is used to check condition and return an assertion error if the statement is false. This can be handled by try except in python
        assert quantity >= 0, f"The quantity can't be less than zero" # we can also add messages to assertion error
        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        self.name = name
        self.price = price
        self.quantity = quantity

    # creating a method to find out total value of the each good
    def ValueCalculator(self):
        return (self.price + (self.price*self.discount//100)) * self.quantity
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# creating objects of this class

if __name__ == '__main__':
        
    good1 = Goods('phone', 5000, 5)
    good2 = Goods('Laptop', 30000, 2)


    print(good1.ValueCalculator())
    print(good2.ValueCalculator())

    print(Goods.__dict__) # shows all the attributes of the class in a dictinary format
    print(good1.__dict__) # shows all the attributes of that instance in a dictionary format

