"""
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
"""


# Parent/Base Class
class Person:

    def __init__(self, name):
        self.name = name

    def displayName(self):
        print(self.name)


# Child/ derived Class
class Employee(Person):
    def __init__(self, name):
        # Person.__init__(self, name)
        # or use super() method . you not need to give self parameter when will used super() method
        super().__init__(name)


emp = Employee("Koushik Chandra Sarker")
emp.displayName()
