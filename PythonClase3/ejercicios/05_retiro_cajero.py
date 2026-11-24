saldo = float(input("Ingrese su saldo disponible: "))
monto = float(input("Ingrese el monto a retirar: "))

if saldo < 0:
    mensaje = "Error en la informacion"

if saldo <= 0:
    mensaje = "Su operacion ha sido rechazada"
elif monto > saldo:
    mensaje = "No se puede hacer su retiro"
else:
    mensaje = "Su retiro ha sido autorizado"

total = saldo - monto

print("\n-------CAJERO AUTOMATICO--------\n")
print(mensaje)
print(f"Su saldo restante: C$ {total}")

