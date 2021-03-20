"""
If derived (child class) has the same method as declared in the parent class, it is known as method overriding.
"""


class A:
    def greeting(self):
        print("Welcome class A")


class B(A):
    pass


b = B()

b.greeting()  # Output: Welcome class A


# Now Write the same code with method overriding

class A:
    def greeting(self):
        print("Welcome class A")


class B(A):
    def greeting(self):
        print("Welcome class B")


b = B()

b.greeting()  # Output: Welcome class B
