
x=input("Enter the 1st number:")
y=input("Enter the 2nd number:")
a=int (x)
b=int(y)
z=a+b
print("Results",z)
# same ex:
x=int(input("Enter the 1st number:"))
y=int(input("Enter the 2nd number:"))
a=x * y
print("Result",a)

x=input("enter the char:")
count=x[3]
print("result",count)

x=input("enter any char:")
if len(x)!=1:
    print("enter the singal char:")
    x=input("enter any char:")
print(x)

x=input("enter any char:")
while len(x)!=1:
    print("enter the singal char:")
    x=input("enter any char:")
print(x)
input()


# lopping practice
for k in range(0,20):
    print(k)

k="deva bharath"
for k in range(1,10):
    print("deva bharath",)
    print(k)

deva=1
while deva<15:
    print("amma",deva)
    deva+=1

