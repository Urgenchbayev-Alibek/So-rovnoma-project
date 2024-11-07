# database.py
import pymysql
from pymysql.cursors import DictCursor

class Connection_DB:
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='urg_alibek',
                cursorclass=DictCursor
            )
            self.create_base()
            print("Database connected successfully.")
        except pymysql.MySQLError as e:
            print(f"Database connection error: {e}")

    def create_base(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('DROP DATABASE IF EXISTS collage')
                cursor.execute('CREATE DATABASE IF NOT EXISTS collage')
                cursor.execute('USE collage')

                cursor.execute('DROP TABLE IF EXISTS students')
                cursor.execute("""CREATE TABLE IF NOT EXISTS students (      
                  id INT PRIMARY KEY AUTO_INCREMENT,
                  first_name VARCHAR(32),
                  last_name VARCHAR(32),
                  age INT,
                  gender VARCHAR(16),
                  region VARCHAR(32),
                  phone VARCHAR(15),
                  faculty VARCHAR(16),
                  course VARCHAR(8)
                );""")
            self.conn.commit()
        except pymysql.MySQLError as e:
            print(f"Error creating tables: {e}")

    def get_connection(self):
        return self.conn
