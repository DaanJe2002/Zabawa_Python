import random
ilprob = 1
losowa = random.randint(1,9)
print(losowa)
print('Siema zgadnij liczbe od 1 do 9')
def proba():
    global ilprob,losowa
    gracz = int(input('Jaki jest twoj wybor: '))
    while True:
        if gracz == losowa:
            print('Udalo ci sie zgadnac w '+ str(ilprob) + ' probach' )
            break
        else:
            if gracz != losowa:
                ilprob += 1
                print('nie udalo ci sie zgadnac')
                proba()
proba()
