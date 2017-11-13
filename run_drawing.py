from pony.orm import *
import polynanna


db = Database()

class Person(db.Entity):
    name = Required(str)
    giving_to = Required(str)


db.bind('sqlite', 'participants.db', create_db=True)
db.generate_mapping(create_tables=True)

@db_session
def run_drawing():
	polyanna = polynanna.main()
	for p in polyanna.participants:
		try: # update table if name entries already exist
			person = Person.get(name=p.name)
			person.giving_to = p.giving_to
		except: # otherwise create them.
			person = Person(name=p.name, giving_to=p.giving_to)


if __name__ == '__main__':
	run_drawing()
	print('Drawing Complete.')
