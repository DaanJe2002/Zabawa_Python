dzielniki = []
x = range(1,999999)
num = int(input('Podaj numer: '))
for i in x:
    if num % i == 0:
        dzielniki.append(i)
print('Dzielniki liczby: ' + str(num)+': '+ str(dzielniki))
