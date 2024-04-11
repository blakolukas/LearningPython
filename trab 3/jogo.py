from random import randint

while True:
    op=int(input("gostaria de jogar?\n1-sim\n2-não\n"))
    if op==1:
        jogadas= 0
        while jogadas<5:
            dado= randint(1,6)
            jogadas+=1
            if dado==1:
                print('|---|\n|   |\n| o |\n|   |\n|---|\n\n')
            if dado==2:
                print('|---|\n|o  |\n|   |\n|  o|\n|---|\n\n')
            if dado==3:
                print('|---|\n|o  |\n| o |\n|  o|\n|---|\n\n')
            if dado==4:
                print('|---|\n|o o|\n|   |\n|o o|\n|---|\n\n')
            if dado==5:
                print('|---|\n|o o|\n| o |\n|o o|\n|---|\n\n')
            if dado==6:
                print('|---|\n|o o|\n|o o|\n|o o|\n|---|\n\n')
    else:
        print("jogo encerrado")
        break








