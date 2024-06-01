# HOMEWORK: 근로자 1명 늘리기
class Employee():
    def __init__(self, name, title, ratePerHour=None):
        self.name = name
        self.title = title
        if ratePerHour is not None:
            ratePerHour = float(ratePerHour)
        self.ratePerHour = ratePerHour

    def getName(self):
        return self.name

    def getTitle(self):
        return self.title

    def payPerYear(self):
        pay = 52 * 5 * 8 * self.ratePerHour
        return pay


class Manager(Employee):
    def __init__(self, name, title, salary, reportsList=None):
        self.salary = float(salary)
        if reportsList is None:
            reportsList = []
        self.reportsList = reportsList
        super().__init__(name, title)

    def getReports(self):
        return self.reportsList

    def payPerYear(self, giveBonus=False):
        pay = self.salary
        if giveBonus:
            pay = pay + (.10 * self.salary)
            print(self.name, 'gets a bonus for good work')
        return pay       




oEmployee1 = Employee('Joe Schmoe', 'Pizza Maker', 16)
oEmployee2 = Employee('Chris Smith', 'Cashier', 14)
oEmployee3 = Employee('Joe Biden', 'USA President', 100)
oManager = Manager('Sue Jones', 'Pizza Restaurant Manager',
                             55000, [oEmployee1, oEmployee2, oEmployee3])

print('Employee name:', oEmployee1.getName())
print('Employee salary:', '{:,.2f}'.format(oEmployee1.payPerYear()))
print('Employee name:', oEmployee2.getName())
print('Employee salary:', '{:,.2f}'.format(oEmployee2.payPerYear()))
print()

managerName = oManager.getName()
print('Manager name:', managerName)

print('Manager salary:', '{:,.2f}'.format(oManager.payPerYear(True)))
print(managerName, '(' + oManager.getTitle() + ')', 'direct reports:')
reportsList = oManager.getReports()
for oEmployee in reportsList:
    print('   ', oEmployee.getName(),
            '(' + oEmployee.getTitle() + ')')