print("-" * 40)
print("                 Bienvenido")
print("-" * 40)

while True:
    try:
        cal=int(input("\nIngrese su calificacion: "))
        if 100>=cal>=60:
            print("\nFelicidades, has aprobado")
            break
        elif 0<=cal<60:
            print("\nLo siento, no has aprobado")
            break
        else: print("\nIngrese una calificacion valida")
    except: print("\nIngrese una calificacion valida")

