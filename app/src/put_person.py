from abc import ABC, abstractmethod
from typing import Optional
from src.mysql_handler import (
    InsertData
)
from src.person_handler import (
    Person
)


class PutPersonInterface(ABC):
    """
    An interface for putting a person's information.
    """
    @abstractmethod
    def put(self) -> Optional['Person']:
        """Retorna um objeto Person ou None."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Representação em string da resposta."""
        pass


class PutPersonImplementation(PutPersonInterface):
    """ 
    A class to handle operation related to input a person's information.
    """

    def __init__(self, person: Person):
        """
        Initializes the PeopleHandler class.
        """
        self.person = person
        self.databaseoperation = InsertData()
        self.response = None

    def __str__(self):
        return self.response

    def put(self) -> str:
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
            self.response = f"Success put person: {self.person.name} {self.person.last_name}"
            return self.response
        else:
            self.response = f"Error put person: {person}"
            return self.response


class PutPerson:
    """
    An class use the putPersonInterface to retrieve a person's information.
    """
    def __init__(self, handler: PutPersonInterface):
        self.handler = handler
        self.response = self.put()

    def put(self):
        return self.handler.put()

    def __str__(self):
        return str(self.handler)
