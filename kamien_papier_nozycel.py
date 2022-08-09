import random

Wybor = ['kamien','papier','nozyce']
Komputer = random.choice(Wybor)
Gracz = input('Wybierz nozyce kamien czy papier: ')
print('Komputer wybral: '+ Komputer)
print('Gracz numer 2 wybral: '+Gracz)
while True:
    if Komputer == 'nozyce' and Gracz == 'papier':
        print('Wygral Komputer')
        break
    elif Komputer == 'kamien' and Gracz == 'nozyce':
        print('Wygral Komputer')
        break
    elif Komputer == 'papier' and Gracz == 'kamien':
        print('Wygral Komputer')
        break
    elif Komputer == Gracz:
        print('Remis!!')
        break
    else:
        print('Wygrales Brawo!!')
        break