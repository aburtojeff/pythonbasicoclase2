pin = "555"
usuarioPIN = input("Ingrese el PIN: ")
intentos = 3

for p in range(1,4):
    restantes = intentos - p 
    if pin == usuarioPIN:
        print("Acceso autorizado")
        break

    elif pin != usuarioPIN:
            print("PIN incorrecto")
            print(f"Intentos restantes: {restantes}")

            usuarioPIN = input("Ingrese el PIN: ")
            
            if restantes == 0 :
                 print(f"Usuario bloqueado ")
     