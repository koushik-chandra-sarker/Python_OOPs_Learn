class Person:
    name = "foo"
    age = 35

    def display(self):
        print(self.name, self.age)


"""
Here, the self is used as a reference variable, which refers to the current class object.
 It is always the first argument in the function definition. However, 
 Using self is optional in the function call.
"""

# Creating an instance(Object) of the class

person = Person()
person.display()  # Output: foo 35


# Delete the Object
# We can delete the properties of the object or object itself by using the del keyword.

del person.age
del person.name
# person.display()   # Throw an AttributeError:

