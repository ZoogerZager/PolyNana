from random import choice, shuffle
import participants


class PolyNanna:
    """This class contains stats, the drawing logic, and all data."""

    def __init__(self, _participants=None, hat=None,):
        self._participants = participants.main()
        self.hat = hat
        self.failcount = 0


    def run_drawing(self, completed=False):
        """Build a Hat and make selections until a valid result is achieved.

        The try/except block works by iterating over hat contents and making
        selections. If no selection is available (No valid gift recipient for a
        participant), it will raise an IndexError add to the failcount, and
        restart the while loop.
        """
        while not completed:
            self.hat = set([p.name for p in self._participants])
            try:
                for p in self._participants:
                    p.giving_to = choice(list(self.hat - p.restricted_set))
                    self.hat.remove(p.giving_to)
                completed = True
            except IndexError:
                self.failcount += 1
        return completed


def main():
    polyanna = PolyNanna()
    polyanna.run_drawing()
    polyanna._participants = sorted(polyanna._participants, key=lambda p: p.name)
    return polyanna


if __name__ == '__main__':
    main()
