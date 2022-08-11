wyraz = 'Dawid lubi male kotki'
slowa = 1
litery = 0
hash_table = {}
for i in wyraz:
    if i == ' ':
        slowa += 1
print('Ilosc slow w tym zdaniu wynosi: ' + str(slowa))
for i in wyraz:
    if i != ' ':
        litery += 1
print('Ilosc liter w tym zdaniu wynosi: ' + str(litery))
for i in wyraz:
    if i in hash_table:
        hash_table[i] += 1
    else:
        hash_table[i] = 1
print('Szczegoly twojego wyrazu -- > ' + str(hash_table))

