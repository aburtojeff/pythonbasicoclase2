

distancia = float(input("Ingrese la distancia en KM: "))

if distancia <= 0:
    tarifa = 0
elif distancia >= 3:
    tarifa = 30
elif distancia <= 8:
    tarifa = 50
else:
    tarifa = 75

if tarifa <= 0:
    mensaje = "Que camaine"
else: 
    mensaje = f"Tarifa: {tarifa}"

print("------- SERVICIO DE ENTREGA ---------")
if tarifa > 0:
    print(f"Distancia: {distancia}")
print(f"Tarifa: {mensaje}")
