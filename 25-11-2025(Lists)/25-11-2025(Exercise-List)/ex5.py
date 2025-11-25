list=[[1,2],[3,4],[5,6]]
ans=[]
for i in list:
    for j in range(len(i)):
        ans.append(i[j])


print(ans)