# id operator

# ID operator in python is used to check whether two objects are same with same memory location

# for instance
a = ["English", "Hindi"]
b = ["English", "Hindi"] 

c = a

print(a is b) # b and a are both same objects and both have same values but they are not identical

print(c is a) # both are same objects and have same memory location

print(a == b) # == operator checks whether both have same value or not but it doesn't check whether both have same memory location
