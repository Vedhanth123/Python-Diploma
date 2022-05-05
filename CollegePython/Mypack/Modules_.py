# module in python refers to a file, a normal .py file

# This file is a module and can be imported into another file


def greet():
    print("Hi, How are you?")


# If you call function or write any code in the module then that code will also be imported into another file.  If you want to stop that then you can use this

if __name__ == '__main__':
    greet()
    print("You are an idiot") # this line will not be run in another file