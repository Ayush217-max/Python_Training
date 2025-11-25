tup=(1,2,3,4,9,5,6)
for i in range(1,len(tup)-1):
    if tup[i]>tup[i-1] and tup[i]<tup[i+1]:
        continue
    else:
        break
if i==len(tup)-2:
    print("True")
else:
    print("False")