# Función que verifica si el empleado tiene derecho al subsidio
def verificar_subsidio():
    # Recibir el nombre del empleado
    nombre = input("Ingrese el nombre del empleado: ")

    # Recibir el estrato socio-económico
    estrato = int(input("Ingrese el estrato socio-económico (entre 1 y 6): "))

    # Verificar que el estrato esté en el rango correcto
    if estrato < 1 or estrato > 6:
        print("El estrato debe estar entre 1 y 6.")
        return

    # Recibir la antigüedad en años
    antiguedad = int(input("Ingrese la antigüedad en años en la entidad: "))

    # Verificar si el empleado tiene derecho al subsidio
    if estrato < 4 and antiguedad >= 8:
        print(f"{nombre}, usted tiene derecho al subsidio de vivienda.")
    else:
        print(f"{nombre}, usted no tiene derecho a subsidio de vivienda.")

# Llamar a la función para iniciar el proceso
verificar_subsidio()

