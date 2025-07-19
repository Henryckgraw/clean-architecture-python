from src.people_handler import (
    Person,
    GetPeople,
    PutPerson,
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
from pprint import pprint

# p = Person(
#         name="Rosana",
#         last_name="Maria",
#         dt_birth="1958-06-12"
#     )
# print(f"{p.name} {p.last_name} - {p.dt_birth}")

# print("Put Person:")
# pprint(str(PutPerson(p)))

print("\nPerson with childs:")
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
pe = GetPeople()
pprint(pe.to_dict())
for p in pe:
    print(str(p))
