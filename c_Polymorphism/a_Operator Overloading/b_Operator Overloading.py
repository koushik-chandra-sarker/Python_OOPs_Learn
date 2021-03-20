"""

# if multiple methods having same name but different in parameters, it is known as Method Overloading.

class Employee:

    def __init__(self, baseSalary, extraIncome):
        self.baseSalary = baseSalary
        self.extraIncome = extraIncome


emp1 = Employee(10000, 2000)
emp2 = Employee(20000, 1000)

total = emp1 + emp2  # TypeError: unsupported operand type(s) for +: 'Employee' and 'Employee'

"""


# Now Create same class with operator overloading

class Employee:

    def __init__(self, baseSalary, extraIncome):
        self.baseSalary = baseSalary
        self.extraIncome = extraIncome

    # Overloading the {+} operator using __add__() method
    def __add__(self, other):
        totalBaseSalary = self.baseSalary + other.baseSalary
        totalExtraIncome = self.extraIncome + other.extraIncome
        emp3 = Employee(totalBaseSalary, totalExtraIncome)
        return emp3


emp1 = Employee(10000, 2000)
emp2 = Employee(20000, 1000)

total = emp1 + emp2  # it will be call __add__(self, other) method
print(total.baseSalary)  # Output: 30000
print(total.extraIncome)  # Output: 3000

"""
    You can overload any operator:
        - through __sub__()
        == through __eq__()
        > through __gt__()
        < through __lt__()
        etc.
"""

