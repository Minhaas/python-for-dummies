student_grades = [9.0, 8.25, 7.3, 10, 6.3, 10.0, 8.5, 8.85, 8.92, 9.3, 9.71, 9.83]
max_value = max(student_grades)
print("Max value is: ",max_value)

student_count = student_grades.count(10)
print("Number of 10's are" ,student_count)

mySum = sum(student_grades)
mylen = len(student_grades)
meanValue = mySum/mylen
print("Average grade is: ",meanValue)

seconds = [1.2323442655, 1.4534345567, 1.023458894]
current = 1.10001399445
#Append current to list 

seconds.append(current)
print("Appended list is: ",seconds)
