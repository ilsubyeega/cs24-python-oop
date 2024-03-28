accountNamesList = []
accountBalancesList = []
accountPasswordsList = []


def newAccount(name, balance, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    accountNamesList.append(name)
    accountBalancesList.append(balance)
    accountPasswordsList.append(password)


def show(accountNumber):
    global accountNamesList, accountBalancesList, accountPasswordsList
    print('Account', accountNumber)
    print('       Name', accountNamesList[accountNumber])
    print('       Balance:', accountBalancesList[accountNumber])
    print('       Password:', accountPasswordsList[accountNumber])
    print()


def getBalance(accountNumber, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    return accountBalancesList[accountNumber]

def deposit(accountNumber, amountToDeposit, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if amountToDeposit < 0:
        print('Deposit amount is incorrect: must be positive')
        return None
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    accountBalancesList[accountNumber] += amountToDeposit
    return accountBalancesList[accountNumber]

def withdraw(accountNumber, amountToWithdraw, password):
    global accountNamesList, accountBalancesList, accountPasswordsList
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None
    if password != accountPasswordsList[accountNumber]:
        print('Incorrect password')
        return None
    if amountToWithdraw > accountBalancesList[accountNumber]:
        print('You cannot withdraw more than you have in your account')
        return None
    accountBalancesList[accountNumber] -= amountToWithdraw
    return accountBalancesList[accountNumber]


print("Joe's account is account number:", len(accountNamesList))
newAccount("Joe", 100, 'soup')

print("Mary's account is account number:", len(accountNamesList))
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

    if action == 'd':
        print('Deposit:')
        userAccountNumber = int(input('Please enter your account number: '))
        userPassword = input('Please enter the password: ')
        amountToDeposit = int(input('Please enter the amount to deposit: '))
        newBalance = deposit(userAccountNumber, amountToDeposit, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)

    if action == 'n':
        print("Create account:")
        name = input('Please enter the name: ')
        balance = int(input('Please enter the balance: '))
        password = input('Please enter the password: ')
        newAccount(name, balance, password)
        print('New account created')

    if action == 'w':
        print('Withdraw:')
        userAccountNumber = int(input('Please enter your account number: '))
        userPassword = input('Please enter the password: ')
        amountToWithdraw = int(input('Please enter the amount to withdraw: '))
        newBalance = withdraw(userAccountNumber, amountToWithdraw, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)

    if action == 's':
        for i in range(len(accountNamesList)):
            show(i)

    if action == 'q':
        break
print('The End')
