import argparse as ar
import hashlib as hb
from cryptography.fernet import Fernet, MultiFernet
import os
import mysql.connector as mysql
arg = ar.ArgumentParser(description="This code is used either to create the database or to add a new user.")
arg.add_argument("-u", '--Username', required=True, help="The username to add.")
arg.add_argument('-p', '--Password', required=True, help="The password to add.")
arg.add_argument("-a", '--Add', action="store_true",help="To enable addition mode.")
args = arg.parse_args()

db = mysql.connect(host='localhost', username='root', password='0770mustafa8763531')
if not args.Add:
    with db.cursor() as cur:
        cur.execute("CREATE DATABASE Company;")
        cur.execute("USE Company;")
        cur.execute("CREATE TABLE Users(user_id int primary key auto_increment,Username varchar(255) unique not null, Password varchar(256) unique not null);")
    key1 = Fernet.generate_key()
    key2 = Fernet.generate_key()
    with open(f"{os.getcwd()}\key1.txt", 'wb') as k1: k1.write(key1)
    with open(f"{os.getcwd()}\key2.txt", 'wb') as k2: k2.write(key2)
password = hb.sha256(args.Password.encode()).hexdigest()
k1 = open(f"{os.getcwd()}\key1.txt", 'rb')
k2 = open(f"{os.getcwd()}\key2.txt", 'rb')
key1 = k1.read()
key2 = k2.read()
f1 = Fernet(key1)
f2 = Fernet(key2)
k1.close()
k2.close()
mtf = MultiFernet([f1,f2])
username = mtf.encrypt(args.Username.encode()).decode()
with db.cursor() as cur:
    cur.execute("USE Company;")
    cur.execute("INSERT INTO Users(Username, Password) VALUES('{}','{}');".format(username, password))
    db.commit()