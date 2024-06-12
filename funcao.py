
def funcao(inf=int,sup=int,qnt=int,rep=bool):
    from random import randint
    numeros=[]

    if inf>=sup:
        return "inf deve ser menor que sup"
    if rep==True:
        while len(numeros)<qnt:
            numeros.append(randint(inf,sup))
        return numeros
    else:
        while len(numeros)<qnt:
            ran=randint(inf,sup)
            if check(ran,numeros)==False:
                numeros.append(ran)
    return numeros

def check(num,vet):
    for i in range (len(vet)):
        if num==vet[i]:
            return True
    return False

a= int(input("inferior\n"))
b= int(input("superior\n"))
c= int(input("quantidade\n"))
d= int(input("repetição?\n1-sim\n2-não\n"))
if d==1:
    e=True
else:
    e=False

v= funcao(a,b,c,e)
print(v)
