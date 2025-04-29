import random
import sys
salir = False
print("-" * 40)
print("                 Bienvenido")
print("-" * 40)

def ran():
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
        print(f"\nQue pendejo no adivinaste, el numero era {numa}")
        
ran()
while salir !=True:
    vol= str(input("\nQuieres volver a jugar? N/Y\n")).upper()

    if vol=="Y" or vol == "YES":
        ran()
    elif vol == "N" or vol =="NO":
        print("\nNos vemos...")
        sys.exit()
    else:
        print("\nIngresa una opcion valida")