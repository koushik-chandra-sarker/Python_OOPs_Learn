
class A:
    def showA(self):
        print("From A")


class B:
    def showB(self):
        print("From B")


class C(A, B):
    def showC(self):
        print("From C")


c = C()
c.showC()  # Output: From C
c.showB()  # Output: From B
c.showA()  # Output: From A
