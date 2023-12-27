strname="Bharath"
print(strname.upper())
print(strname.lower())
name="madhu"
print(name.capitalize())
name="deva vv"
name=name.count("v")
print("the repeated character  of v",name)
name="syeed hussain"
name=name.find("h")
print("find the postion",name)
name="vinod kumar"
name=name.rfind("k")
print("the index of k is",name)

 # strip
name="deva bharath"
name=name.strip()
print("the name of without space",name)
# lstrip
name="    bharath   deva   "
name=name.lstrip()
print("bharath",name,"bharath")
# rstrip
name="    bharath     deva   "
name=name.rstrip()
print("bharath",name,"bharath")
# replace
name="deva bharath madhu"
name=name.replace("deva","mani")
print(name)

num=78
if(num%2==0):
    print("the number is even")
else:
    print("the number is odd")
for numItr in range(2,50,2):
    print(" this is even number:",numItr)

    for numItr in range(1, 51, 2):
        print(" this is odd number:", numItr)

empname=input("enter the employee name")
print("the data stored in empname:",empname)
count=1
for strItr in empname:
    print("the vowels character in",count,"iteration")
    if(
         strItr.upper()=="A" or strItr.upper()=="E" or strItr.upper()=="I" or strItr.upper()=="O" or strItr.upper()=="U"):
        print("the vowels found and it is at position",count,"and the vowels",strItr)
    count+=1









