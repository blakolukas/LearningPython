nome= input("escreva seu nome: \n")
um= float(input("nota 1: \n"))
dois= float(input("nota 2: \n"))
faltas= int(input("quantas faltas? \n"))

notas= ((um)*(dois))**0.5
repf= (60-faltas)/60

if repf < 0.75:
    print("\nreprovado por falta!")
elif notas<7 and notas>=4:
    print("\nvocê pegou recuperação!")
    print(f"\nsua nota: {notas}")
    recn= float(input("nota da G2: "))
    gg= (notas+recn)/2
    if gg<5:
        print("\nreprovou por média!")
    else:
        print(f"\npassou! \nsua nota: {gg}")
elif notas>7:
    print(f"\npassou!\nsua nota: {notas}")
elif notas<4:
    print("\nreprovado por média na G1!")
    print(f"sua nota: {notas}")