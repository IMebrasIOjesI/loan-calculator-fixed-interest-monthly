while True:
    try:
        loan = float(input('Loan Amount: '))
        if loan > 0:
            break
    except:
        print('Error: Please type a reasonable number.')
        continue
        
while True:
    try:
        payment = float(input('To Pay Per Month: '))
        if payment > 0:
            break
    except:
        print('Error: Please type a reasonable number.')
        continue
while True:
    try:
        interestrate = float(input('Interest rate in Percentage: '))
        if interestrate > 0:
            break
    except:
        print('Error: Please type a reasonable number.')
        continue
print('...................................................................................')
ogLoan = loan
count = 0
countpay = 0
while loan > 0:
    count = count + 1
    interest = loan * (interestrate / 100)
    balance = loan + interest
    print('Month:', count)
    print('Your Previous Balance: ', f'{round(loan,2):,}')
    print('Current Interest:', f'{round(interest,2):,}')
    print('New Balance: ', f'{round(balance,2):,}')
    if loan >= payment or loan > 0:
        while True:
            custompay = input('Press "Enter" for the default payment. If not, please enter Custom Payment: ')
            custompay = custompay.strip()
            if custompay == '':
                if payment >= loan:
                    print('You Paid: ', f'{round(balance,2):,}')
                    loan = balance - balance
                    print('Your Current Balance: ', f'{round(loan,2):,}')
                    print('...................................................................................')
                    countpay = countpay + balance
                    break
                else:
                    loan = balance - payment
                    print('You Paid: ', f'{round(payment,2):,}')
                    print('Your Current Balance: ', f'{round(loan,2):,}')
                    print('...................................................................................')
                    countpay = countpay + payment
                    break
            try:
                fcustompay = float(custompay)
                if fcustompay <= loan and loan > 0:
                    loan = balance - fcustompay
                    print('You Paid: ', f'{round(fcustompay,2):,}')
                    print('Your Current Balance: ', f'{round(loan,2):,}')
                    print('...................................................................................')
                    countpay = countpay + fcustompay
                    break
                elif fcustompay >= loan and loan > 0:
                    loan = balance - balance
                    print('You Paid: ', f'{round(balance,2):,}')
                    print('Your Current Balance: ', f'{round(loan,2):,}')
                    print('...................................................................................')
                    countpay = countpay + balance
                    break
                else:
                    print('You entered a negative value. Please try again.')
                    continue
            except:
                print('Error: You did not type a number! Press "Enter" blank for default payment.')
                continue        
    else:
        countpay = countpay + balance
        print(countpay)
        break
totalint = round(countpay - ogLoan, 2)
intrate = round((totalint / ogLoan) * 100, 2)
print('Original Amount Loaned:', f'{round(ogLoan,2):,}')
print('Interest Rate in Percentage %:', f'{round(interestrate,2):,}')
print('Total Paid For the Loan: ', f'{round(countpay,2):,}')
print('Total Paid in Interest:', f'{totalint:,}')
print('Total Interest Rate:', intrate, '%')
print('Total Paid Months:', count)