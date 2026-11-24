edad = int(input("Ingrese su edad: "))

promocion = input("Tiene un codigo promocional (S/N): ").lower()

if edad <= 0:
     print("Edad invalida, no se puede realizar la compra")
else:
    if edad < 12:
        categoria = "Niño"
        precio = 50
    elif edad <= 17:
        categoria = "Adolecente"
        precio = 80
    elif edad <= 64:
        categoria = "Adulto"
        precio = 120
    else:
        categoria = "Adulto mayor"
        precio = 70

if promocion == "s":
    descuento = precio * 0.10
else:
    descuento = 0

total = precio - descuento

print("\n------FESTIVAL-------\n")
print(f"Categoria: {categoria}")
print(f"Precio: C$ {precio:.2f}")
print(f"Descuento: C$ {descuento:.2f}")
print(f"Total a pagar: C$ {total:.2f}")