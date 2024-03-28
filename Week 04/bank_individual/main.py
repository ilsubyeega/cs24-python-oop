from account import *

joe = Account('Joe', 100, 'pass')
mary = Account('Mary', 12345, 'pass')

joe.show()
mary.show()

joe.deposit(50, 'pass')
mary.withdraw(200, 'pass')
mary.deposit(100, 'pass')

joe.show()
mary.show()
