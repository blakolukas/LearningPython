x=1
total=0
media=0
med=-1

while x<=10:
    ignore= med
    med= float(input("\nmedida: "))
    total= total + med
    media= total/x
    x+=1
    if ignore<0:
        print()
    elif abs(ignore-media)>(media*0.5):
        print("!!!!!!alerta!!!!!!")
    print(f"média: {media}")
print(f"\nmédia final: {media}")