class Mobile:
    def __init__(self,brand,ram,price):
        self.brand=brand
        self.ram=ram
        self.price=price
    def display(self):
        print("brand:",self.brand)
        print("ram:",self.ram)
        print("price:",self.price)
# for i in range(5):
obj=Mobile("apple","8gb",'400000')
obj.display()
obj=Mobile("onefles","10gb",'30000')
obj.display()




#Single inheritance
class Parent:
    def fun1(self):
        print("This is parent class")
class Child(Parent):
    def fun2(self):
        print("This is child class")
obj=Child()
obj.fun2()
obj.fun1()
print("-----------")
#Multiulevel inheritance
class Parent:
    def fun1(self):
        print("This is parent class")
class Child(Parent):
    def fun2(self):
        print("This is child class")
class Grandchild(Child):
    def fun3(self):
        print("this is grandchild class")
obj=Grandchild()
obj.fun3()
obj.fun2()
print("--------")
#Multiple inheritance
class Father:
    def fun1(self):
        print("This is father class")
class Mother:
    def fun2(self):
        print("this is mother class")
class Child(Father,Mother):
    def fun3(self):
        print("This is child class")
obj=Child()
obj.fun3()
obj.fun2()
obj.fun1()
print("--------")
#Hybrid inheritance
class School:
    def fun1(self):
        print("this is school class")
class Teacher1(School):
    def fun2(self):
        print("This is teacher1")
class Teacher2(School):
    def fun3(self):
        print("This is teacher2")
class Student(Teacher1,Teacher2):
    def fun4(self):
        print("This is student class")
obj=Student()
obj.fun4()
obj.fun3()
obj.fun2()
obj.fun1()



