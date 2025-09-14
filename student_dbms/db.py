import mysql.connector
def create_connection():
    conn=mysql.connector.connect(
    host="localhost",
    user="sqlworkout",
    password="1q2w3e4r5t6y7u8i9o0p",
    port="3306",
    database="std_db"
    )
    return conn