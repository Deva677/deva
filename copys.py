numbers=[1,2,3,4,5,6,7]
new_numbers=numbers
new_numbers[0]=9
print("numbers list:",numbers)
print("id of new numbers:",id(numbers))

print("new numbers:",new_numbers)
print("id of new numbers:",id(new_numbers))

import copy
old_list=[[1,2,3,4],[5,6,7,8,],[9,0,1,]]
new_list=copy.deepcopy(old_list)
new_list[0][2]="c"
print("old list;",old_list)
print("new list:",new_list)


class student:
    def displaystudent(self):
        print("Rollno:",self.Rollno,"name:",self.name)
s1=student(101,"deva")
s2=student(102,"bharaths1")
s1.displaystudent()
s2.displaystudent()









