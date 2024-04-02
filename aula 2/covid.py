cov= int(input("1- para positivo \n2- para negativo\n"))
temp= float(input("digite sua temperatura: \n"))
doses= int(input("numero de doses: \n"))

if temp>27:
    if cov==1 or doses<3:
        print("7 dias")
elif cov==1:
    print ("7 dias")
else:
    print("está liberado")