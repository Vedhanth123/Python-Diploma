# Python has a way to send variable number of arguments to a function this is done using
# *args

def fun(*args):

    print(type(args)) # prints: tuple
    print(args)

# Python also has a way to send variable number of keyworded arguments to a function This is done using
# **kwargs

def fun1(**kwargs):

    print(type(kwargs)) # prints: dict
    print(kwargs)

fun('vedhanth', 'gurram', 'CME')
fun1(name='vedhanth', surname='gurram', branch='CME')
