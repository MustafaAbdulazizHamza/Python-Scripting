import mysql.connector as mysql
db = mysql.connect(user='root', password='password', host='127.0.0.1')
cur = db.cursor()
cur.execute("CREATE DATABASE Company;")
cur.execute('USE Company;')
cur.execute("""CREATE TABLE Employees(emp_ID INT PRIMARY KEY AUTO_INCREMENT,
            first_name VARCHAR(15) NOT NULL, last_name VARCHAR(15) NOT NULL);""")
cur.close()
db.close()