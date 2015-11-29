"""

A program designed to randomize a pollyanna gift exchange where parents
cannot get gifts for their children and children cannot get gifts
for their parents. Neither can spouses.

with Nanna.

"""

import random

class Person:
    
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
            
            
joe = Person('Joe', ['Joe', 'Jeff', 'Dave', 'Adam'])
dave = Person('Dave', ['Dave', 'Jeff', 'Adam', 'Joe'])
adam = Person('Adam', ['Adam', 'Jeff', 'Dave', 'Joe'])
justin = Person('Justin', ['Justin', 'Angela', 'Stefan'])
stefan = Person('Stefan', ['Stefan', 'Angela', 'Amanda', 'Justin'])
amanda = Person('Amanda', ['Amanda', 'Stefan'])
francesca = Person('Francesca', ['Francesca', 'Renee', 'George'])
jeff = Person('Jeff', ['Jeff', 'Dave', 'Joe', 'Adam', 'Renee', 'Angela'])
angela = Person('Angela', ['Angela', 'Stefan', 'Justin', 'Renee', 'Jeff'])
renee = Person('Renee', ['Renee', 'George', 'Francesca', 'Angela', 'Jeff'])
george = Person('George', ['George', 'Renee', 'Francesca'])
nanna = Person('Nanna', ['Jeff', 'Renee', 'Angela'])

participants = [joe, dave, adam, justin, stefan, amanda, francesca, jeff,
angela, renee, george, nanna]

part_strings = []
for participant in participants:
    part_strings.append(participant.name)

while part_strings:
    try:
        for participant in participants:
            participant.select()
        # Optional Code to print out to Console rather than .txt
        # for participant in participants:
            # print(participant.name, 'gives to', participant.giving_to)
        print('Success. You are awesome.')
    except IndexError:
        print('You may be awesome but it did not work. Running the program again.')
        quit()
        
with open('full_results.txt', 'w') as f:
    for participant in participants:
        f.write(participant.name + ' --> ' + participant.giving_to + '\n')
        
for participant in participants:
    filename = '%s.txt' % participant.name
    with open(filename, 'w') as file:
        file.write(participant.giving_to)
                     
