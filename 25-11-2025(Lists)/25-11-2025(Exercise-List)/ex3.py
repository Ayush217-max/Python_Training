list=[2,3,4,5,6,7,8]
n=int(input("Enter a number:"))
list[:n]=list[:n][::-1]
list[n:]=list[n:][::-1]
list[:]=list[:][::-1]
print(list)