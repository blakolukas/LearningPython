from math import sin
import matplotlib.pyplot as graph
from numpy import arange

graph.figure(1)
x=[1,2,5,8]
y=[2,5,-1,0]
y2=[10,10,20,3]
graph.plot(x,y,'r:o',x,y2,'b--s')
graph.title("algo")
graph.xlabel("Coisa")
graph.ylabel("Alguma")
graph.legend(["sum","blu"])
graph.grid(True)
graph.show()

graph.figure(2)
t= arange(0,30,0.1)
v=[]
for k in range (len(t)):
    v[k]= 100*sin(10*t[v])/t[v]
graph.plot(t,v)
graph.show