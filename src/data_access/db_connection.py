import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connected to the database.")
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            raise

    def execute_script(self, script_path):
        """Execute an SQL script from a file."""
        try:
            if not self.connection:
                raise Exception("Database connection is not established.")
            cursor = self.connection.cursor()
            with open(script_path, 'r') as file:
                script = file.read()
                for statement in script.split(';'):
                    if statement.strip():
                        cursor.execute(statement)
            self.connection.commit()
            print(f"Executed script: {script_path}")
        except Error as e:
            print(f"Error executing script: {e}")
            raise
        except FileNotFoundError:
            print(f"File not found: {script_path}")
            raise
        finally:
            cursor.close()

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")
