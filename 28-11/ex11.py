a={1,2,3,4}
b={2,3,4,5,6}
print((a|b)-(a&b))

s=set()
l=[1,2,3,4,5,6,7,6,5,4,8,9,0]
for i in l:
    if l.count(i)==2:
        s.add(i)

print(s)