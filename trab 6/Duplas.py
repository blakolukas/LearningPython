from random import randint

nomes= []
duplas=[["",""],["",""],["",""],["",""],["",""]]

while len(nomes)<10:
    bota= input("\nnome:")
    nomes.append(bota)

print(f"nomes: {nomes}")
a=0
while(True): 
    b=0
    c= randint(0,len(nomes)-1)
    duplas[a][b]= nomes[c]
    nomes.remove(nomes[c])
    b=1
    c= randint(0,len(nomes)-1)
    duplas[a][b]= nomes[c]
    nomes.remove(nomes[c])
    a+=1
    if len(nomes)==0:
        break

print(f"\nduplas: {duplas}")
