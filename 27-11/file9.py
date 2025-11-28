with open("numbers.txt","w") as f:
    for i in range(1,11):
        f.write(f'{i**2} \n')

        