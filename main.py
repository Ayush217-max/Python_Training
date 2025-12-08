import pymysql

conn = pymysql.connect(
    host= "localhost",
    user="root",
    password="1234",
    database="company_db"
)

cursor = conn.cursor()
cursor.execute("select * from employees")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()
