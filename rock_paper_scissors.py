
import time
print("Hello in Rock Paper Scissors game!!")
def gra():
    time.sleep(1.5)
    Gracz1 = input("What is your choice player 1?: ")
    time.sleep(0.5)
    print('Thanks for your choice, now player 2')
    time.sleep(1.5)
    Gracz2 = input('What is your choice player 2?: ')
    while True:
        if Gracz1 == 'Rock' and Gracz2 == 'Scissors':
            print('Player number 1 won !!!')
            nastepna = input('Do you want play again?: ')
            if nastepna == 'Yes':
                gra()
            else:
                print('Koniec gry!!')
                break
        elif Gracz1 == 'Scissors' and Gracz2 == 'Paper':
            print('Wygral Gracz 1 !!!')
            nastepna = input('Do you want play again?: ')
            if nastepna == 'Yes':
                gra()
            else:
                print('Koniec gry!!')
                break
        elif Gracz1 == 'Paper' and Gracz2 == 'Rock':
            print('Wygral Gracz 1 !!!')
            nastepna = input('Do you want play again?: ')
            if nastepna == 'Yes':
                gra()
            else:
                print('Koniec gry!!')
                break
        elif Gracz1 == Gracz2:
            print('Niestety remis sprobojmy jeszcze raz')
            gra()
        else:
            print('Wygral Gracz 2 !!!!')
            nastepna = input('Do you want play again?: ')
            if nastepna == 'Yes':
                gra()
            else:
                print('Koniec gry!!')
                break
            break
gra()