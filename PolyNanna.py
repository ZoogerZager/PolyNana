import os
from random import choice
from time import time

class Polyanna:

    def __init__(self, participants=None):
        self.participants = participants
        self.runtime = 0
        self.failcount = 0


    def build_participants(self):
        participants = []
        with open('data.txt', 'r') as data:
            for line in data:
                if not line.startswith('#'):
                    participants.append(Participant(line.rsplit()[0], set(line.rsplit())))
        self.participants = participants


    def build_all_history(self):
        for participant in self.participants:
            participant.build_history()


    def run_drawing_until_completed(self):
        completed = False
        while not completed:
            hat = Hat(self.participants)
            try:
                for participant in self.participants:
                    participant.giving_to = hat.select(participant)
                    hat.contents.remove(participant.giving_to)
                completed = True
            except IndexError:
                completed = False
                self.failcount += 1
        return completed


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
        self.contents = contents
        self.contents = set([participant.name for participant in self.contents])


    def select(self, participant):
        return choice(list(self.contents - participant.restricted_set))


class Results:

    def __init__(self, polyanna, results_directory=os.getcwd() + '\Results'):
        self.polyanna = polyanna
        self.results_directory = results_directory
        if not os.path.exists(results_directory):
            os.mkdir(results_directory)
        if not os.path.exists(results_directory + '\Individual_Results'):
            os.mkdir(results_directory + '\Individual_Results')

    def print_results(self):
        for participant in self.polyanna.participants:
            print(participant.name, '-->', participant.giving_to)


    def write_full_results(self):
        os.chdir(self.results_directory)
        with open('full_results.txt', 'w') as f:
            for participant in self.polyanna.participants:
                f.write(participant.name + ' --> ' + participant.giving_to + '\n')


    def write_individual_results(self):
        os.chdir(self.results_directory + '\Individual_Results')
        for participant in self.polyanna.participants:
            filename = '%s.txt' % participant.name
            with open(filename, 'w') as file:
                file.write(participant.giving_to)

def main():
    start_time = time()
    polyanna = Polyanna()
    polyanna.build_participants()
    polyanna.build_all_history()
    if polyanna.run_drawing_until_completed():
        print('Success. You are awesome.')
        results = Results(polyanna)
        results.print_results()
        # results.write_full_results()
        # results.write_individual_results()
    polyanna.runtime = round((time() - start_time), 5)
    print('Runtime: {} seconds'.format(polyanna.runtime))
    print('Fail Count: ', polyanna.failcount)

if __name__ == '__main__': main()
