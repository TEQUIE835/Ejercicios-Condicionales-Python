print("Bienvenido")

while True:
    try:
        num=int(input("\nIngrese un numero entero: "))
        break
    except: print("\nIngrese un numero valido")
    

if num<0:
    print(f"\n{num} es un numero negativo")
elif num==0:
    print(f"\n{num} es igual a 0")
elif num>0:
    print(f"\n{num} es un numero positivo")
else: print("\nIngrese un numero valido")