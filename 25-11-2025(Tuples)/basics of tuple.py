#packing unpacking should match the number of elements
data = 10,20,30
a,b,c=data
print(a,b,c)
####
employee=("ayush",22,("kochi","India"))
print(employee[2][0])
# max min
nums=(33,20,30,60,50)
l=float('-inf')
s=float('inf')
for n in nums:
    if n>l:
        l=n
    if n<s:
        s=n
print("Max:",l)
print("Min:",s)