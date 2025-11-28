with open("notes.txt", "r") as src, open("sample.txt", "w") as dst:
    dst.write(src.read())


print("file copied")