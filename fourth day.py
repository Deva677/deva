strname="DEVENDRA k"
strRollno="199H"
straddress='''kpbh,
            kukatpally,
            hyd-500081'''
print(len(strname))
print(len(strRollno))
print(len(straddress))
print(strname[0:5])
print(strname[-5:-2])
print(strname[::-1])
# STRING METHOD
strname="Bharath"
print(strname.upper())
print(strname.lower())
strname="devendra"
print(strname.isupper())
print(strname.islower())
strname="madhu"
print(strname.capitalize())
strname="masthan"
print(strname.isalpha())
strname="raju"
print(strname.isalnum())
name="devendra"
name=name.count("e")
print("repeated character of e is:",name)
name="bharath gftyjhxffcvbnmnvc gjvbh"
name=name.index("n")
print("the postion of a",name)
name="syeed hussain"
name=name.find("h")
print("find the postion",name)
name="vinod kumar"
name=name.rfind("k")
print("the index of k is",name)

# strip
name=("    DEVENDRA   BHARTH")
print("the name with space",(name))
name=name.strip()
print("the name of without space",name)
# lstrip
name="    bharath       deva   "
name=name.lstrip()
print("bharath",name,"bharath")
# rstrip
name="    bharath     deva   "
name=name.rstrip()
print("bharath",name,"bharath")
# replace
name="i like travelling"
name=name.replace("travelling","beach")
print(name)
# split
name="i like travelling"
name=name.split( )
print(name)
# join
names=("deva","bharath","mani")
best="pavan".join(names)
print(best)


# task
# take any input string and seperate numbers alphabets and special characters
input_string = "abc123@def456!ghi789"
result = separate_characters(input_string)
print("Numbers:", result['numbers'])
print("Alphabets:", result['alphabets'])
print("Special Characters:", result['special_characters'])


