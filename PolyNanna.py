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


    def select(self, participant):
        return choice(list(self.contents - participant.restricted_set))


class Results:

    def write_full_results(self):
        with open('full_results.txt', 'w') as f:
            for participant in participants:
                f.write(participant.name + ' --> ' + participant.giving_to + '\n')

    def write_individual_results(self):
        individual_results_directory = os.getcwd() + '\Individual_Results'
        if not os.path.exists(individual_results_directory):
            os.mkdir(individual_results_directory)
        os.chdir(individual_results_directory)
        for participant in participants:
            filename = '%s.txt' % participant.name
            with open(filename, 'w') as file:
                file.write(participant.giving_to)


def build_participants():
    participants = []
    with open('data.txt', 'r') as data:
        for line in data:
            participants.append(Participant(line.rsplit()[0], set(line.rsplit())))
    return participants


def run_drawing_until_completed():
    completed = False
    count = 0
    while not completed:
        hat = Hat()
        try:
            for participant in participants:
                participant.giving_to = hat.select(participant)
                hat.contents.remove(participant.giving_to)
            completed = True
            print('Fail Count: ', count)
        except IndexError:
            completed = False
            count += 1
    return completed


participants = build_participants()
if run_drawing_until_completed():
    print('Success. You are awesome.')
    results = Results()
    results.write_full_results()
    results.write_individual_results()
