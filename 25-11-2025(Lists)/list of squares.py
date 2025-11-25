inp = input("Enter numbers separated by spaces: ")
nums = list(map(int, inp.split()))
num2=[]
for i in range(len(nums)):
    num2.append(nums[i]**2)


print(num2)