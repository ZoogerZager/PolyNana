"""

A program designed to randomize a pollyanna gift exchange where
- Parents cannot give to their children.
- Children cannot give to their parents.
- Siblings cannot give to each other.
- Spouses/Couples cannot give to each other.

"""

import os
import random


class Person:
    
    def __init__(self, name, restricted_list=None, giving_to=None):
        self.name = name
        self.restricted_list = restricted_list
        self.giving_to = giving_to
        
        
def select(person, hat_list):
    '''person should be a Person object. hat_list should be a list of strings of participants.'''
    okay_list = []
    for each in hat:
        okay_list.append(each)
    for name in person.restricted_list:
        if name in okay_list:
            okay_list.remove(name)
        else:
            pass        
    return random.choice(okay_list)
    
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

completed = False
while not completed:
    hat = []
    for participant in participants:
        hat.append(participant.name)
    try: 
        for participant in participants:
            participant.giving_to = select(participant, hat)
            hat.remove(participant.giving_to)
        completed = True        
    except IndexError:
        completed = False

if completed:
    print('Success. You are awesome.')
    with open('full_results.txt', 'w') as f:
        for participant in participants:
            f.write(participant.name + ' --> ' + participant.giving_to + '\n')
    
    if not os.path.exists(os.getcwd() + '\Individual_Results'):
        os.mkdir(os.getcwd() + '\Individual_Results')
    os.chdir(os.getcwd() + '\Individual_Results')
    for participant in participants:
        filename = '%s.txt' % participant.name
        with open(filename, 'w') as file:
            file.write(participant.giving_to)
