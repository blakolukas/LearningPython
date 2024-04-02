x=1
total=0
media=0

while x<=10:
    med= float(input("\nmedida: "))
    total= total + med
    media= total/x
    x+=1
    if abs(med-media)>(media*0.5):
        print("!!!!!!alerta!!!!!!")
    print(f"média: {media}")
print(f"\nmédia final: {media}")