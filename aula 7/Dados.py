from random import randint

while True:
    op=int(input("gostaria de jogar?\n1-sim\n2-não\n"))
    if op==1:
        jogadas= 0
        x=0
        y=0
        vet= [[[" "],[" "],[" "]],[[" "],[" "],[" "]],[[" "],[" "],[" "]],[[" "],[" "],[" "]],[[" "],[" "],[" "]]]
        dados= [["|   |"],
                ["| o |"],
                ["|o o|"],
                ["|o  |"],
                ["|  o|"]
                ]
        num= [[0,1,0],[3,0,4],[3,1,4],[2,0,2],[2,1,2],[2,2,2]]
        a=0
        b=0
        print(num[2][0])
        while jogadas<5:
            dado= randint(1,6)
            vet[jogadas]= dado
            jogadas+=1
            while y < 2:
                if dado==1:
                    a=0
                    vet[x][y]=dados[num[a][b]]
                    b+=1
                    y+=1
                    
                if dado==2:
                    a=1
                    vet[x][y]=dados[num[a][b]]
                    b+=1
                    y+=1
                if dado==3:
                    a=2
                    vet[x][y]=dados[num[a][b]]
                    b+=1
                    y+=1
                if dado==4:
                    a=3
                    vet[x][y]=dados[num[a][b]]
                    b+=1
                    y+=1
                if dado==5:
                    a=4
                    vet[x][y]=dados[num[a][b]]
                    b+=1
                    y+=1
                if dado==6:
                    a=5
                    vet[x][y]=dados[num[a][b]]
                    b+=1
                    y+=1
            y=0
        x+=1
        print(vet)
    else:
        print("jogo encerrado")
        break

