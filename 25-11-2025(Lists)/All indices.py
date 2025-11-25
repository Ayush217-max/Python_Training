inp = input("Enter numbers separated by spaces: ")
nums = list(map(int, inp.split()))
n = int(input("Enter the number "))
pnum = []
for i in range(len(nums)):
    if nums[i] == n:
        pnum.append(i)


print(pnum)