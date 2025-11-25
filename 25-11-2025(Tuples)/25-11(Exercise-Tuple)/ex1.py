tup=("hey",22,"here")
l1=[]
l2=[]
for i in tup:
    if type(i)==str:
        l1.append(i)
    else:
        l2.append(i)

print(tuple(l1))
print(tuple(l2))
