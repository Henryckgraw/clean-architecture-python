import src.mysql_handler as mysql_handler

class PeopleHandler:
    """
    A class to handle operations related to people in the database.
    """
    def get_person(name, last_name):
        """
        Returns a dictionary with the person's name and last name.
        """
        db = mysql_handler.MysqlHandler(
            host="127.0.0.1",
            user="Aplication",
            password="1234",
            database="cadastro"
        )

        people = db.execute_query(
            "SELECT nome, sobrenome, dt_nasc FROM usuario WHERE nome = %s AND sobrenome = %s",
            (name, last_name)
        )
        print(people)
        if not people:
            return None
        else:
            return {
                "name":      people[0][0],
                "last_name": people[0][1],
                "dt_birth_mdy":  people[0][2].strftime("%m/%d/%Y"),
            }

    def put_person(name, last_name, dt_birth):
        """
        Adds a person to the database.
        """
        db = mysql_handler.MysqlHandler(
            host="127.0.0.1",
            user="Aplication",
            password="1234",
            database="cadastro"
        )

        people = db.execute_query(
            "INSERT INTO usuario VALUES (%s, %s, %s)",
            (name, last_name, dt_birth)
        )

        if not people:
            return "Sucess"
        else:
            return f"Error put person: {people}"

    def get_people():
        """
        Returns a list of dictionaries with the people's names and last names.
        """
        db = mysql_handler.MysqlHandler(
            host="127.0.0.1",
            user="Aplication",
            password="1234",
            database="cadastro"
        )

        people = db.execute_query(
            "SELECT nome, sobrenome, dt_nasc FROM usuario"
        )
        
        list_person = []
        for indx, person in enumerate(people):
            list_person.append({
                "line":      indx,
                "name":      person[0],
                "last_name": person[1],
                "dt_birth_mdy":  person[2].strftime("%m/%d/%Y"),
            })

        if not list_person:
            return None
        else:
            return list_person