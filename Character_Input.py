def stowka():
    name = input("Podaj prosze swoje imie:  ")
    age = int(input('Podaj prosze swoj wiek: '))
    kopy = int(input('Podaj jaka liczbe kopi wiadomosci chcesz otrzymac: '))
    rokur = 2022 - age
    stowka = rokur + 100
    for i in range(kopy):
        print('Czesc ' + str(name) + ' bedziesz mial sto lat w ' + str(stowka) + '!!!!')
stowka()