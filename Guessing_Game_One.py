import random

ilprob = 1
losowa = random.randint(1, 9)
print(losowa)
print('Siema zgadnij liczbe od 1 do 9')


def proba():
    global ilprob, losowa
    gracz = int(input('Jaki jest twoj wybor: '))
    if gracz != losowa:
        ilprob += 1
        print('Nie udalo ci sie zgadnac')
        if gracz > losowa:
            print('Twoja liczba jest za duza')
        else:
            print('Twoja liczba jest za mala')
        proba()
    elif gracz == losowa:
        print('Udalo ci sie zgadnac w ' + str(ilprob) + ' probach')
        return


proba()