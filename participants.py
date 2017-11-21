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

participants = {'Joe': {'Joe', 'Jeff', 'Dave', 'Adam', 'Adrienne'},
        'Dave': {'Dave', 'Jeff', 'Joe', 'Adam'},
        'Adam': {'Adam', 'Jeff', 'Joe', 'Dave'},
        'Justin': {'Justin', 'Angela', 'Stefan'},
        'Stefan': {'Stefan', 'Angela', 'Justin', 'Amanda'},
        'Amanda': {'Amanda', 'Stefan'},
        'Francesca': {'Francesca', 'Renee', 'George'},
        'Jeff': {'Jeff', 'Renee', 'Angela', 'Nanna', 'Joe', 'Adam', 'Dave'},
        'Angela': {'Angela', 'Renee', 'Jeff', 'Nanna', 'Stefan', 'Justin'},
        'Renee': {'Renee', 'Jeff', 'Angela', 'Nanna', 'Francesca', 'George'},
        'George': {'George', 'Renee', 'Francesca'},
#       'Nanna': {'Nanna', 'Jeff', 'Angela', 'Renee'}, Nanna is not participating.
        'Adrienne': {'Adrienne', 'Joe'},
}

history = {'Joe': [(2015, 'Renee'), (2016, 'George')],
           'Dave': [(2015, 'Stefan'), (2016, 'Francesca')],
           'Adam': [(2015, 'Justin'), (2016, 'Amanda')],
           'Justin': [(2015, 'Francesca'), (2016, 'Adam')],
           'Stefan': [(2015, 'George'), (2016, 'Renee')],
           'Amanda': [(2015, 'Adam'), (2016, 'Adrienne')],
           'Francesca': [(2015, 'Angela'), (2016, 'Joe')],
           'Jeff': [(2015, 'Nanna'), (2016, 'Justin')],
           'Angela': [(2015, 'Joe'), (2016, 'Dave')],
           'Renee': [(2015, 'Amanda'), (2016, 'Stefan')],
           'George': [(2015, 'Jeff'), (2016, 'Angela')],
           'Nanna': [(2015, 'Dave')],
           'Adrienne': [(2016, 'Jeff')],
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