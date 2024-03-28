accountsList = []


def newAccount(aName, aBalance, aPassword):
    global accountsList
    newAccountDict = {'name': aName, 'balance': aBalance, 'password': aPassword}
    accountsList.append(newAccountDict)


def show(accountNumber):
    global accountsList
    print('Account', accountNumber)
    thisAccountDict = accountsList[accountNumber]
    print('       Name:', thisAccountDict['name'])
    print('       Balance:', thisAccountDict['balance'])
    print('       Password:', thisAccountDict['password'])
    print()


def getBalance(accountNumber, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None
    return thisAccountDict['balance']


def deposit(accountNumber, amountToDeposit, password):
    global accountsList
    if amountToDeposit < 0:
        print('Deposit amount is incorrect: must be positive')
        return None
    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None

    thisAccountDict['balance'] += amountToDeposit
    return thisAccountDict['balance']


def withdraw(accountNumber, amountToWithdraw, password):
    global accountsList
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None

    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
        print('Incorrect password')
        return None

    if amountToWithdraw >= thisAccountDict['balance']:
        print('You cannot withdraw more than you have in your account')
        return None

    thisAccountDict['balance'] -= amountToWithdraw
    return thisAccountDict['balance']


print("Joe's account is account number:", len(accountsList))
newAccount("Joe", 100, 'soup')

print("Mary's account is account number:", len(accountsList))
newAccount("Mary", 12345, 'nuts')

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press n to create a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()  # force lowercase
    action = action[0]  # just use first letter
    print()

    if action == 'b':
        print('Get Balance:')
        userAccountNumber = int(input('Please enter your account number: '))
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('Deposit:')
        userAccountNumber = input('Please enter the account number: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')

        newBalance = deposit(userAccountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)

    elif action == 'n':
        print('New Account:')
        userName = input('What is your name? ')
        userStartingAmount = input('What is the amount of your initial deposit? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('What password would you like to use for this account? ')

        userAccountNumber = len(accountsList)
        newAccount(userName, userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)

    if action == 'w':
        print('Withdraw:')
        userAccountNumber = int(input('Please enter your account number: '))
        userPassword = input('Please enter the password: ')
        withdrawAmount = int(input('Please enter the withdraw amount: '))
        theBalance = withdraw(userAccountNumber, withdrawAmount, userPassword)
        if theBalance is not None:
            print('Your balance is now:', theBalance)

    if action == 's':
        print('Show: ')
        for i, _ in enumerate(accountsList):
            show(i)

    if action == 'q':
        break

print('The End')
