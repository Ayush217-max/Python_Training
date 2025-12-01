generate_line = lambda user: f"Hello {user},welcome to the session we r learning Python"
## f for dynamic writing and  format string
def write_dynamic_line(filename,user):
    with open(filename,'w') as f:
        f.write(generate_line(user))

write_dynamic_line('users.txt','Ayush')
