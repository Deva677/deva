class Parent:
    def fun1(self):
     print("This is parent class1")
     print("This is parent class2")
class Child(Parent):
    def fun1(self):
        print("This is child class1 ")
        print("This is child class2 ")
        print("This is child class3 ")
        super().fun1()
Child_obj=Child()
Child_obj.fun1()
# Child_obj.fun1()
class parentclass:
    def parent_method(self):
        print("This is parent class")
class childclass(parentclass):
    def parent_method(self):
        super().parent_method()
    def child_method(self):
        print("This is child class")
        super().parent_method()
child_obj=childclass()
child_obj.child_method()
# child_obj.parent_method()
#Interface
class Chandu:
    name ="abc"
    Age = 18
class Parent:
    def fun1(self):
     print("This is parent class1")
     print("This is parent class2")
class Child(Parent):
    def fun1(self):
        print("This is child class1 ")
        print("This is child class2 ")
        print("This is child class3 ")
        super().fun1()
Child_obj=Child()
Child_obj.fun1()
# Child_obj.fun1()
class parentclass:
    def parent_method(self):
        print("This is parent class")
class childclass(parentclass):
    def parent_method(self):
        super().parent_method()
    def child_method(self):
        print("This is child class")
        super().parent_method()
child_obj=childclass()
child_obj.child_method()
# child_obj.parent_method()
#Interface
class Chandu:
    name ="abc"
    Age = 18
    DOB = "10-Jan-2024"
    def _init_(self,name,Age,DOB):
        self.name=name
        self.Age=Age
        self.DOB=DOB
    def display(self):
        pass
obj=Chandu("Chandu",21,"03/07/2002")
obj.display()
class deva:
    Qualification="Btech"
    Percentage=70
    def _init_(self,Qualificaton,Percentage):
        self.Qualification=Qualificaton
        self.Percentage=Percentage

    def display(self):
        pass
obj=deva("btech",70)
obj.display()