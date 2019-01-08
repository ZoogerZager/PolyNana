"""
How to Use this File.

participants is a dictionary where a key is the name of the participant and the value is
a set of all the invalid selections for that participant.

participants = {'Bob': {'Sue', 'Jim'},
        'Jim': {'Bob', 'Betty'},
}       # And so on.

history is a dictionary where a key is the name of the participant and the value
is  a list of tuples that contain a year and that participant's recipient
for that year.

history = {'Bob': [(2010, 'Betty'), (2011, 'Freddie')],
           'Jim': [(2011, 'Sue']
           # And so on.
}
"""

participants = {'Adam': {'Adam', 'Jeff', 'Joe', 'David'},
                'Adrienne': {'Adrienne', 'Joe'},
                # 'David': {'David', 'Joe', 'Adam', 'Shaina'},
                'Phil': {'Phil', 'Kara'},
                'Kara': {'Micki', 'Kara'},
                'Joe': {'Joe', 'David', 'Adam', 'Adrienne'},
                'Micki': {'Micki', 'Kara'},
                # 'Shaina': {'Shaina', 'David'},
}

history = {'Adam': [(2018, 'Phil')],
           'Adrienne': [(2018, 'Micki')],
           # 'David': [],
           'Micki': [(2018, 'Adrienne')],
           'Kara': [(2018, 'Joe')],
           'Phil': [(2018, 'Adam')],
           'Joe': [(2018, 'Kara')],
           # 'Shaina': [],  
}


class Participant:
    """The class for individual participants that contains their attributes."""

    def __init__(self, name, restricted_set=None, giving_to=None):
        self.name = name
        self.restricted_set = restricted_set
        self.restricted_set = participants.get(self.name)|set([y[1] for y in history.get(self.name)])
        self.giving_to = giving_to


def main():
    return sorted([Participant(p) for p in participants.keys()],
                   key=lambda p: len(p.restricted_set), reverse=True)


if __name__ == '__main__':  
    main()
