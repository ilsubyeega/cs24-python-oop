account0Name = ''
account0Balance = 0
account0Password = ''
account1Name = ''
account1Balance = 0
account1Password = ''
nAccounts = 0


def newAccount(accountNumber, name, balance, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        account0Name = name
        account0Balance = balance
        account0Password = password
    if accountNumber == 1:
        account1Name = name
        account1Balance = balance
        account1Password = password


def show():
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if account0Name != '':
        print('Account 0')
        print('       Name', account0Name)
        print('       Balance:', account0Balance)
        print('       Password:', account0Password)
        print()
    if account1Name != '':
        print('Account 1')
        print('       Name', account1Name)
        print('       Balance:', account1Balance)
        print('       Password:', account1Password)
        print()


def getBalance(accountNumber, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if password != account0Password:
            print('Incorrect password')
            return None
        return account0Balance
    if accountNumber == 1:
        if password != account1Password:
            print('Incorrect password')
            return None
        return account1Balance

def deposit(accountNumber, amountToDeposit, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return None

    if accountNumber == 0:
        if password != account0Password:
            print('Incorrect password')
            return None

        account0Balance = account0Balance + amountToDeposit
        return account0Balance

    if accountNumber == 1:
        if password != account1Password:
            print('Incorrect password')
            return None

        account1Balance = account1Balance + amountToDeposit
        return account1Balance

def withdraw(accountNumber, amountToWithdraw, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None

    if accountNumber == 0:
        if password != account0Password:
            print('Incorrect password for this account')
            return None
        if amountToWithdraw > account0Balance:
            print('You cannot withdraw more than you have in your account')
            return None

        account0Balance = account0Balance - amountToWithdraw
        return account0Balance

    if accountNumber == 1:
        if password != account1Password:
            print('Incorrect password for this account')
            return None
        if amountToWithdraw > account1Balance:
            print('You cannot withdraw more than you have in your account')
            return None

        account1Balance = account1Balance - amountToWithdraw
        return account1Balance


# initialize accounts
newAccount(0, "Stick", 100, 'dic')
newAccount(1, "Drake", 200, 'coc')

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]
    print()
    if action == 'b':
        print('Get Balance:')
        accountNumber = int(input('Please enter the account number: '))
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(accountNumber, userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)
    elif action == 'd':
        print('Deposit:')
        accountNumber = int(input('Please enter the account number: '))
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')

        newBalance = deposit(accountNumber, userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)
    elif action == 'w':
        print('Withdraw:')
        accountNumber = int(input('Please enter the account number: '))
        userWithdrawAmount = input('Please enter amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')

        newBalance = withdraw(accountNumber, userWithdrawAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)
    elif action == 's':
        print('Show:')
        show()
    elif action == 'q':
        break