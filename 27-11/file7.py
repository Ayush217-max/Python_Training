with open("notes.txt","r") as f:
    for line in f:
        if "Python" in line:
            print(line)
