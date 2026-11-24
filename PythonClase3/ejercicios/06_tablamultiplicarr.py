productos = ["arroz", "frijoles", "leche", "pan", "huevos"]

print (productos)

for p in productos:
    print(f"- {p}")

for dia in range(1,8):
    print(f"Dia {dia}: hacer ejercicios")

conteo = 0
for dia in range(1,8):
    conteo = conteo + 1

print(conteo)


numero = int(input("Ingrese un numero: "))

for n in range (1,13):
    r = numero * n
    print(f"{numero} x {n} = {r}")


