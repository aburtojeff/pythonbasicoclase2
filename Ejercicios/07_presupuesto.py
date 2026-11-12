descripcion = input("Ingrese la descripcion del producto: ")
presupuesto = int(input("Ingrese el presupuesto disponible: "))
precio = float(input("Ingrese el precio: "))
cantidad = int(input("Ingrese la cantidad del producto: "))

total = precio * cantidad
saldo = total - presupuesto
suficiente = saldo > presupuesto

print("---------------------------------------")
print(f"El producto es: {descripcion}")
print(f"Presupuesto es: {presupuesto:.2f}")
print(f"El precio es: {precio}")
print(f"Cantidad del producto: {cantidad}")
print("----------------------------------------")
print(f"El total es: C$ {total:.2f}")
print(f"El saldo disponible es: C$ {saldo:.2f}")
print(f"Es suficiente: {suficiente}")