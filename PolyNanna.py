import os
from random import choice


class Participant:

    def __init__(self, name, restricted_set=None, giving_to=None):
        self.name = name
        self.restricted_set = restricted_set
        self.giving_to = giving_to


def build_participants():
    participants = []
    with open('data.txt', 'r') as data:
        for line in data:
            restricted_set = line.rsplit()
            participants.append(Participant(restricted_set[0], set(restricted_set)))
    return participants


def build_hat():
    return set([participant.name for participant in participants])


def select(person, hat):
    okay_set = set([person for person in hat]) - person.restricted_set
    return choice(list(okay_set))


def run_drawing_until_completed():
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
if run_drawing_until_completed():
    print('Success. You are awesome.')
    write_full_results()
    write_individual_results()
