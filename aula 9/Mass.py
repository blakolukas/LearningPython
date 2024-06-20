import matplotlib.pyplot as graph
from numpy import arange

a=False
listPeso=[]
i=0
while a!=True:
    peso= int(input(f"seu peso na semana {i}:\n"))
    listPeso.append(peso)
    v= int(input("gerar gráfico?\n1-sim\n2-não\n"))
    if v==1:
        a=True
    i+=1

graph.figure(1)
graph.plot(arange(0,i),listPeso,'o--')
graph.title("peso")
graph.xlabel("tempo")
graph.ylabel("massa")
graph.grid(True)
graph.show()

v= int(input("gerar gráfico?\n1-sim\n2-não\n"))
if v==1:
    listP=[]
    listL=[]
    t=0

    while t<(len(listPeso)-1):
        p= (1-(listPeso[t+1]/listPeso[t]))*100
        first= (1-(listPeso[t+1]/listPeso[0]))*100
        listP.append(p)
        listL.append(first)
        t+=1
   
    graph.figure(2)
    graph.plot(arange(1,i),listP,'o--',arange(1,i),listL,'ro--')
    graph.title("peso")
    graph.xlabel("tempo")
    graph.ylabel("%")
    graph.grid(True)
    graph.show()