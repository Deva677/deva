# FUNCTIONS:
# type1 whithout input and without output
def add():
    num1=20
    num2=40
    sum=num1+num2
    print("without input sum is :",sum)
    #return sum;
add()

# type2 with input and without output
def sub(num1=20,num2=60):
    sum=num1-num2
    print("Withinput and without output :",sum)
sub(50,5)

# type3 without input and with output
def mult():
    num1=40
    num2=60
    sum=num1*num2
    return sum
result= mult()
print("witout input and with output :",result)

# type4 with input and with output
def div(num1,num2):
    num3=6
    sum=num1/num2
    return sum
result = div(12,3)
print("With input and with output :",result)


def add(num1,num2):
    result=num1+num2
    print(result)
add(50,78)

