class Parent():

    # public class attribute
    job = "Computer-Scientist"

    # protected class attribute
    _Surname = "Gurram"

    # private class attribute
    __BankAccountPassword = "randomshittythingwhichIdon'tknow"

    @classmethod
    def printer(cls):
        return(cls.__BankAccountPassword)

class Child(Parent):
    pass
    
# ---------------------------------------------------------------------------------------------------------------------


print(Parent.job, Parent._Surname, Parent.printer())
# print(o2.job, o2._Surname)

# ---------------------------------------------------------------------------------------------------------------------
# python is a bit different in handling with access specifiers
# python contains 3 access specifiers
# 1) public: can be accessed within a class and outside a class
# 2) protected: can be accessed within class and subclasseso only 
# 3) private: can be accessed only within a class

# ---------------------------------------------------------------------------------------------------------------------