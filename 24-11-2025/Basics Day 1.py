print("Hello World!")
# variables

name = "Ayush"
age = 22
salary = 4
print(name)
print(age)
print(salary)

# basic maths

a = 10
b = 3
print("Addition",a+b)
print("Divison",a/b)
print("Floor Division ",a//b)
print("Modulus",a%b)
print("power:",a**b)
for i in range(1,21):
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")
i=1
while i<=20:
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")
    i+=1
        

# if else

m = int(input("Enter your Marks:"))
if m >= 90:
    print("Grade A")
elif m >= 75:
     print("Grade B")
elif m >= 60:
     print("Grade C")
else:
     print("Grade D")

#loops

for i in range(1,6):
    print("Number",i)
i=1
while i<=5:
    print("Number:", i)
    i+=1

# break and continue

for i in range(10):
    if i == 5:
        break
    print(i)
for i in range(10):
    if i%2 == 0:
        continue
    print(i)

# List

fruits = ["apple", "mango", " banana"]
vegetables = ["potato", "cabbage","beans"]
marks = [98,97,92,93]

print(fruits[0])
print(marks[-1])
print(vegetables[2])

fruits.append("kiwi")
print(fruits)

fruits.insert(1,"orange")
print(fruits)

fruits.pop()
print(fruits)

fruits.pop(2)
print(fruits)

fruits.remove("apple")
print(fruits)

del fruits[1]
print(fruits)




