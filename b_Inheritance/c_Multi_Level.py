"""
Multi-Level inheritance is possible in python like other object-oriented languages.
Multi-level inheritance is archived when a derived class inherits another derived class.
There is no limit on the number of levels up to which, the multi-level inheritance is archived in python.
"""


class A:
    def showA(self):
        print("From A")


class B(A):
    def showB(self):
        print("From B")


class C(B):
    def showC(self):
        print("From C")


c = C()
c.showC()  # Output: From C
c.showB()  # Output: From B
c.showA()  # Output: From A
