list=[-4,-3,3,6,7,-2,5,-2,-7]
i=0
lis=[]
for i in range (len(list)):
    if list[i]<0:
        lis.append(list[i])
for i in range (len(list)):
    if list[i]>0:
        lis.append(list[i])

print(lis)