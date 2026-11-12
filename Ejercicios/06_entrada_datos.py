nombre = input("Ingrese su nombre: ")
precio_unitario = float( input('Precio unitario: '))
cantidad = int(input("Digite la cantidad: "))

#precio_unitario = 125.50
#cantidad = 3
descuento_porcentaje = 10

subtotal = precio_unitario * cantidad
descuento = subtotal * (descuento_porcentaje/100)
total = subtotal - descuento   

print(F"Nombre: {nombre}")
print("RESUMEN DE COMPRAS")
print(f"Sub Total: C$ {subtotal:.2f}")
print(f"Descuento: C$ {descuento:.2f}")
print(f"Total: C$ {total:.2f}")

print(total >= 300)