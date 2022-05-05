
# global variable
number = 100

def function():

    global number
    print(number)

    # changing global variable
    number += 10
    print(number)

function()
print(number)