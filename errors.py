# error handling
# syntax error
a=""""will to
my village""
print(a)

# indentation error
for i in range(10):
print(i)

# index errror
a=[20,40,40,60,]
print(a[5])

# name error
a,b,c=10,20,30
print(e)

# type error
a=("deva")
b=20
c=a+b
print(c)

# # value error
a="deva"
b=int(a)

# expection
try:
    a = "deva"
    b = int(a)
except TypeError:
    print("type error")
except ValueError:
    print("ValueError")
else:
    print("no error")
finally:
    print("over")





