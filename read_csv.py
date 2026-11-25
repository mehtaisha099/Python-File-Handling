import csv

file = open("students.csv", "r")

reader = csv.reader(file)

print("Student Details:")
print("----------------")

for row in reader:
    print("Name:", row[0], "| Age:", row[1], "| Course:", row[2])

file.close()