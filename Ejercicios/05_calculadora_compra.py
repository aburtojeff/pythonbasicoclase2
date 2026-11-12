precio_unitario = 125.50
cantidad = 3
descuento_porcentaje = 10

subtotal = precio_unitario * cantidad
descuento = subtotal * (descuento_porcentaje/100)
total = subtotal - descuento   

print("RESUMEN DE COMPRAS")
print(f"Sub Total: C$ {subtotal:.2f}")
print(f"Descuento: C$ {descuento}")
print(f"Total: C$ {total}")

print(total >= 300)