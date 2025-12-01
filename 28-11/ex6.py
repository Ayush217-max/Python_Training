def pallindrome(n,a):
    if n == n[::-1]:
        print("True")
    else:
        print("False")
    print(n.count(a))
    for ch in ['!',"@","#","%","$","^"]:
        n=n.replace(ch,"")
    print(n)

pallindrome("$AyuyA$","A")

