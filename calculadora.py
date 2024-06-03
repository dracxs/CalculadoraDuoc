num1=int(input("Numero 1: "))
num2=int(input("Numero 2: "))
num3=int(input("Numero 3: "))
valor=0
while True:
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Salir")
    opcion=int(input("Opcion: "))
    if opcion==1:
        valor=num1+num2+num3
        print("Resultado: ",valor)
    elif opcion==2:
        valor=num1-num2-num3
        print("Resultado: ",valor)
    elif opcion==3:
        valor=num1*num2*num3
        print("Resultado: ",valor)
    elif opcion==4:
        valor=num1/num2/num3
        print("Resultado: ",valor)
    elif opcion==5:
        break
    else:
        print("Opcion incorrecta")