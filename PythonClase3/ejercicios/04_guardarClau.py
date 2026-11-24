def validar_compra(monto):

    if monto <= 0:
        return "Monto inválido"

    if monto > 5000:
        return "Requiere autorización"

    return "Compra permitida"


print(validar_compra(250))
print(validar_compra(0))
print(validar_compra(6000))