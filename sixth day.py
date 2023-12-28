# # forward
# empname=input("enter the employee name")
# print("the data stored in empname:",empname)
# count=1
# for strItr in empname:
#     print("the vowels character in",count,"iteration")
#     if(
#          strItr.upper()=="A" or strItr.upper()=="E" or strItr.upper()=="I" or strItr.upper()=="O" or strItr.upper()=="U"):
#         print("the vowels found and it is at position",count,"and the vowels",strItr)
#     count+=1
#
#  # task
# name=input("enter the name")
# count=1
# d="a","e","i","o","u","A","E","I","O","U"
# check=name[::-1]
# for i in check:
#     if i in d:
#         print("the vowels found and it is at position",count,"and the vowels",i)
#     count+=1

# append add name nym
nums=[1,2,3,4,56,]
nums.append("deva")
print(nums)

# extend add multiple names
names=["deva","mani","bharath","arun","sree"]
names.extend(["madhu","mahi"])
print(names)

# replace names
names=['mahesh','suresh','rajesh']
names[0:2]=["deva","bharath"]
print(names)

# remove any name
fruits=['banana','orange','lemon','grapes']
fruits.pop(2)
print(fruits)

 # remove any name
fruits=['banana','orange','lemon','grapes']
fruits.remove('banana')
print(fruits)

# clear varibles
fruits=['banana','orange','lemon','grapes']
fruits.clear()
print(fruits)

# sort first upper second lower
fruits=['banana','orange','Lemon','Grapes']
fruits.sort()
print(fruits)
# same
nums=[23,45,567,67,8,9,2,1,]
nums.sort(reverse =True)
print(nums)
# same
nums=[23,45,76,8,6,4,2,]
nums.sort()
print(nums)

# duplicates count
names =("deva","bharath","deva","madhu")
names=names.count("deva")
print(names)

# tuple list of names
names=("deva","bharath","deva","madhu")
namelist=list(names)
print(namelist)

names=("deva","bharath","deva","madhu")
namelist.append("raju",)
name=tuple(namelist)
print(name)

# set duplicate value is not allow
flowers={"rose","jasmin",22,True}
print(len(flowers))
flowers={"rose","jasmin",22,True}


# Dictionary
address={"fname": "deva","lname":"bharath","mobile":"56746890"}
print(address)

# add address
address={"fname": "deva","lname":"bharath","mobile":"56746890"}
address.update({'age':30})
print(address)

# clear
person={"fname": "deva","lname":"bharath","mobile":"56746890"}
person.clear()
print(person)

# delete
person={"fname": "deva","lname":"bharath","mobile":"56746890"}
del person["lname"]
print(person)

# pratice
# length find out
string=input("enter the length of string")
lenofstring=len(string)
print(lenofstring)

def find_repeated_characters_for_loop(string):
    repeated_chars = []
    for i in range(len(string)):
        current_char = string[i]
        if current_char in string[i+1:] and current_char not in repeated_chars:
            repeated_chars.append(current_char)
    return repeated_chars

string = "level"
result = find_repeated_characters_for_loop(string)
print("Repeated characters (For Loop):", result)



