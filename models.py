from pony.orm import *

db = Database()


class Participant(db.Entity):
    name = Required(str)
    giving_to = Required(str)
