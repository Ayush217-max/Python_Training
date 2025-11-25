tup=(10,(20,30),(40,(50,60)))
def intprint(tup,a):
    if a>=len(tup):
        return
    if type(tup[a])==int:
        print(tup[a])
    else:intprint(tup[a],0)
    intprint(tup,a+1)


intprint(tup,0)