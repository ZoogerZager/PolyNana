import data
from random import choice, shuffle


class Polyanna:
    """This class contains stats, the drawing logic, and all data."""

    def __init__(self, participants=None):
        self.participants = []
        self.failcount = 0


    def build_participants(self):
        """Builds a list of Participant objects from Data.py and shuffles it."""
        for key, restricted in data.data.items():
            self.participants.append(Participant(key, set(restricted)))
        shuffle(self.participants) # Adds noise to selection decision tree.


    def build_all_history(self):
        """Iterates over participants and removes prior years' selections."""
        for participant in self.participants:
            participant.build_history()


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


def main():
    polyanna = Polyanna()
    polyanna.build_participants()
    polyanna.build_all_history()
    polyanna.run_drawing_until_completed()
    polyanna.participants = sorted(polyanna.participants, key=lambda p: p.name)
    return polyanna

if __name__ == '__main__': main()
