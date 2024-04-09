x=1
total=0
media=0
med=-1
imp=0

while x<=10:
    med= float(input("\nmedida: "))
    print(med)
    if med%2!=0:
        imp= imp+med
    media= imp/x
    x+=1
if imp==0:
    print("não foi possivel calcular")
else:
    print(f"\nmédia final: {media}")