inp = input("Enter numbers separated by spaces: ")
nums = list(map(int, inp.split()))
l=sl=float('-inf')
for n in nums:
    if n > l:
        sl=l
        l=n
    elif n > sl and n!=l:
        sl=n

print(sl)