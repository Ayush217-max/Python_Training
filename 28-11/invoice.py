import csv

generate_invoice= lambda a,b,c: f'{a} : {b*c} \n'

with open ('orders.csv','r') as f, open('invoice.txt','a') as g:
    reader = csv.reader(f)
    s=0
    for row in reader:
        item,quantity,price = row[0],row[1],row[2]
        s += (quantity*price)
        g.write(generate_invoice(item,quantity,price))
    g.write("Invoice Total:"+str(s)+"\n")