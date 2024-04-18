import mysql.connector as mysql
db = mysql.connect(user='root', password='password', host='127.0.0.1')
with db.cursor() as cur:
    cur.execute('USE Company;')
    cur.execute("SELECT * FROM Employees;")
    data = cur.fetchall()
    print(data) # [(1, 'Ahmed', 'Khaled'), (2, 'Salim', 'Hassan')]
    first_names = [name[1] for name in data] 
    print(first_names) # ['Ahmed', 'Salim']
db.close()