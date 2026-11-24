contador = 3

while contador <= 5:
    print(f"Paso numero {contador}")
    
    contador = contador + 1

print("---------------------------")

meta = 500
ahorra = 0

while ahorra < meta:

    aporte = float(input("Cuanto desea ahorrar?: "))

    if aporte <= 0:
        print("El aporte debe ser mayor que cero")
        continue

    ahorra += aporte

    print(f"Total ahorrado: C$ {ahorra:.2f}")

print("Felicidades has alcanzado tu meta")
