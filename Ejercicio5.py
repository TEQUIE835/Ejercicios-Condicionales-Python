import random
print("-" * 40)
print("                 Bienvenido")
print("-" * 40)


numa=random.randint(1, 10)
intentos= 3


while intentos > 0:
    print(f"Tienes {intentos} intentos")
    while True:
        try:
            numu=int(input("\nIngrese un numero del 1 al 10: "))
            if 0<numu<=10:
                break
            else: print("\nIngrese un numero valido")
        except: print("\nIngrese numero valido")
    if numu==numa: 
        print("\nHas adivinado el numero")
        break
    elif numu<numa:
        print("\nEl numero es mayor")
    elif numu>numa:
        print("\nEl numero es menor")


if intentos>0:
    pass
elif intentos<=0:
    print("\nQue pendejo no adivinaste")
        
