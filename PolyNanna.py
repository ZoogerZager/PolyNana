import os
from random import choice


class Person:

    def __init__(self, name, restricted_list=None, giving_to=None):
        self.name = name
        self.restricted_list = restricted_list
        self.giving_to = giving_to


def select(person, hat):
    '''person should be a Person object. hat_list should be a list of strings of participants.'''
    okay_list = list(set([person for person in hat]) - person.restricted_list)
    return choice(okay_list)

def run_drawing():
    completed = False
    while not completed:
        hat = build_hat()
        try:
            for participant in participants:
                participant.giving_to = select(participant, hat)
                hat.remove(participant.giving_to)
            completed = True
        except IndexError:
            completed = False
    return completed

def build_participants():
    participants = []
    with open('data.txt', 'r') as data:
        for line in data:
            restricted_list = line.rsplit()
            participants.append(Person(restricted_list[0], set(restricted_list)))
    return participants

def build_hat():
    return set([participant.name for participant in participants])

def write_full_results():
    with open('full_results.txt', 'w') as f:
        for participant in participants:
            f.write(participant.name + ' --> ' + participant.giving_to + '\n')

def write_individual_results():
    if not os.path.exists(os.getcwd() + '\Individual_Results'):
        os.mkdir(os.getcwd() + '\Individual_Results')
    os.chdir(os.getcwd() + '\Individual_Results')
    for participant in participants:
        filename = '%s.txt' % participant.name
        with open(filename, 'w') as file:
            file.write(participant.giving_to)

participants = build_participants()
if run_drawing():
    print('Success. You are awesome.')
    write_full_results()
    write_individual_results()
