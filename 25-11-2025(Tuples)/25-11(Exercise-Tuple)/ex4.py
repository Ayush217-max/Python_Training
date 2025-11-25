tup=(1,2,3,4,5,6,7,8,9,10)
val=int(input("Enter a number: "))
for i in range(0,len(tup)):
    if tup[i]==val:
        print(i)