lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
numer = int(input('Podaj numer: '))
mniejsze = []
for i in lista:
    if i < numer:
        #print(i)
        mniejsze.append(i)
print(mniejsze)