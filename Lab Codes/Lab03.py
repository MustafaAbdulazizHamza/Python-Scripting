import mysql.connector as mysql
from cryptography.fernet import Fernet, MultiFernet
from hashlib import sha256
import os
import sys
import argparse
from colorama import Fore, init
db = mysql.connect(host='localhost', username='root' ,password = "0770mustafa8763531")
init(autoreset=True)
arp = argparse.ArgumentParser(description="A simple shell interface for interaction with Company database")
arp.add_argument("-u", '--Username', required=True, help="The username")
arp.add_argument("-p", "--Password", required=True, help="The password")
arp.add_argument("-k", '--Keys', required=True, help="The location where the two keys files exists")
args = arp.parse_args()
def load_keys():
        if not os.path.isdir(args.Keys) or not os.path.isfile(f"{args.Keys}\\key1.txt") or not os.path.isfile(f"{args.Keys}\\key2.txt"):
              print(Fore.RED+"The keys` files was not found!")
              sys.exit(404)
        k1 = open(f"{args.Keys}\key1.txt", 'rb')
        k2 = open(f"{args.Keys}\key2.txt", 'rb')
        key1 = k1.read()
        key2 = k2.read()
        return key1,key2

def get_hpassword(id):
        cur1 = db.cursor()
        cur1.execute("USE Company;")
        cur1.execute(f"SELECT * FROM Users WHERE user_id = {id};")
        pd = cur1.fetchall()[0][2]
        return pd

def login(username, password):
    password = sha256(password.encode()).hexdigest()
    key1, key2 = load_keys()
    mf = MultiFernet([Fernet(key1), Fernet(key2)])
    with db.cursor() as cur:
          cur.execute("USE Company;")
          cur.execute(f"SELECT Username, user_id FROM Users;")
          data = cur.fetchall()
          usernames = [{mf.decrypt(tupl[0].encode()).decode():tupl[1]} for tupl in data]
          id = ''
          for t in usernames:
                if username in t.keys():
                      id = t[username]
                      break
          if not id:
                print(Fore.RED+"The username was not found!")
                sys.exit(404)
          if get_hpassword(id) == password:
                return True
def execute(cmd):
      cur2 = db.cursor()
      cur2.execute("USE Company;")
      cur2.execute(cmd)
      data = cur2.fetchall()

      if data == []: return ''
      return data
if login(args.Username, args.Password):
      while True:      
            try:
                  cmd = input(Fore.GREEN+f"{args.Username}"+Fore.RESET+">>> ")
                  if cmd.split()[0].lower() == "exit":
                        sys.exit(0)
                  output = execute(cmd)
                  print(output)
            except Exception as e: print(Fore.RED+f"{e}")
      