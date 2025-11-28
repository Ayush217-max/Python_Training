import csv

with open("students.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        name,marks=row[0],row[1]
        print(name,marks)