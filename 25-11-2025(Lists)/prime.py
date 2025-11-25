inp = input("Enter numbers separated by spaces: ")
nums = list(map(int, inp.split()))

def prime(n):
    if n<2:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
    return True

num=[n for n in nums if prime(n)]
print(num)