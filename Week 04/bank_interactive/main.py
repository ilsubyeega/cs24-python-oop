from account import Account

if __name__ == '__main__':
    account_list = []
    while True:
        print("""
            b: Get the balance
            d: Deposit
            n: Create a new account
            w: Withdraw
            s: Show all accounts
            q: Quit
        """)

        action = input('What do you want to do? ')
        action = action.strip().lower()
        print()

        if action == 'b':
            print('Get Balance:')
            accountNumber = int(input('Please enter the account number: '))
            userPassword = input('Please enter the password: ')
            theBalance = account_list[accountNumber].get_balance(userPassword)
            if theBalance is not None:
                print('Your balance is:', theBalance)
        elif action == 'd':
            print('Deposit:')
            accountNumber = int(input('Please enter the account number: '))
            userDepositAmount = input('Please enter amount to deposit: ')
            userDepositAmount = int(userDepositAmount)
            userPassword = input('Please enter the password: ')

            newBalance = account_list[accountNumber].deposit(userDepositAmount, userPassword)
            if newBalance is not None:
                print('Your new balance is:', newBalance)
        elif action == 'n':
            print('Create account:')
            name = input('Please enter the name: ')
            balance = int(input('Please enter the balance: '))
            password = input('Please enter the password: ')
            account_list.append(Account(name, balance, password))
            print('New account created')
        elif action == 'w':
            print('Withdraw:')
            accountNumber = int(input('Please enter the account number: '))
            userWithdrawAmount = input('Please enter amount to withdraw: ')
            userWithdrawAmount = int(userWithdrawAmount)
            userPassword = input('Please enter the password: ')

            newBalance = account_list[accountNumber].withdraw(userWithdrawAmount, userPassword)
            if newBalance is not None:
                print('Your new balance is:', newBalance)
        elif action == 's':
            print('Show:')
            for account in account_list:
                account.show()
        elif action == 'q':
            break
        else:
            print('Invalid action. Please try again.')
