with open("sample.txt","w") as f:
    f.write("Hello World This is Ayush \n")
    f.write("I am here to learn Python \n")

with open("sample.txt","r") as f:
    print(f.read())