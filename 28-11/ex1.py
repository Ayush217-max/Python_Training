generate_line = lambda user: f'''Hello {user} 
We are glad to inform you that you have been certified for successful completion of you
Python Course availed by EYGDS'''

with open("students.txt","r") as f:
    names = [l.strip() for l in f.readlines()]
    print(names)

for n in names:
    with open(f'certificate{n}.txt', "w") as f:
        f.write(generate_line(n))


