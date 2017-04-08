# PolyNanna
A program designed to randomize a pollyanna gift exchange with familial restrictions.

## Getting Started

```
git clone https://github.com/joemarchese/polynanna
cd polynanna
python gui.py
```

## Prerequisites
Python 3.x

## How to Set Participants
Participants are set in the data.py file.

data is a dictionary where a key is the name of the participant and the value is a list of all the invalid selections for that participant.

```
data = {'Bob': ['Sue', 'Jim'],
        'Jim': ['Bob', 'Betty'],
}       # And so on.
```

history is a dictionary where a key is the name of the participant and the value is  a list of tuples that contain a year and that participant's recipient for that year.

```
history = {'Bob': [(2010, 'Betty'), (2011, 'Freddie')],
           'Jim': [(2011, 'Sue']
           # And so on.
}
```

## How to Use
To use the GUI:
```
python gui.py
```
For Command Line Only:
```
python polynanna.py
```

## Rule Specifications
- Parents cannot give to their children.
- Children cannot give to their parents.
- Siblings cannot give to each other.
- Spouses/Couples cannot give to each other.

## Authors

* **Joseph Marchese** - [joemarchese](https://github.com/joemarchese)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
