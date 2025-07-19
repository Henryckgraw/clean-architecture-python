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


class PersonMarriedChildless(PersonChildless):
    """
    A class people to represent a person with name, last name, and date of birth.
    """
    def __init__(
        self,
        name: str,
        last_name: str,
        dt_birth: str,
        person: Person
    ):
        super().__init__(name, last_name, dt_birth)
        self.spouse = f"{person.name} {person.last_name}"

    def to_dict(self):
        return {
            "name": self.name, 
            "last_name": self.last_name, 
            "date_birth": self.dt_birth,
            "type": self.type,
            "spouse": self.spouse
        }

    def __str__(self):
        return f"""name: {self.name},
last_name: {self.last_name},
date_birth: {self.dt_birth},
type: {self.type},
spouse: {self.spouse}
"""


class PersonMarriedParent(PersonParent):
    """
    A class people to represent a person with name, last name, and date of birth.
    """
    def __init__(
        self,
        name: str,
        last_name: str,
        dt_birth: str,
        person: Person
    ):
        super().__init__(name, last_name, dt_birth)
        self.spouse = f"{person.name} {person.last_name}"

    def to_dict(self):
        return {
            "name": self.name, 
            "last_name": self.last_name, 
            "date_birth": self.dt_birth,
            "type": self.type,
            "sons": self.sons,
            "spouse": self.spouse
        }

    def __str__(self):
        return f"""name: {self.name},
last_name: {self.last_name},
date_birth: {self.dt_birth},
type: {self.type},
sons: {self.sons},
spouse: {self.spouse}
"""
