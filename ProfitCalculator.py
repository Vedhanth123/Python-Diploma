principle = int(input())
roi = 0.18

reinvest = [principle]
return_ = 0

withdrawable = 0


for x in range(30):
    
    if(x < 8):
        return_ = principle * roi
        principle += return_
        reinvest.append(return_)
    if(x >= 8 and x < 21):
        principle -= reinvest[abs(8-x)]
        return_ = principle * roi
        principle += return_
        reinvest.append(return_)
    if(x >= 22):
        principle -= reinvest[abs(8-x)]
        return_ = principle * roi
        withdrawable += return_
        reinvest.append(return_)

print(withdrawable)

        
        
