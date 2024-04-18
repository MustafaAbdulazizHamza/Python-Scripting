import mysql.connector
db = mysql.connector.connect(user='root', password='password', host='127.0.0.1')
with db.cursor() as cur:
    cur.execute('USE Company;')
    cur.execute("INSERT INTO Employees(first_name, last_name) VALUES('Ahmed', 'Khaled'), ('Salim', 'Hassan');")
db.commit()
db.close()