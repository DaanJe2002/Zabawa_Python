def sum():
    suma = 0
    list = [2,4,8,1,6,7]
    dl = len(list)
    for y in range(dl):
        for i in range(dl):
            if list[i] + list[y] == 9:
                print('znales liczbe essa')
                print(list[i],list[y])
                suma += 1
sum()
print(sum)







