import random
print("-" * 40)
print("                 Bienvenido")
print("-" * 40)



adiv = False
numa=random.randint(1, 10)



for i in range (1, 4):
    while True:
        try:
            numu=int(input("\nIngrese un numero del 1 al 10: "))
            if 0<numu<=10:
                break
            else: print("\nIngrese un numero valido")
        except: print("\nIngrese numero valido")
    if numu==numa: 
        print("\nHas adivinado el numero")
        adiv = True
        break
    elif numu<numa:
        print("\nEl numero es mayor")
    elif numu>numa:
        print("\nEl numero es menor")


if adiv==True:
    pass
elif adiv == False:
    print("\nQue pendejo no adivinaste")
        
