import numpy as np
# addtion operater
list=np.array([[1,2,3,],[4,5,6]])
newlist=np.array([[1,2,3,],[4,5,6]])
result=list+newlist
print("Addtion value is:\n",result)
print("Addtion value is:\n",result.shape)
print("addtion value is:\n",result.size)
print("addtion value is:\n",result.dtype)
print("addtion value is:\n",result.ndim)


# subraction operater
list=np.array([[1,2,3],[4,5,6,],[7,8,9]])
newlist=np.array([[1,2,3],[4,5,6,],[7,8,9]])
result1=list-newlist
print("subtraction value is:\n",result1)

# multiplication operater
list=np.array([1,2,3])
newlist=np.array([4,5,6])
result2=list*newlist
print("multipliction value is:\n",result2)

# division operater
list=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
newlist=np.array([[1,2,3],[4,5,6],[7,8,9]])
result3=list/newlist
print("division value is:\n",result3)

# matrics mutiplication
list=np.array([[[1,2,3],[4,5,6]]])
newlist=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
result4=list@newlist
print("matrics multipication value is:\n",result4)

# slicing
list=np.array([[1,2,3],[4,5,6],[7,8,9]])
result5=list[1:2,1]
print("slicing value is:\n",result5)

list1=np.array([[1,2,3],[4,5,6],[7,8,9]])
result=list1[2:3,2]
print(result)

# reshape
array1=np.array([1,2,3,4,5,6,7,8])
print(array1.ndim)
result=array1.reshape(4,2)
print("reshape value:\n",result)

# sum
array2=np.array([1,2,3,4])
result=np.sum(array2)
print("sum value is:\n",result)

# minimum value
array2=np.array([[1,2,3],[4,5,6]])
result=np.min(array2)
print("mininum value:\n",result)

# maximum value
array2=np.array([[1,2,3],[4,5,6]])
result=np.max(array2)
print("maximum value:\n",result)

# tolist value
array3=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(type(array3))
result=array3.tolist()
print("tolist value is:\n",result)
print(type(result))

# sort
array4=np.array([[8,6,10],[8,9,0]])
result=np.sort(array4)
print("sort value:\n",result)
array4=np.array(["Devendra","Bharath","Nandhu","Varsha"])
result=np.sort(array4)
print("sort value in string value:\n",result)

# concatenations
array5=np.array([1,2,3,4,5])
array6=np.array([2,3,4,5])
result=np.concatenate((array5,array6))
print("concatenate value:\n",result)

# mean
array7=np.array([1,2,3,4,5])
result=np.mean(array7)
print("mean value is:\n",result)

# itemsize
array8=np.array([1,2,3,4,5,6])
result=array8.itemsize
print("itemsize value is:\n",result)

# transpose
array9=np.array([[1,2,3],[1,2,3]])
result=np.transpose(array9)
print("transpose value is:\n",result)

# arrange
array10=np.arange(10,50)
print("arrage value is:\n",array10)

array10=np.arange(10,50,3)
print("arrage value is two numbers skipt:",array10)

# astype
array11=np.array([[1,2,3],[1,2,3]])
result=array11.astype(float)
print("astype value is:\n",result)