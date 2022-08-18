sen = input('Podaj jakies wyraz: ')
lista = []
for i in sen:
    lista.append(i)
if lista[0:-1] == lista[:0:-1]:
    print('Wyraz jest palindormem')
else:
    print('wyraz nie jest palindromem')

#print(lista[0:-1])
#print(lista[:0:-1])

