"""
If a_Class Object Constructor class has multiple methods having same name but different in parameters,
 it is known as Method Overloading.
"""


class Calculator:

    def sum(self, a, b):
        return a + b

    def sum(self, a, b, c):
        return a + b + c


calc = Calculator()
calc.sum(4, 3)
calc.sum(4, 3, 10)

"""
    This code Throw an error.
    Because, In Python method overloading concept is not present like java, c++ or c language.
    But There is a different way to overload method.
    
    I show this way in { b_Method Overloading.py } file
    
"""
