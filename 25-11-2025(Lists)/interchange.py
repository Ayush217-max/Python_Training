inp = input("Enter characters separated by spaces: ")
nums = list(inp.split())

nums[0],nums[-1]=nums[-1],nums[0]
print(nums)