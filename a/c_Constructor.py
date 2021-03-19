"""
In Python, the method the __init__() simulates the constructor of the class.

Two type of Constructor:
    1.Non-Parameterized Constructor,
    2.Parameterized Constructor

Python Default Constructor
    When we do not include the constructor in the class or forget to declare it,
    then that becomes the default constructor. It does not perform any task but initializes the objects.
"""


class Person:
    def __init__(self):
        print("This is non parametrized constructor")


person = Person()  # Output: This is non parametrized constructor


class User:

    def __init__(self, name):
        print("This is non parametrized constructor")
        print("Welcome %s" % name)


user = User("foo")
"""
Output:
        This is non parametrized constructor
        Welcome foo

"""
