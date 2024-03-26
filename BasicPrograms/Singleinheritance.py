class parent:
    def function1(self):
        print("this is function one")
class child(parent):
    def function2(self,a):
        print("this is function two")
        print(a)
    b=20
y=child()
y.function1()
y.function2(10)
print(y.b)


