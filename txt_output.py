import polynanna
import seed_db
from participants import participants, history

polyanna = polynanna.main()
with open('results/masterlist.txt', 'w') as file:
	for p in polyanna._participants:
		file.write(p.name + ' is giving to ' + p.giving_to + '\n')
for p in polyanna._participants:
    filename = 'results/' + p.name + '.txt'
    with open(filename, 'w') as file:
    	file.write(p.name + ' your gift recipient is ' + p.giving_to)



