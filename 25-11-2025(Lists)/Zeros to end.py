inp = input("Enter numbers separated by spaces: ")
nums = list(map(int, inp.split()))
nums1=[]
i=0
for n in nums:
    if n!=0:
        nums1.append(n)
        i=i+1

while i<len(nums):
    nums1.append(0)
    i=i+1


print(nums1)