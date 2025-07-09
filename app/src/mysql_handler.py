import mysql.connector

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


    def execute_select(self, db, parameters) -> list[dict]:
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

        return db.execute_query(
            f"""
            SELECT
                {', '.join(parameters['select'])}
            FROM
                {parameters['from']}
            WHERE
                {' AND '.join([f"{k} = '{v}'" for k, v in parameters['where'].items()])}
            """
        )

    def execute_insert(self, db, parameters) -> str:
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

        return db.execute_query(
            f"""
            INSERT INTO
                {parameters['to']}({', '.join(parameters['fields'])})
            VALUES
                ("{'", "'.join(parameters['values'])}")
            """
        )

    def execute_select_all(self, db, parameters) -> list[dict]:
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

        return db.execute_query(
            f"""
            SELECT
                {', '.join(parameters['select'])}
            FROM
                {parameters['from']}
            """
        )
    