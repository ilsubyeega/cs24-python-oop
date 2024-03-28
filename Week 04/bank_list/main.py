from account import *

if __name__ == '__main__':
    account_list = []

    joe = Account('Joe', 100, 'pass')
    account_list.append(joe)

    mary = Account('Mary', 12345, 'pass')
    account_list.append(mary)

    drake = Account('Drake', 500, 'pass')
    account_list.append(drake)

    pippi = Account('Pippi', 1000, 'pass')
    account_list.append(pippi)

    for account in account_list:
        account.show()

    account_list[0].deposit(50, 'pass')
    account_list[1].withdraw(345, 'pass')
    account_list[1].deposit(100, 'pass')

    for account in account_list:
        account.show()

t = {0: 'a', 2: 'b'}
print(list(t.keys()))
