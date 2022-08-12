import random
import time

runda = 1
punkty_gracz = 0
punkty_komputer = 0

def orzel_czy_reszka():
    global runda,punkty_komputer,punkty_gracz
    while True:
        zbior = ['Orzel','Reszka']
        Komputer = random.choice(zbior)
        print('Runda ' + str(runda))
        print('_____________________________________')
        Gracz = input('Twoj typ: ')
        if Gracz == 'Koniec':
            print('Koniec Gry')
            print('Punkty komputera: ' + str(punkty_komputer) + ' Punkty gracza: ' + str(punkty_gracz))
            break
        print('Komputer wybral: ' + Komputer)
        for i in range(0, 3):
            print(3 - i)
            time.sleep(1)
        wynik = random.choice(zbior)
        print('Wypadl/a:' + wynik)
        if Gracz == wynik and Komputer == wynik:
            print('Remis')
            print('Punkty komputera: ' + str(punkty_komputer) + ' Punkty gracza: ' + str(punkty_gracz))
            runda += 1
            return orzel_czy_reszka()
        elif Gracz == wynik and Komputer != wynik:
            print('Wygral gracz!!')
            punkty_gracz += 1
            print('Punkty komputera: ' + str(punkty_komputer) + ' Punkty gracza: ' + str(punkty_gracz))
            runda += 1
            return orzel_czy_reszka()
        elif Gracz != wynik and Komputer != wynik:
            print('Nikt nie wygral')
            print('Punkty komputera: ' + str(punkty_komputer) + ' Punkty gracza: ' + str(punkty_gracz))
            runda += 1
            return orzel_czy_reszka()
        else:
            print('Wygral komputer')
            punkty_komputer += 1
            print('Punkty komputera: ' + str(punkty_komputer) + ' Punkty gracza: ' + str(punkty_gracz))
            runda += 1
            return orzel_czy_reszka()

orzel_czy_reszka()