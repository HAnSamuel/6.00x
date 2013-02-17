balance = 3329
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate/12.0
Total= 0
for m in range(1,13):
    miniPayment=balance*monthlyPaymentRate
    unpaidBalance=balance-miniPayment
    Interest=unpaidBalance*monthlyInterestRate
    balance=unpaidBalance+Interest
    Total+=miniPayment
    print('Month: ' + str(m))
    print('Minimum monthly payment: ' + str(round(miniPayment,2)))
    print('Remaining balance: ' + str(round(balance,2)))

print('Total paid: ' + str(round(Total,2)))
print('Remaining balance: ' + str(round(balance,2)))
