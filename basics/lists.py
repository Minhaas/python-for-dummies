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

#Remove items from list
seconds.remove(1.2323442655)
print(seconds)

#Accessing list
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])
print(serials[0], serials[2], serials[5])

#Accessing and appending 
workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])
print("Appended list: ",workdays)

#slicing
print("Sliced list" ,workdays[1:3])
print("First three elements (Slicing): ",workdays[:3])
print("Last three (Negative index Slicing): ",workdays[-3:])
