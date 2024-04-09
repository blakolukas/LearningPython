#guess the number

from random import randint
import time as time

times=0
num= randint(0,2)
inicio= time.time()
print("descubra o número!")

while True:
    a= int(input(f"\ntentantivas: {times} \ndiga um número: "))
    times+=1
    if a==num:
        print("acertou!")
        break

fim= time.time()
per= fim-inicio

print(f"\nsegundos para concluir: {per} seg \ntentativas: {times}") 