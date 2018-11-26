# Script to read from database and output recipient of participant into .txt file

from models import db, Participant
from pony.orm import *


db.bind('sqlite', 'participants.db', create_db=False)
db.generate_mapping(create_tables=True)

@db_session
def recipient_to_txt():
    query = Participant.get(name=input('Who do you need the recipient for? ex: Justin: '))
    with open(query.name + '.txt', 'w') as file:
        file.write(query.name + ', you are giving to ' + query.giving_to + "!") 


recipient_to_txt()
