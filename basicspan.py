import numpy as np
import pandas as pd
marks=pd.Series([20,30,40,50,60])
print("marks index\n",marks)
# series
student=pd.Series({"deva":20,"madhu":30,"ravi":60,"chandu":70})
print("students details is\n",student)
print("maxmimum values is:",student.max())
print("minimum values is:",student.min())
print("student size value is:",student.size)
print("student head value\n",student.head())
print("student tail value is\n:",student.tail(2))
print("student count value is\n:",student.count())
student1=pd.Series([10,20,39,40,"ch",30],index=[0,1,2,3,5,7])
student2=pd.Series([10,20,39,60,40,80],index=[0,1,2,3,6,7])
result=student1+student2
print("add two values is\n:",result)

# index
a=[1,2,3]
valarry=pd.Series(a,index=["x,","y","z"])
print("values\n",valarry)
var=pd.Series([20,30,40,50],name="student")
print("student value is\n",var)



