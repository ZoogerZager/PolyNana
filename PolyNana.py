"""

A program designed to randomize a pollyanna gift exchange where parents
cannot get gifts for their children and children cannot get gifts
for their parents. Neither can spouses.
Of course, Nana gives gifts to everyone.

"""
import random

class Person (object):
    
    def __init__(self, name, restricted_list=None, giving_to=None):
        self.name = name
        self.restricted_list = restricted_list
        
    def select(self):
        okay_list = []
        for person in part_strings:
            okay_list.append(person)
        restricted_list = self.restricted_list
        for name in restricted_list:
            if name in okay_list:
                okay_list.remove(name)
            else:
                pass
        self.giving_to = random.choice(okay_list)
        part_strings.remove(self.giving_to)
            
            
joe = Person('Joe', ['Joe', 'Jeff'])
dave = Person('Dave', ['Dave', 'Jeff'])
adam = Person('Adam', ['Adam', 'Jeff'])
justin = Person('Justin', ['Justin', 'Angela'])
stefan = Person('Stefan', ['Stefan', 'Angela', 'Amanda'])
amanda = Person('Amanda', ['Amanda', 'Stefan'])
francesca = Person('Francesca', ['Francesca', 'Renee', 'George'])
jeff = Person('Jeff', ['Jeff', 'Dave', 'Joe', 'Adam'])
angela = Person('Angela', ['Angela', 'Stefan', 'Justin'])
renee = Person('Renee', ['Renee', 'George', 'Francesca'])
george = Person('George', ['George', 'Renee', 'Francesca'])

participants = [joe, dave, adam, justin, stefan, amanda, francesca, jeff,
angela, renee, george]

part_strings = []
for participant in participants:
    part_strings.append(participant.name)

random.shuffle(participants)

while part_strings != []:
    try:
        for participant in participants:
            participant.select()
        # Optional Code to print out to Console rather than .txt
        #for participant in participants:
            #print(participant.name, 'gives to', participant.giving_to)
        print('Success!')    
    except IndexError:
        print('Oh no, Elves sabotaged the proceedings! Run the program again.')
        quit()
        
for participant in participants:
    filename = '%s.txt' % participant.name
    with open(filename, 'w') as file:
        file.write(participant.giving_to)
