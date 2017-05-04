import data
import os
from random import choice, shuffle


class Polyanna:
    """This class contains stats, the drawing logic, and all data."""

    def __init__(self, participants=None):
        self.participants = []
        self.failcount = 0
        self._print = True
        self._write = False
        self._print_all_recipients = False


    def get_participant_by_name(self, name):
        person = [p for p in self.participants if p.name.lower() == name.lower()]
        return person[0]


    def build_participants(self):
        """Builds a list of Participant objects from Data.py and shuffles it."""
        for key, restricted in data.data.items():
            self.participants.append(Participant(key, set(restricted)))
        shuffle(self.participants) # Adds noise to selection decision tree.


    def build_all_history(self):
        """Iterates over participants and removes prior years' selections."""
        for participant in self.participants:
            participant.build_history()

    def print_all_possible_recipients(self):
        """For each participant, print possibilities to console

        Note:
            This should be run after build_all_history().
        """
        for participant in self.participants:
            print(participant.name, ' --> ',
            set([p.name for p in self.participants]) - participant.restricted_set)


    def run_drawing_until_completed(self):
        """Build a Hat and make selections until a valid result is achieved.

        The try/except block works by iterating over hat contents and making
        selections. If no selection is available (No valid gift recipient for a
        participant), it will raise an IndexError add to the failcount, and
        restart the while loop.
        """
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
    """The class for individual participants that contains their attributes."""

    def __init__(self, name, restricted_set=None, giving_to=None):
        self.name = name
        self.restricted_set = restricted_set
        self.giving_to = giving_to

    def build_history(self):
        """Adds previous gift recipients to a Participant's restricted_set."""
        for year in data.history[self.name]:
            self.restricted_set.add(year[1])


class Hat:
    """This class represents the valid participants still in the drawing."""

    def __init__(self, contents):
        self.contents = contents
        self.contents = set([participant.name for participant in self.contents])


    def select(self, participant):
        """takes a participant and returns a valid selection out of the hat."""
        return choice(list(self.contents - participant.restricted_set))


class Results:
    """This class handles the I/O file operations and offers console output."""

    def __init__(self, polyanna, results_directory=os.getcwd() + '\Results'):
        self.polyanna = polyanna
        self.results_directory = results_directory
        if not os.path.exists(results_directory):
            os.mkdir(results_directory)
        if not os.path.exists(results_directory + '\Individual_Results'):
            os.mkdir(results_directory + '\Individual_Results')

    def print_results(self):
        """Print results to the console."""
        for participant in self.polyanna.participants:
            print('{:<9} -->  {}'.format(participant.name, participant.giving_to))


    def write_full_results(self):
        """Write results to a .txt file."""
        os.chdir(self.results_directory)
        with open('full_results.txt', 'w') as f:
            for participant in self.polyanna.participants:
                f.write('{:<9} -->  {} \n'.format(participant.name, participant.giving_to))


    def write_individual_results(self):
        """Write individual results to separate files.

        Note:
            This is to keep the program's selections confidential from the
            program's operator. Participants can be instructed to open the .txt
            file with their name, it will provide their intended recipient.
        """
        os.chdir(self.results_directory + '\Individual_Results')
        for participant in self.polyanna.participants:
            filename = '{}.txt'.format(participant.name)
            with open(filename, 'w') as file:
                file.write(participant.giving_to)


def main():
    polyanna = Polyanna()
    polyanna.build_participants()
    polyanna.build_all_history()
    if polyanna.run_drawing_until_completed():
        results = Results(polyanna)
        if polyanna._print_all_recipients:
            polyanna.print_all_possible_recipients()
        if polyanna._print:
            results.print_results
        if polyanna._write:
            results.write_full_results()
            results.write_individual_results()
    print('Fail Count: ', polyanna.failcount)
    polyanna.participants = sorted(polyanna.participants, key=lambda p: p.name)
    return polyanna

if __name__ == '__main__': main()
