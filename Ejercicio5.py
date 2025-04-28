import random
print("-" * 40)
print("                 Bienvenido")
print("-" * 40)


numa=random.randint(1, 10)
intentos= 3

print(f"\nTienes {intentos} intentos")
while intentos > 0:
    
    
    try:
            numu=int(input("\nIngrese un numero del 1 al 10: "))
            if 0<numu<=10:
                pass
            else: 
                print("\nIngrese un numero valido")
                continue
    except: print("\nIngrese numero valido")
    if numu==numa: 
        print("\nHas adivinado el numero")
        break
    elif numu<numa:
        print("\nEl numero es mayor")
        intentos = intentos-1
    elif numu>numa:
        print("\nEl numero es menor")
        intentos = intentos-1
    print(f"\nTienes {intentos} intentos")


if intentos>0:
    pass
elif intentos<=0:
    print("\nQue pendejo no adivinaste")
        
