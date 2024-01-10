# creating a read fil
import os
filepath="c:\\samples\empdata.txt"
name=open(filepath,"r")
mydata=name.read()
print("The  present in Empdata file:\n",mydata)

# readline
name=open(filepath,"r")
name.seek(0)
mydata=name.readline(8)
print("The readline is:",mydata)
name.close()

# readlines
name=open(filepath,"r")
name.seek(0)
mydata=name.readlines()
print("thereadlines is:",mydata)

# write
import os
filepath="c:\\samples\empdata_1.txt"
name=open(filepath,"w+")
mydata="Deva is farmer.he is good worker"
name.write(mydata)
# empFd.close()#remove comment

# write lines
items=[20,30,40,50,60,"madhu","deva"]
name.writelines(str(items))
name.close()

