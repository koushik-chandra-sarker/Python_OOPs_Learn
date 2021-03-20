"""
    a = b+c, here a_,b,c are {operand} & {+} is operator

    Let see some general example

    I perform operator overloading in {b_Operator Overloading.py} file

"""

a = 30
b = 10

c = a + b  # here, + operator internally called int.__add__(a, b) method

print(c)  # Output: 40
d = int.__add__(a, b)
print(d)  # Output: 40
"""
a + b and int.__add__(a, b) both are the same

-> many in_build method are there in int object
        Ex. __abs__(), __sub__(), __mul()__ etc.
"""

# Another Example of a String

a = "Hello"
b = "Python"

print(a + b)  # Output: HelloPython
print(str.__add__(a, b))  # Output: HelloPython

print(a == b)  # Output: False
print(str.__eq__(a, b))  # Output: False

"""
 Here, a + b and str.__add__(a, b) both are the same
 Here, a == b and str.__eq__(a, b) both are the same
 
"""

# See the "b_Operator Overloading.py
