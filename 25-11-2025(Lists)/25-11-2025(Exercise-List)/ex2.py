list=[1,2,3,2,4,1,5,1]
ans=[]
for i in list:
    if list.count(i)>1 and i not in ans:
        ans.append(i)

print (ans)