# coments
# single line coments
a=10 # a is int var
b=20
c=a+b# add a+b
print(c)

# multi line coments
'''a=20
b=30
c=a+b
print(c)'''

# variables
# which will store the value
# rules
# 1)Dont start with digit or symbols
# 2)starting letter should be alphabets and underscore
# 3)case senstive

# Data types
# type of a value
# int, float, boolean, complex.
# adavnce data types
# list[],tuple(),set{},dictonary{}

# int
a=1
b=20
print(type(a),type(b))
# boolean
a=True
b=False
print(type(a),type(b))
# float
a=1.50
b=40.40
print(type(a),type(b))
# complex
a=10.2j
b=20.7j
print(type(a),type(b))
# string
a="deva"
b="bharath"
print(type(a),type(b))
# converted data types
a=10.4
print(int(a))

# conditional statements
Age=19
if Age>18:
    print("you can vote")
elif Age==18:
    print("you can vote")
else:
    print("wait")

if True:
    print("hii")
    if True:
        print("bye")
    else:
        print("")
else:
    print("")
# practice
if False:
    print("nenu vela")
elif False:
    print("velthunna")
else :
    print("ponu")
# nested if
if True:
    print("outer if")
    if True:
        print("inner if")
    else:
        print("inner else")
else:
    print("outer if")

# looping statements or itaretive statements
# for loop
a="devendra"
for k in a:
    print(k)
# while loop
# while True:
#     print("hii")#contuines reapeted

# for i in range(0,10,3):
#     print(i)

deva=1
while deva<15:
    print("haii",deva)
    deva+=1
# nested loop
for i in range(0,10):#i=1
    for j in range(0,20):#j=0-100
        print(i+j)




