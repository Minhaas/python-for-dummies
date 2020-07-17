student = {"Praj": 8.85, "Minhaas": 7.95, "Prithvi": 8.2}

mySum = sum(student.values())
mylen = len(student)
myMean = mySum / mylen

print("Average using dictionaries is :", myMean)

for students in student.values():
    print(students)

for students in student:
    print(students)