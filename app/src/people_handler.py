from src.mysql_handler import SelectData, InsertData, SelectFullData

class Person:
    """
    A class Person to represent a person with name, last name, and date of birth.
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
    
class PersonParent(Person):
    """
    A class Person to represent a person with name, last name, and date of birth.
    """
    def __init__(
        self,
        name: str,
        last_name: str,
        dt_birth: str
    ):
        super().__init__(name, last_name, dt_birth)
        self.type = "parent"
        self.sons = [f"{self.name} 1st Son", f"{self.name} 2nd Son"]

    def to_dict(self):
        return {
            "name": self.name, 
            "last_name": self.last_name, 
            "date_birth": self.dt_birth,
            "type": self.type,
            "sons": self.sons
        }

    def __str__(self):
        return f"""name: {self.name},
                   last_name: {self.last_name},
                   date_birth: {self.dt_birth},
                   type: {self.type},
                   sons: {self.sons}
                """

class PersonChildless(Person):
    """
    A class people to represent a person with name, last name, and date of birth.
    """
    def __init__(
        self,
        name: str,
        last_name: str,
        dt_birth: str
    ):
        super().__init__(name, last_name, dt_birth)
        self.type = "childless"

    def to_dict(self):
        return {
            "name": self.name, 
            "last_name": self.last_name, 
            "date_birth": self.dt_birth,
            "type": self.type
        }

    def __str__(self):
        return f"""name: {self.name},
last_name: {self.last_name},
date_birth: {self.dt_birth},
type: {self.type}
"""

class GetPerson:
    """ 
    A class to handle operation related to retrieving a person's information.
    """

    def __init__(self, name: str, last_name: str):
        """
        Initializes the PeopleHandler class.
        """
        self.name, self.last_name = name, last_name
        self.databaseoperation = SelectData()
        self.response = self.get_person()

    def __str__(self):
        if self.response:
            return str(self.response)
        return "Person not found"

    def to_dict(self):
        if self.response:
            return self.response.to_dict()
        return "Person not found"

    def get_person(self) -> Person:
        """
        Returns a dictionary with the person's name and last name.
        """
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

        person = self.databaseoperation.execute(parameters=parameters)

        if not person:
            return None
        else:
            return Person(
                name=person[0][0],
                last_name=person[0][1],
                dt_birth=person[0][2].strftime("%m/%d/%Y")
            )


class PutPerson:
    """ 
    A class to handle operation related to input a person's information.
    """

    def __init__(self, p: Person):
        """
        Initializes the PeopleHandler class.
        """
        self.person = p
        self.databaseoperation = InsertData()
        self.response = self.put_person()

    def __str__(self):
        return self.response


    def put_person(self) -> str:
        """
        Adds a person to the database.
        """
        parameters = {
            "fields": [
               "nome",
               "sobrenome",
               "dt_nasc"
            ],
            "to": "usuario",
            "values": [
                self.person.name,
                self.person.last_name,
                self.person.dt_birth
            ]
        }

        person = self.databaseoperation.execute(parameters=parameters)

        if "Error" not in person:
            return f"Success put person: {self.person.name} {self.person.last_name}"
        else:
            return f"Error put person: {person}"


class GetPeople:
    """ 
    A class to handle operations related to retrieving a people's information.
    """

    def __init__(self):
        """
        Initializes the PeopleHandler class.
        """
        self.databaseoperation = SelectFullData()
        self._people = self.get_people()

    def __iter__(self):
        return iter(self._people)

    def to_dict(self):
        if self._people:
            return {i: p.to_dict() for i, p in enumerate(self._people)}
        return "People not found"

    def get_people(self) -> list[Person]:
        """
        Returns a list of dictionaries with the people's names and last names.
        """
        parameters = {
            "select": [
               "nome",
               "sobrenome",
               "dt_nasc"
            ],
            "from": "usuario"
        }

        person = self.databaseoperation.execute(parameters=parameters)
        
        list_person = []
        for person in person:
            list_person.append(
                Person(
                    name=person[0],
                    last_name=person[1],
                    dt_birth=person[2].strftime("%m/%d/%Y")
                )
            )

        return list_person