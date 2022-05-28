
def Calculate(principal, duration):

    income = 0
    roi = 0.18
    IncomePercentage = 0.9
    Stake = 0
    HistoryOfStakes = {7:principal}
    amount = 0

    for x in range(duration):

        if(x < 7):
            income = principal * roi
            income *= IncomePercentage
            Stake += income
            if(Stake >= 0.05):
                HistoryOfStakes[x+7] = Stake
                principal += Stake
                Stake = 0
            income = 0
        if(x >= 7 and x < duration-x):
            if(x in HistoryOfStakes):
                principal -= HistoryOfStakes[x]
                del HistoryOfStakes[x]
            income = principal * roi
            income *= IncomePercentage
            Stake += income
            if(Stake >= 0.05):
                HistoryOfStakes[x+7] = Stake
                principal += Stake
                Stake = 0
            income = 0
        if(x == duration-x):
            if(x in HistoryOfStakes):
                principal -= HistoryOfStakes[x]
                del HistoryOfStakes[x]
            income = principal * roi
            income *= IncomePercentage
            amount += income
            income = 0
    
    print(amount)

# principal = float(input("Enter your principal amount: "))
principal = float(input("Enter your principal amount: "))
duration = int(input("No. of dayes you want to store for? "))
Calculate(principal, duration)