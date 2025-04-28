print("-" * 40)
print("                 Bienvenido")
print("-" * 40)

while True:
    try:
        cont=int(input("\nIngrese un numero positivo: "))
        if cont>0:
            break
        else: print("\nIngrese un numero valido")
    except: print("\nIngrese un numero valido")

print("\nTu cuenta regresiva: ")
while cont!=0:
    print(cont)
    cont=cont-1
