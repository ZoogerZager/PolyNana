import os
from random import choice
from time import time

class Participant:

    def __init__(self, name, restricted_set=None, giving_to=None):
        self.name = name
        self.restricted_set = restricted_set
        self.giving_to = giving_to

    def build_history(self):
        with open('history.txt', 'r') as history:
            for line in history:
                if line.rsplit()[0] == self.name:
                    for name in line.rsplit()[1:]:
                        self.restricted_set.add(name)


class Hat:

    def __init__(self, contents=None):
        self.contents = set([participant.name for participant in participants])


    def select(self, participant):
        return choice(list(self.contents - participant.restricted_set))


class Results:

    def __init__(self, results_directory=os.getcwd() + '\Results'):
        self.results_directory = results_directory
        if not os.path.exists(results_directory):
            os.mkdir(results_directory)
        if not os.path.exists(results_directory + '\Individual_Results'):
            os.mkdir(results_directory + '\Individual_Results')

    def write_full_results(self):
        os.chdir(self.results_directory)
        with open('full_results.txt', 'w') as f:
            for participant in participants:
                f.write(participant.name + ' --> ' + participant.giving_to + '\n')


    def write_individual_results(self):
        os.chdir(self.results_directory + '\Individual_Results')
        for participant in participants:
            filename = '%s.txt' % participant.name
            with open(filename, 'w') as file:
                file.write(participant.giving_to)


def build_participants():
    participants = []
    with open('data.txt', 'r') as data:
        for line in data:
            if not line.startswith('#'):
                participants.append(Participant(line.rsplit()[0], set(line.rsplit())))
    return participants


def build_all_history():
    for participant in participants:
        participant.build_history()


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


start_time = time()
participants = build_participants()
build_all_history()
if run_drawing_until_completed():
    print('Success. You are awesome.')
    results = Results()
    results.write_full_results()
    results.write_individual_results()
print('Runtime: %s seconds' % round((time() - start_time), 5))
