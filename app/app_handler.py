from src import people_handler

#print(people_handler.PeopleHandler.get_person(
# name="Lucas", 
# last_name="Silva"))
#print(people_handler.PeopleHandler.put_person(
# name="João", 
# last_name="Gomes", 
# dt_birth="2010-11-01"))
#print(people_handler.PeopleHandler.get_person(
# name="Lucas", 
# last_name="Silva"))
print(people_handler.PeopleHandler.get_person(
    name="João", 
    last_name="Gomes"))
print(people_handler.PeopleHandler.get_people())
