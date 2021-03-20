"""
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
"""


# Parent/Base Class
class A:

    def showInfo(self):
        print("Show Method from class A")


# Child/ derived Class
class B(A):

    def Display(self):
        print("Display Method from class B")


b = B()
b.showInfo()  # Output: Show Method from class A
b.Display()  # Output: Display Method from class B
