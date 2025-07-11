import mysql.connector
import abc

class DbHandler:
    """
    A class to handle MySQL database connections and operations.
    """
    host: str
    user: str
    password: str
    database: str

    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "Aplication"
        self.password = "1234"
        self.database = "cadastro"

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
                return f"Error: {err}"
            finally:
                cursor.close()
                self.close_connection(connection)


class DatabaseOperation:
    """
    A base class for database operations.
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self, parameters):
        return


class SelectData(DatabaseOperation):
    """
    Executes a SELECT query and returns the results.

    {
        "select": [
            "nome",
            "sobrenome",
            "dt_nasc"
        ],
        "from": "usuario",
        "where": {
            "nome": f"{name}",
            "sobrenome": f"{last_name}"
        }
    }
    """
    def __init__(self):
        self.db_handler = DbHandler()

    def execute(self, parameters) -> list[dict]:

        return self.db_handler.execute_query(
            f"""
            SELECT
                {', '.join(parameters['select'])}
            FROM
                {parameters['from']}
            WHERE
                {' AND '.join([f"{k} = '{v}'" for k, v in parameters['where'].items()])}
            """
        )


class InsertData(DatabaseOperation):
    """
    Executes a SELECT query and returns the results.

    {
        "fields": [
            "nome",
            "sobrenome",
            "dt_nasc"
        ],
        "to": "usuario",
        "values": [
            name,
            last_name,
            dt_birth
        ]
    }
    """
    def __init__(self):
        self.db_handler = DbHandler()

    def execute(self, parameters) -> str:

        return self.db_handler.execute_query(
            f"""
            INSERT INTO
                {parameters['to']}({', '.join(parameters['fields'])})
            VALUES
                ("{'", "'.join(parameters['values'])}")
            """
        )


class SelectFullData(DatabaseOperation):
    """
    Executes a SELECT query and returns the results.

    {
        "select": [
            "nome",
            "sobrenome",
            "dt_nasc"
        ],
        "from": "usuario"
    }
    """
    def __init__(self):
        self.db_handler = DbHandler()

    def execute(self, parameters) -> list[dict]:

        return self.db_handler.execute_query(
            f"""
            SELECT
                {', '.join(parameters['select'])}
            FROM
                {parameters['from']}
            """
        )
    