"""
    In python, method overloading done with optional variable.
"""


class Calculator:

    def sum(self, a, b, c=None, d=None):
        if c != None and d != None:
            s = a + b + c + d
        elif c != None:
            s = a + b + c
        else:
            s = a + b
        print(s)


calc = Calculator()
calc.sum(4, 3)  # Output: 7
calc.sum(4, 3, 10)  # Output: 17
calc.sum(4, 3, 10, 5)  # Output: 22
