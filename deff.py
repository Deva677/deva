# functions means block of code
def deva(a,b,c):
    print("iam devevndra",a,b,c)
deva(1,2,3)

# orbitary perameters
def deva(*a,):
    print("I am Devendra",a)
deva(1,2,3)

# nested functions
def outer():
    print("outer")
    def inner():
       print("inner")
    inner()
outer()

def add(a,b):
    print(add)
def sub(a,b):
    print(sub)



#Arithmetic operations
a=10
b=30
c=a+b
print("The sum of two values is: ",c)
a=50
b=20
c=a-b
print("The subtraction value is:",c)
c=a*b
print("The multiplication value is:",c)
c=a/b
print("The division value is:",c)
c=a%b
print("The remainder is:",c)
c=a//b
print("The floor value is:",c)
c=a**2
print("The exponent of a is:",c)

#logical operator
#And or OR
a=10
b=20
if a==b or b==a:
    print("The values are equal")
else:
    print("The values are not equal")
Age=18
state="TS"
if Age>=18 and state=="Ap":
    print("They are eligible to vote")
else:
    print("They are not elgible to vote")
    if Age >= 18 or state == "Ap":
        print("They are eligible to vote")
    else:
        print("They are not elgible to vote")

#Membership operators
#in and not in
Fruits=("Apple","Grapes","Banana","Orange","Berry")
print("Apple" in Fruits)
print("Apple" not in Fruits)

#Type conversions
num1=30
print("The float value is:",float(num1))
num2=33.6
print("The integer value is:",int(num2))
num3=60
print("The bool value is:",bool(num3))
num4=True
print("The int value is:",float(num4))
num4=False
print("The float value is:",float(num4))

def fun1():
    print("deva bharath is good friends")
fun1()

def fun():
    print("deva bharath is good friends")