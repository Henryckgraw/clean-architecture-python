from abc import ABC, abstractmethod
from typing import Optional
from src.mysql_handler import (
    SelectFullData
)
from src.person_handler import (
    Person
)


class GetPeopleInterface(ABC):
    """
    An interface for getting a person's information.
    """
    @abstractmethod
    def get(self) -> Optional['list[Person]']:
        """Retorna um lista de Person ou lista vazia."""
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """Retorna os dados das pessoas como dicionário."""
        pass

    @abstractmethod
    def __iter__(self) -> str:
        """Interação da resposta."""
        pass


class GetPeopleImplementation(GetPeopleInterface):
    """ 
    A class to handle operations related to retrieving a people's information.
    """

    def __init__(self):
        """
        Initializes the PeopleHandler class.
        """
        self.databaseoperation = SelectFullData()
        self._people = None

    def __iter__(self):
        return iter(self._people)

    def to_dict(self):
        if self._people:
            return {i: p.to_dict() for i, p in enumerate(self._people)}
        return "People not found"

    def get(self) -> list[Person]:
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

        people = self.databaseoperation.execute(parameters=parameters)

        list_person = []
        for person in people:
            list_person.append(
                Person(
                    name=person[0],
                    last_name=person[1],
                    dt_birth=person[2].strftime("%m/%d/%Y")
                )
            )
        self._people = list_person

        if not self._people:
            return []
        return self._people


class GetPeople:
    """
    An class use the GetPersonInterface to retrieve a person's information.
    """
    def __init__(self, handler: GetPeopleInterface):
        self.handler = handler
        self.response = self.get()

    def get(self):
        return self.handler.get()

    def to_dict(self):
        return self.handler.to_dict()

    def __iter__(self):
        return (self.handler.__iter__())
