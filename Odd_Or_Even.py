num = int(input('Podaj dzielnik: '))
check = int(input('Podaj liczbe: '))
if num % 4 == 0:
    print('Liczba jest wielokrotnosica 4')
elif num % 2 == 0:
    print('Liczba jest parzysta')
else:
    print('Liczba jest nieparzysta')
if check % num == 0:
    print('Liczba '+ str(check) + ' dzieli sie przez ' + str(num))
else:
    print('Liczba ' + str(check) + ' nie jest dzielnikiem ' + str(num))