import random
dl_listy_a = int(input('Podaj dl listy a : '))
dl_listy_b = int(input('Podaj dl listy b : '))
a = []
b = []
nowa = []
for i in range(dl_listy_a):
    a.append(random.randint(1,40))
    a.sort()
print(a)
for i in range(dl_listy_b):
    b.append(random.randint(1,40))
    b.sort()
print(b)
for i in a:
    if i in b and i not in nowa:
        nowa.append(i)
print(nowa)
