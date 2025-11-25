inp = input("Enter numbers separated by spaces: ")
nums = list(map(int, inp.split()))
even =[]
odd = []
for n in nums:
    if n % 2 == 0:
        even.append(n)
    else: odd.append(n)

print("Even:",even)
print("Odd:",odd)