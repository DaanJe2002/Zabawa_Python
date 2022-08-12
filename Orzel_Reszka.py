import random
import time
def orzel_czy_reszka():
    runda = 1
    punkty_gracz = 0
    punkty_komputer = 0
    zbior = ['Orzel','Reszka']
    Komputer = random.choice(zbior)
    print('Runda ' + str(runda))
    print('_____________________________________')
    #for
    Gracz = input('Twoj typ: ')
    print('Komputer wybral: ' + Komputer)
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