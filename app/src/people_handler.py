from src.mysql_handler import DbHandler

class People:
    """
    A class people to represent a person with name, last name, and date of birth.
    """
    def __init__(
        self,
        name: str,
        last_name: str,
        dt_birth: str
    ):
        self.name: str = name
        self.last_name: str = last_name
        self.dt_birth: str = dt_birth

    def to_dict(self):
        return {
            "name": self.name, 
            "last_name": self.last_name, 
            "date_birth": self.dt_birth
        }

    def __str__(self):
        return f"name: {self.name}, last_name: {self.last_name}, date_birth: {self.dt_birth}"
    
class GetPerson():
    """ 
    A class to handle operation related to retrieving a person's information.
    """

    def __init__(self, name: str, last_name: str):
        """
        Initializes the PeopleHandler class.
        """
        self.dbConnection = DbHandler()
        self.name, self.last_name = name, last_name
        self.response = self.get_person()

    def __str__(self):
        if self.response:
            return str(self.response)
        return "Person not found"

    def to_dict(self):
        if self.response:
            return self.response.to_dict()
        return "Person not found"

    def get_person(self) -> People:
        """
        Returns a dictionary with the person's name and last name.
        """
        db = self.dbConnection
        parameters = {
            "select": [
               "nome",
               "sobrenome",
               "dt_nasc"
            ],
            "from": "usuario",
            "where": {
               "nome": f"{self.name}",
               "sobrenome": f"{self.last_name}"
            }
        }

        people = db.execute_select(db, parameters)

        if not people:
            return None
        else:
            return People(
                name=people[0][0],
                last_name=people[0][1],
                dt_birth=people[0][2].strftime("%m/%d/%Y")
            )


class PutPerson():
    """ 
    A class to handle operation related to input a person's information.
    """

    def __init__(self, p: People):
        """
        Initializes the PeopleHandler class.
        """
        self.dbConnection = DbHandler()
        self.people = p
        self.response = self.put_person()

    def __str__(self):
        return self.response


    def put_person(self) -> str:
        """
        Adds a person to the database.
        """
        db = self.dbConnection
        parameters = {
            "fields": [
               "nome",
               "sobrenome",
               "dt_nasc"
            ],
            "to": "usuario",
            "values": [
                self.people.name,
                self.people.last_name,
                self.people.dt_birth
            ]
        }

        people = db.execute_insert(db, parameters)

        if "Error" not in people:
            return f"Success put person: {self.people.name} {self.people.last_name}"
        else:
            return f"Error put person: {people}"


class GetPeople():
    """ 
    A class to handle operations related to retrieving a people's information.
    """

    def __init__(self):
        """
        Initializes the PeopleHandler class.
        """
        self.dbConnection = DbHandler()
        self._people = self.get_people()

    def __iter__(self):
        return iter(self._people)

    def to_dict(self):
        if self._people:
            return {i: p.to_dict() for i, p in enumerate(self._people)}
        return "People not found"

    def get_people(self) -> list[People]:
        """
        Returns a list of dictionaries with the people's names and last names.
        """
        db = self.dbConnection
        parameters = {
            "select": [
               "nome",
               "sobrenome",
               "dt_nasc"
            ],
            "from": "usuario"
        }

        people = db.execute_select_all(db, parameters)
        
        list_person = []
        for person in people:
            list_person.append(
                People(
                    name=person[0],
                    last_name=person[1],
                    dt_birth=person[2].strftime("%m/%d/%Y")
                )
            )

        return list_person