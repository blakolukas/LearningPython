notaum= float(input("primeira nota: "))
notad= float(input("segunda nota: "))
notat= float(input("terceira nota: "))

media= (notaum+notad+notat)/3

desvio= ((((notaum-media)**2)+((notad-media)**2)+((notat-media)**2))/3)**0.5

if(desvio>(media*0.1)):
    print("\n---ALERTA!---\n")

print(f"\nmédia: {media}")
print(f"desvio: {desvio}\n")