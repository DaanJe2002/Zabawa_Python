lista = [1,4,-20,7]
najm = None
najw = None
for i in lista:
    if najm == None or najm > i:
        najm = i
    if najw == None or najw < i:
        najw = i

print('najmniejsza liczba to '+str(najm))
print('najwieksza liczba to '+str(najw))