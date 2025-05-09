import mysql.connector

class MysqlHandler:
    """
    A class to handle MySQL database connections and operations.
    """
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return connection
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def close_connection(self, connection):
        if connection.is_connected():
            connection.close()

    def execute_query(self, query, params=None):
        connection = self.connect()
        if connection:
            cursor = connection.cursor(buffered=True)
            try:
                cursor.execute(query, params)
                connection.commit()
                return cursor.fetchall()
            except mysql.connector.Error as err:
                print(f"Error: {err}")
            finally:
                cursor.close()
                self.close_connection(connection)
        return None
