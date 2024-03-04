import numpy as np
student=np.loadtxt("c:/StudentData.txt",delimiter=",",skiprows=1,dtype=int)
print(student)
student=np.genfromtxt("c:/StudentData.txt",skip_header=1,dtype=int)
print(student)
StudentData=np.loadtxt("C:/StudentData.txt",dtype=int,delimiter=",",skiprows=1,unpack=True)
print(StudentData)
StudentData=np.genfromtxt("c:/StudentData.txt",skip_header=1,dtype=int,filling_values=10)
print(StudentData)
#StudentData=np.savetxt("C:/StudentnewData",StudentData,delimiter="@",fmt="%i")

