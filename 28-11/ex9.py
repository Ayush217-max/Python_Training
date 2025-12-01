def new_list(names):
    ans = []
    for i in names:
        if len(i)>4:
            ans.append(i)
    return ans

print(new_list(["Ayush","Mishra","Hey"]))

