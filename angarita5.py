# Función que verifica si la persona tiene derecho al subsidio
def verificar_subsidio():
    # Recibir el nombre de la persona
    nombre = input("Ingrese el nombre de la persona: ")

    # Recibir el estrato socio-económico
    estrato = int(input("Ingrese el estrato socio-económico (entre 1 y 6): "))

    # Verificar que el estrato esté en el rango correcto
    if estrato < 1 or estrato > 6:
        print("El estrato debe estar entre 1 y 6.")
        return

    # Recibir el nivel de SISBEN
    sisben = int(input("Ingrese el nivel de SISBEN (entre 1 y 3): "))

    # Verificar que el nivel de SISBEN esté en el rango correcto
    if sisben < 1 or sisben > 3:
        print("El nivel de SISBEN debe estar entre 1 y 3.")
        return

    # Verificar si la persona tiene derecho al subsidio
    if estrato <= 2 and sisben < 2:
        print(f"{nombre}, usted tiene derecho al subsidio mensual en efectivo.")
    else:
        print(f"{nombre}, usted no tiene derecho a subsidio mensual en efectivo.")

# Llamar a la función para iniciar el proceso
verificar_subsidio()
