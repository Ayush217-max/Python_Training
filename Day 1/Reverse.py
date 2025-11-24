a = int(input("Enter n:"))
num=0
s=0
while a>0:
    s=a%10
    num=num*10+s
    a=a//10
    
print("Reversed number",num)



