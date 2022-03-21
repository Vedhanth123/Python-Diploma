# single inheritance 
'''
class A():
    def parent_function(self):
        print("Function1")
class B(A):
    def Child_function(self):
        print("Function2")

obj = B()
obj.parent_function()
obj.Child_function()
'''

# multiple inheritance
'''
class A():
    def Alpha(self):
        print("Function1")
    
class B():
    def Beta(self):
        print("Function2")

class C(A, B):
    pass

obj = C()
obj.Alpha()
obj.Beta()
'''

# hybrid inheritance
'''
class A():
    def function(self):
        print("Function in A")
    
class B(A):
    def function2(self):
        print("Function in B")

class C():
    def function3(self):
        print("Function in C")
    
class D(B, C): # combination of multilevel and single
    pass

obj = D()
obj.function()
obj.function2()
obj.function3()
'''

    
    
