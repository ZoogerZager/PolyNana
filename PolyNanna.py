import os
from random import choice


class Participant:

    def __init__(self, name, restricted_set=None, giving_to=None):
        self.name = name
        self.restricted_set = restricted_set
        self.giving_to = giving_to


class Hat:

    def __init__(self, contents=None):
        self.contents = set([participant.name for participant in participants])


    def select(self, participant, hat):
        okay_set = self.contents - participant.restricted_set
        return choice(list(okay_set))


class Results:

    def write_full_results(self):
        with open('full_results.txt', 'w') as f:
            for participant in participants:
                f.write(participant.name + ' --> ' + participant.giving_to + '\n')

    def write_individual_results(self):
        if not os.path.exists(os.getcwd() + '\Individual_Results'):
            os.mkdir(os.getcwd() + '\Individual_Results')
        os.chdir(os.getcwd() + '\Individual_Results')
        for participant in participants:
            filename = '%s.txt' % participant.name
            with open(filename, 'w') as file:
                file.write(participant.giving_to)


def build_participants():
    participants = []
    with open('data.txt', 'r') as data:
        for line in data:
            restricted_set = line.rsplit()
            participants.append(Participant(restricted_set[0], set(restricted_set)))
    return participants


def run_drawing_until_completed():
    completed = False
    while not completed:
        hat = Hat()
        try:
            for participant in participants:
                participant.giving_to = hat.select(participant, hat.contents)
                hat.contents.remove(participant.giving_to)
            completed = True
        except IndexError:
            completed = False
    return completed


participants = build_participants()
if run_drawing_until_completed():
    print('Success. You are awesome.')
    results = Results()
    results.write_full_results()
    results.write_individual_results()
