class Bank:
    def fun1(self,Name,withdral,Date,Age,Branch):
        self.Name=Name
        self.withdral=withdral
        self.Date=Date
        self.Age=Age
        self.Branch=Branch
        print("Name",Name)
        print("withdral", withdral)
        print("Date", Date)
        print("Age", Age)
        print("Branch",Branch )
class mainbranch(Bank):
    def fun2(self,signature):
        self.signature=signature
        print("signature",signature)
obj=mainbranch()
obj.fun2("Devendra")
obj.fun1("deva",200000,25/1/2023,23,"kphb" )
# multilevel
class Bank:
    def fun1(self,Name,withdral,Date,Age,Branch):
        self.Name=Name
        self.withdral=withdral
        self.Date=Date
        self.Age=Age
        self.Branch=Branch
        print("Name",Name)
        print("withdral", withdral)
        print("Date", Date)
        print("Age", Age)
        print("Branch",Branch )
class mainbranch(Bank):
    def fun2(self,signature):
        self.signature=signature
        print("signature",signature)
class Publicbank( mainbranch,Bank):
    def fun3(self,type):
        self.type=type
        print("type",type)
obj=Publicbank()
obj.fun3("savingaccount")
obj.fun2("Devendra")
obj.fun1("deva",200000,25/1/2023,23,"kphb" )
# multiple
class Bank:
    def fun1(self,Name,withdral,Date,Age,Branch):
        self.Name=Name
        self.withdral=withdral
        self.Date=Date
        self.Age=Age
        self.Branch=Branch
        print("Name",Name)
        print("withdral", withdral)
        print("Date", Date)
        print("Age", Age)
        print("Branch",Branch )
class mainbranch:
    def fun2(self,signature):
        self.signature=signature
        print("signature",signature)
class privatebank(Bank,mainbranch):
    def fun3(self,private):
        self.private=private
        print("private",private)

obj=privatebank()
obj.fun3("take")
obj.fun2("Devendra")
obj.fun1("deva",200000,25/1/2023,23,"kphb" )

print("--------------")



