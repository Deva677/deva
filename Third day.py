# COMPARISION OPERATORS
x=4
y=6
z=8
result=(x==y),(y==z),(z==x)
print(result)

x=4
y=3
z=6
result=(x!=y),(y!=z),(z!=x)
print(result)

x=4
y=3
z=6
result=(x>y),(y>z),(z>x)
print(result)

x=4
y=3
z=6
result=(x<y),(y<z),(z<x)
print(result)

x=4
y=3
z=6
result=(x<=y),(y<=z),(z<=x)
print(result)

x=4
y=3
z=6
result=(x>=y),(y>=z),(z>=x)
print(result)

#logical operators
# And gate
a=5
b=7
result=(a<b and b<a)#( False True)
print(result)
a=10
b=20
result=(a<b and a>b)#(TRUE FALSE)
print(result)
a=30
b=20
result=(b<a and a>b)#(True True)
print(result)
a=20
b=10
rsult=( a>20 and a<20)#(False False)
print(result)


a=5
b=7
result=(a<b or b<a)#( False True)
print(result)
a=10
b=20
result=(a<b or a>b)#(TRUE FALSE)
print(result)
a=30
b=20
result=(b<a or a>b)#(True True)
print(result)
a=8
b=9
result=( a<2 or b>10)#(False False)
print(result)

# not gate
a=8
b=9
result=(not( a<2 , b>10))#(False False)
print(result)

a=6
b=7
result=(not( a<9 and b>10))
print(result)

# Membership operators
x=["deva, bharath"]
print("bharath" in  x)

# membership operators
string="deva"
print("the character e is in string:",'e' in string)

string="deva"
print("the character e is in string:",'o' in string)
# not in
string="deva"
print("the character e is in string:",'o' not in string)

string="deva"
print("the character e is in string:",'d' not in string)
# condtions satement
# if
print("result")
marks=3
if marks >= 4:
    print("pass")
# if and else
print("result")
marks=50
if marks >= 40:
    print("pass")
else:
    print("fail")

# if and elif
print("result")
marks=30
if marks >= 35:
    print("pass")
elif marks < 40 and 50:
    print("average")

# if  else and elif
print("result")
marks=35
if marks >= 35:
    print("good marks")
elif marks > 40 and 50:
    print("average")
else:
    print("pass")
