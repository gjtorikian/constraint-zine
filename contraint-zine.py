from random import choice

location = ['THE WORLD',
            'THIS HOME',
            'YOUR SOUL',
            'AN INMATE',
            'THAT LIFE',
            'THE SCALE',
            'YOUR TEXT',
            'THAT CELL',
            'YOUR FACE',
            'AN ENERGY']

state = ['IS TRULY',
         'WAS THEN',
         'SHALL BE']

verb = ['RECOVERED',
        'DESTROYED',
        'THRUSTING',
        'SCATTERED',
        'SANITIZED',
        'PRESERVED',
        'ASSAULTED',
        'COARSENED',
        'HARVESTED',
        'INCUBATED',]


def phrase(idx):
    if idx == 0 or idx == 3 or idx == 6:
        text = choice(location) + ' ' + state[0] + ' ' + choice(verb)
    elif idx == 1 or idx == 4 or idx == 7:
        text = choice(location) + ' ' + state[1] + ' ' + choice(verb)
    elif idx == 2 or idx == 5 or idx == 8:
        text = choice(location) + ' ' + state[2] + ' ' + choice(verb)
    return text

for i in range(6):
    for j in range(9):
        print(phrase(j) + '.')

    print('')
