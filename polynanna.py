from random import choice, shuffle
import participants


class PolyNanna:
    """This class contains stats, the drawing logic, and all data."""

    def __init__(self, _participants=None):
        self._participants = participants.main()
        shuffle(self._participants)
        self.failcount = 0


    def run_drawing(self, completed=False):
        """Build a Hat and make selections until a valid result is achieved.

        The try/except block works by iterating over hat contents and making
        selections. If no selection is available (No valid gift recipient for a
        participant), it will raise an IndexError add to the failcount, and
        restart the while loop.
        """
        while not completed:
            hat = Hat(self._participants)
            try:
                for participant in self._participants:
                    participant.giving_to = hat.select(participant)
                    hat.contents.remove(participant.giving_to)
                completed = True
            except IndexError:
                self.failcount += 1
        return completed

class Hat:
    """This class represents the valid participants still in the drawing."""

    def __init__(self, contents):
        self.contents = contents
        self.contents = set([participant.name for participant in self.contents])


    def select(self, participant):
        """takes a participant and returns a valid selection out of the hat."""
        return choice(list(self.contents - participant.restricted_set))


def main():
    polyanna = PolyNanna()
    polyanna.run_drawing()
    polyanna._participants = sorted(polyanna._participants, key=lambda p: p.name)
    return polyanna


if __name__ == '__main__':
    main()
