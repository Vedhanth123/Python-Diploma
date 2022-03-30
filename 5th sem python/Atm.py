# ATM program

cash = int(input("Enter amount which you want to withdraw:"))

# store all the denomination of inr in atm
denomination = [100, 200, 500]

# check if all the denomination so the atm are present in atm
if(cash % denomination[0] and cash % denomination[1] and cash % denomination[2]):
    print("Here's your cash")
else:
    print("Invalid Amount")

# ---------------------------------------------------------------------------------------------------------------------

for i in range(10):
    print(i)

for i in range(2, 10):
    print(i)

for i in range(2, 10, 2):
    print(i)

# ---------------------------------------------------------------------------------------------------------------------

list_= [1,2,3]
tuple_ = (1,2,3,4)
dict_ = {0:1,1:2,2:3}
set_ = {1,2,3,4,5}

print(list_, tuple_, dict_, set_)
