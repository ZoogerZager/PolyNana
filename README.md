# PolyNanna
A program designed to randomize a pollyanna gift exchange with familial restrictions.

Rule Specifications
- Parents cannot give to their children.
- Children cannot give to their parents.
- Siblings cannot give to each other.
- Spouses/Couples cannot give to each other.

data.txt contains a list of plain text names followed by names of those who are not
valid gift recipients on the same line. White space is for readability.
example:

Bob       Jim John
Bob is a participant and he cannot give to either Jim or John.

The program outputs a group of .txt files named with the participant name
and that contain the name of their gift recipient.
example:

Bob.txt     contains     Jill
Bob is giving to Jill for this Polyanna. 

The program will also output a file with all the results called full_results.txt for reference.

to run:
1. navigate to the PolyNanna directory
2. run python PolyNanna.py  (on linux: python3 PolyNanna.py)
