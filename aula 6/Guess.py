from random import randint
import time as time
ok=0
times=0
num= randint(0,2)
inicio= time.time()

while ok!=1:
    a= float(input(f"tentantivas: {times} \ndiga um número: "))
    times+=1
    if a==num:
        print("acertou!")
        break

fim= time.time()

per= fim-inicio

print(f"segundos para concluir: {per} seg")