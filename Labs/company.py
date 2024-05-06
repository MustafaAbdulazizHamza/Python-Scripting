lab 2




import mysql.connector as mysql  
import hashlib  
from cryptography.fernet import Fernet  
import sys  
import os  
 
def create_db(): 
    conn = mysql.connect( 
        user='root',  
        password='password',  
        host='127.0.0.1',  
    ) 
    cursor = conn.cursor() 
 
    cursor.execute("CREATE DATABASE IF NOT EXISTS Company;") 
    cursor.execute("USE Company;")  # Use the 'Company' database 
 
    cursor.execute( 
        """ 
        CREATE TABLE IF NOT EXISTS Users ( 
            user_id INT AUTO_INCREMENT PRIMARY KEY, 
            username BLOB,  # Blob to hold encrypted data 
            password TEXT  # Plain text or hashed 
        ) 
        """ 
    ) 
 
    conn.commit()  
    return conn, cursor 
 
def hash_password(password): 
    return hashlib.sha256(password.encode("utf-8")).hexdigest() 
 

def encrypt_username(username): 
    key = Fernet.generate_key()  # Generate a key 
    cipher = Fernet(key) 
    encrypted_username = cipher.encrypt(username.encode("utf-8")) 
 
    
    with open("encryption_key.key", "wb") as key_file: 
        key_file.write(key) 
 
    return encrypted_username, key 
 
def insert_user(cursor, username, password): 
    encrypted_username, encryption_key = encrypt_username(username) 
    hashed_password = hash_password(password) 
 
    cursor.execute( 
        """ 
        INSERT INTO Users (username, password) 
        VALUES (%s, %s) 
        """, 
        (encrypted_username, hashed_password), 
    ) 
 
    return encrypted_username, hashed_password, encryption_key 
 

if name == "__main__": 
    if len(sys.argv) < 3:  
        print("Usage: python script.py <username> <password>") 
        sys.exit(1) 
 
    username = sys.argv[1]   
    password = sys.argv[2]  
 
    conn, cursor = create_db() 
 
    encrypted_username, hashed_password, encryption_key = insert_user(cursor, username, password) 
 
    # Commit and close connection 
    conn.commit() 
    conn.close() 
 
    print("User inserted successfully!") 
    print("Encrypted Username:", encrypted_username)  
    print("Hashed Password:", hashed_password)



lab3
import mysql.connector as mysql   
import hashlib   
from cryptography.fernet import Fernet   
import sys   
import os   
 
 
def load_encryption_key(): 
    with open("encryption_key.key", "rb") as key_file: 
        return key_file.read() 
 
 
def hash_password(password): 
    return hashlib.sha256(password.encode("utf-8")).hexdigest() 
 
 
def authenticate_user(username, password): 
     
    conn = mysql.connect( 
        user='root',  
        password='password',  
        host='127.0.0.1',  # Localhost 
        database='Company',  
    ) 
    cursor = conn.cursor() 
 
 
    encryption_key = load_encryption_key() 
    cipher = Fernet(encryption_key) 
 
 
    hashed_password = hash_password(password) 
 
 
    cursor.execute("SELECT username, password FROM Users") 
    users = cursor.fetchall() 
 
 
    for encrypted_username, stored_hashed_password in users: 
        decrypted_username = cipher.decrypt(encrypted_username).decode("utf-8") 
 
        if decrypted_username == username and stored_hashed_password == hashed_password: 
            # Close the connection and return true if authenticated 
            conn.close() 
            return True 
 
    conn.close()
    return False 
 
 
def execute_sql_command(cursor, command): 
    forbidden_commands = ["DROP", "DELETE", "TRUNCATE", "ALTER"] 
    
    if any(fc.lower() in command.lower() for fc in forbidden_commands): 
        print("Operation not allowed for safety reasons.") 
        return 
 
    try: 
        cursor.execute(command) 
        cursor.connection.commit()  
        print("SQL command executed successfully.") 
    except Exception as e: 
        print("Error executing SQL command:", e) 
 
 
if name == "__main__": 
    if len(sys.argv) < 3:  
        print("Usage: python script.py <username> <password> [sql_command]") 
        sys.exit(1) 
 
    username = sys.argv[1]  
    password = sys.argv[2]  
 
   if authenticate_user(username, password): 
        print("Login successful!")  
 
       if len(sys.argv) > 3: 
            sql_command = " ".join(sys.argv[3:])  
            conn = mysql.connect( 
                user='root',   
                password='password',  
                host='127.0.0.1', 
                database='Company',  
            ) 
            cursor = conn.cursor() 
            execute_sql_command(cursor, sql_command)  # Execute the command 
 
            conn.close()  
    else: 
        print("Login failed. Incorrect username or password.")