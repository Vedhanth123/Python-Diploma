# Iterators: Iterators are objects which can be iterated using for loop

# to create an iterator an iterator class is used and its key methods are
# 1) __iter__() [returns the iterator object]
# 2) __next__() [returns the next element in the iterator]

# code to implement iterator
class odd_numbers():

    # constructor to initialize the range of odd numbers
    def __init__(self, range):
        self.Range = range

    # to create an object and return it
    def __iter__(self):

        # initializing the starting point of odd numbers
        self.StartingPoint = -1
        return self
    
    # __next__ returns the next element of the odd numbers
    def __next__(self):

        if(self.StartingPoint <= self.Range):
            self.StartingPoint += 2
            return self.StartingPoint
            
        

obj = odd_numbers(20)

obj = iter(obj)

for i in obj:
    print(i)

