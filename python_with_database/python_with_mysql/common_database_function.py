import mysql.connector
from mysql.connector import Error

def connect_db(database_name,password='Koratj@y54321'):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=password,
            database=database_name
        )
        if connection.is_connected():
            print("Connected to the database")
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_table(db_cursor, tabel_name):
    try:
        query = f'CREATE TABLE IF NOT EXISTS {tabel_name} (Roll INT, Name VARCHAR(20))'
        db_cursor.execute(query)
        print(f"Table '{tabel_name}' created or already exists!")
    except Error as e:
        print(f"Error creating table: {e}")

def insert_single(db_cursor, tabel_name, mydb, roll, name):
    try:
        query = f"INSERT INTO {tabel_name} (Roll, Name) VALUES (%s, %s)"
        db_cursor.execute(query, (roll, name))
        mydb.commit()
        print(f"Inserted {db_cursor.rowcount} row.")
    except Error as e:
        print(f"Error inserting data: {e}")

def select_all(db_cursor, tabel_name):
    try:
        query = f"SELECT * FROM {tabel_name}"
        db_cursor.execute(query)
        return db_cursor.fetchall()
    except Error as e:
        print(f"Error selecting data: {e}")

def update_data(db_cursor, tabel_name, mydb, roll, name):
    try:
        query = f"UPDATE {tabel_name} SET Name=%s WHERE ROll=%s"
        db_cursor.execute(query, (roll, name))
        mydb.commit()
        print(f"Updated {db_cursor.rowcount} row.")
    except Error as e:
        print(f"Error updating data: {e}")

def delete_data(db_cursor, tabel_name, mydb, roll):
    try:
        query = f"DELETE FROM {tabel_name} WHERE Roll=%s"
        db_cursor.execute(query, (roll,))
        mydb.commit()
        print(f"Deleted {db_cursor.rowcount} row.")
    except Error as e:
        print(f"Error deleting data: {e}")