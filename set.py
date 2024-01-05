#Tuple
#empty tuple
mytuple=()
print(mytuple)
#empty tuple
mytuple=tuple()
print(mytuple)
mytuple=(1,2,3,4,5,6)
print(mytuple)
#list to tuple convertion
mytuple=tuple(["deva","bharath","madhu","mani"])
print(mytuple)
#Count
mytuple=(1,2,3,3,2,3,3,"deva","manoj","nithin","ram","deva")
mytuple=mytuple.count("deva")
print(mytuple)
#index
mytuple=("raju","tuple","masthan","deva")
mytuple=mytuple.index("deva")
print(mytuple)
#length
mytuple=("raju","tuple","masthan","deva")
mytuple=len(mytuple)
print(mytuple)
#forward slicing
mytuple=tuple(["raju","tuple","masthan","deva"])
print(mytuple)
mytuple=mytuple[0:5]
print(mytuple)
mytuple=tuple(["raju","tuple","masthan","deva"])
print(mytuple)
mytuple=mytuple[0:5]
print(mytuple)

#while loop
c=0
while c<10:
    c += 1
    print(c, "Hello world")
    if c==3:
        print("My name is deva")

#break
c=0
while c<10:
    c += 1

    print(c, "Hello world")
    if c==3:
        print("My name is deva")
    break









