from src.people_handler import People, GetPerson, PutPerson, GetPeople
from pprint import pprint

p = People(
        name="Maria", 
        last_name="Oliveira", 
        dt_birth="1959-05-20"
    )
print(f"{p.name} {p.last_name} - {p.dt_birth}")

print("Put Person:")
pprint(str(PutPerson(p)))

print("\nGet Person:")
p = (
        GetPerson(
            name="João",
            last_name="Gomes"
        )
    )
print(p.to_dict())
print(str(p))

print("\nGet People:")
pe = GetPeople()
pprint(pe.to_dict())
for p in pe:
    print(str(p))

