from src.person_handler import (
    Person,
    PersonParent,
    PersonChildless,
    PersonMarriedParent,
    PersonMarriedChildless
)
from src.get_person import (
    GetPerson,
    GetPersonImplementation,
    GetPersonImplementationSubst
)
from src.get_people import (
    GetPeople,
    GetPeopleImplementation
)
from src.put_person import (
    PutPerson,
    PutPersonImplementation
)
from pprint import pprint

print("\n------- Manipulating Class Person -------\n\n")
print("Person with childs:")
p = PersonParent(
        name="Henrique",
        last_name="Oliveira",
        dt_birth="1992-12-10"
    )
print(p.to_dict())

print("\nPerson with childs:")
p = PersonChildless(
        name="Henrique",
        last_name="Oliveira",
        dt_birth="1992-12-10"
    )
print(p.to_dict())

print("\nPerson with child Married:")
p = PersonMarriedParent(
        name="Marcello",
        last_name="Oliveira",
        dt_birth="1988-09-13",
        person=Person(
            name="Denise",
            last_name="Oliveira",
            dt_birth="1993-10-04"
        )
    )
print(str(p))

print("\nPerson without child Married:")
p = PersonMarriedChildless(
        name="Marcello",
        last_name="Oliveira",
        dt_birth="1988-09-13",
        person=Person(
            name="Denise",
            last_name="Oliveira",
            dt_birth="1993-10-04"
        )
    )
print(str(p))



print("\n\n------- Manipulating Database -------\n\n")
p = Person(
        name="Hanna",
        last_name="Montanna",
        dt_birth="1989-11-02"
    )
print(f"{p.name} {p.last_name} - {p.dt_birth}")

print("Put Person:")
putperson = PutPersonImplementation(p)
pprint(str(PutPerson(putperson)))

print("\nGet Person:")
getperson = GetPersonImplementation(
    name="João",
    last_name="Gomes"
)
p = GetPerson(getperson)

print(type(p))
print(p.response.name)
print(p.to_dict())
print(str(p))

print("\nGet Person with GetPersonImplementationSubst:")
getperson = GetPersonImplementationSubst(
    name="João",
    last_name="Gomes"
)
p = GetPerson(getperson)

print(type(p))
print(p.response)
print(p.to_dict())
print(str(p))

print("\nGet People:")
getpeople = GetPeopleImplementation()
pe = GetPeople(getpeople)
pprint(pe.to_dict())
for p in pe:
    print(str(p))
