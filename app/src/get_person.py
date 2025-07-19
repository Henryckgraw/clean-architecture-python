from abc import ABC, abstractmethod
from typing import Optional
from src.mysql_handler import (
    SelectData
)
from src.people_handler import (
    Person
)


class GetPersonInterface(ABC):
    """
    An interface for getting a person's information.
    """
    @abstractmethod
    def get_person(self) -> Optional['Person']:
        """Retorna um objeto Person ou None."""
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """Retorna os dados da pessoa como dicionário."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Representação em string da resposta."""
        pass


class GetPersonImplementation(GetPersonInterface):
    """ 
    A class to handle operation related to retrieving a person's information.
    """

    def __init__(self, name: str, last_name: str):
        """
        Initializes the PeopleHandler class.
        """
        self.name = name
        self.last_name = last_name
        self.databaseoperation = SelectData()
        self.response = None

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
            self.response = None
            return self.response
        else:
            self.response = Person(
                name=person[0][0],
                last_name=person[0][1],
                dt_birth=person[0][2].strftime("%m/%d/%Y")
            )
            return self.response


class GetPersonImplementationSubst(GetPersonInterface):
    """ 
    A class to handle operation related to retrieving a person's information.
    """

    def __init__(self, name: str, last_name: str):
        """
        Initializes the PeopleHandler class.
        """
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return "String representation of GetPersonImplementationSubst"

    def to_dict(self):
        return "Dictionary representation of GetPersonImplementationSubst"

    def get_person(self) -> Person:
        return None


class GetPerson:
    """
    An class use the GetPersonInterface to retrieve a person's information.
    """
    def __init__(self, handler: GetPersonInterface):
        self.handler = handler
        self.response = self.get_person()

    def get_person(self):
        return self.handler.get_person()

    def to_dict(self):
        return self.handler.to_dict()

    def __str__(self):
        return str(self.handler)