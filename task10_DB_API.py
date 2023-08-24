import sqlite3
import pyodbc


class DBConnection:
    def __init__(self):
        with pyodbc.connect('DRIVER={SQLite3 ODBC Driver};'
                            'DATABASE=publications.db',
                            autocommit=True) as self.connection:
            self.cursor = self.connection.cursor()
            self.create_tables()

    def create_tables(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS news (text text, city text, publication_date date)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS advertising (text text, expiration_date date, left_days "
                            "numeric)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS motivations (text text, audience text, publication_date date)")
        # self.cursor.close()

    def select(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        result = self.cursor.fetchall()
        return result

    def insert(self, table_name, value1, value2, value3):
        if not self.check_duplicates(table_name, 'text', value1):
            self.cursor.execute(f"INSERT INTO {table_name} VALUES ('{value1}', '{value2}', '{value3}')")
        else:
            print("Such publication already exists!")

    def check_duplicates(self, table_name, field_name, field_value):
        self.cursor.execute(f"SELECT COUNT({field_name}) as count FROM {table_name} WHERE {field_name} = '{field_value}' GROUP BY {field_name}")
        result = self.cursor.fetchall()
        return len(result) > 0

    def select_text(self, field_name, table_name):
        self.cursor.execute(f"SELECT {field_name} FROM {table_name}")
        result = self.cursor.fetchall()
        return result

    def delete_tables(self, table_name):
        self.cursor.execute(f"DROP TABLE {table_name}")

    def check_table_existing(self, table_name):
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        result = self.cursor.fetchall()
        return result
