from datetime import datetime
generate_report = lambda name,status: f'Name:{name} Time:{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, Status:{status} \n'
def print_report(name,status):
    with open('attendance.log','a') as f:
        f.write(generate_report(name,status))

print_report('Ayush',"Present")
print_report('Diksha',"Absent")
print_report('abhi',"Absent")
print_report('Anmol',"Present")
