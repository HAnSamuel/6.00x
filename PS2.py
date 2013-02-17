balance = 3329; annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12.0
Payment = 10
Total = 0
times = 0
orbalance=balance

while balance>0:
    balance=orbalance
    miniPayment=Payment*times
    for m in range(1,13):
        unpaidBalance=balance-miniPayment
        Interest=unpaidBalance*monthlyInterestRate
        balance=unpaidBalance+Interest
        Total+=miniPayment
#        print(str(Total)+' ; '+str(balance)+' '+str(miniPayment))
    times+=1
    Total = 0
print('Lowest Payment: ' + str(miniPayment))
