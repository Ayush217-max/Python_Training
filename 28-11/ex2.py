generate_report = lambda name,amount: f'{name}:{amount} \n'
def print_report(name,amount):
    with open('report.txt','a') as f:
        f.write(generate_report(name,amount))

print_report('watch',20000)
print_report('watch2',20000)
print_report('watch3',20000)
print_report('watch4',20000)
