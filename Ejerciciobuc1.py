print("-" *40)
print("         Bienvenido")
print("-" * 40)

while True:
    try:
        mult=int(input("\nIngrese un numero del 1 al 10: "))
        if 0<mult<=10:
            break
        else:print("\nIngrese un numero valido")
    except: print("\nIngrese un numero valido")

print("\nEsta es la tabla de multiplicar:\n")
for i in range(1,11):
    mul=mult*i
    print(mul)