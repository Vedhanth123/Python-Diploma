
# 1) create a folder
# 2) create a __init__.py file in the folder
# 3) create a module by creating a python file inside the package
# 4) import the package and use it

def table_printer(num):

    for x in range(1,11):
        print(f"{num} * {x} = {num*x}")

table_printer(2)