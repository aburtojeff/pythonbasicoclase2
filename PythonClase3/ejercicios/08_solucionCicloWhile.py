pin_correcto = "123"
intentos = 0

while intentos < 3:
    pin = input("Ingrese su PIN: ")

    if pin == pin_correcto:
        print("Acceso autorizado")
        break

    intentos += 1

    print("PIN incorrecto")

    if intentos < 3:
        print(f"Intentos restantes: {3 - intentos}")

if intentos == 3:
    print("Usuario bloqueado")