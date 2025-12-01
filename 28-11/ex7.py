def remove_duplicate(list):
    ans = []
    for l in list:
        if l in list and l not in ans:
            ans.append(l)
    print(ans)

remove_duplicate([1,2,3,4,2,8,0,3,5,6,5,6,7,8,9])