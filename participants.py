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
                'Amanda': {'Amanda', 'Stefan' ,'Angela'},
                'Angela': {'Angela', 'Renee', 'Jeff', 'Nanna', 'Stefan', 'Justin', 'Amanda'},
                # 'David': {'David', 'Jeff', 'Joe', 'Adam', 'Shaina'},
                'Francesca': {'Francesca', 'Renee', 'George'},
                'George': {'George', 'Renee', 'Francesca'},
                'Jeff': {'Jeff', 'Renee', 'Angela', 'Nanna', 'Joe', 'Adam', 'David'},
                'Joe': {'Joe', 'Jeff', 'David', 'Adam', 'Adrienne'},
                'Justin': {'Justin', 'Angela', 'Stefan'},
                # 'Nanna': {'Nanna', 'Jeff', 'Angela', 'Renee'}, Nanna is not participating.
                'Renee': {'Renee', 'Jeff', 'Angela', 'Nanna', 'Francesca', 'George'},
                # 'Shaina': {'Shaina', 'David'},
                'Stefan': {'Stefan', 'Angela', 'Justin', 'Amanda'},
}

history = {'Adam': [(2015, 'Justin'), (2016, 'Amanda'), (2017, 'Angela'), (2018, 'Stefan')],
           'Adrienne': [(2016, 'Jeff'), (2017, 'Stefan'), (2018, 'Justin')],
           'Amanda': [(2015, 'Adam'), (2016, 'Adrienne'), (2017, 'Jeff'), (2018, 'George')],
           'Angela': [(2015, 'Joe'), (2016, 'David'), (2017, 'Francesca'), (2018, 'Adrienne')],
           'David': [(2015, 'Stefan'), (2016, 'Francesca'), (2017, 'Renee')],
           'Francesca': [(2015, 'Angela'), (2016, 'Joe'), (2017, 'Adam'), (2018, 'Jeff')],
           'George': [(2015, 'Jeff'), (2016, 'Angela'), (2017, 'Adrienne'), (2018, 'Joe')],
           'Jeff': [(2015, 'Nanna'), (2016, 'Justin'), (2017, 'Shaina'), (2018, 'Amanda')],
           'Joe': [(2015, 'Renee'), (2016, 'George'), (2017, 'Justin'), (2018, 'Angela')],
           'Justin': [(2015, 'Francesca'), (2016, 'Adam'), (2017, 'George'), (2018, 'Renee')],
           'Nanna': [(2015, 'David')],
           'Renee': [(2015, 'Amanda'), (2016, 'Stefan'), (2017, 'David'), (2018, 'Adam')],
           'Shaina': [(2017, 'Amanda')],
           'Stefan': [(2015, 'George'), (2016, 'Renee'), (2017, 'Joe'), (2018, 'Francesca')],       
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