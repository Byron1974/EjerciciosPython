# Función que verifica si la persona necesita usar guantes y gafas de protección
def verificar_proteccion():
    # Recibir el rol de la persona (ejecutivo u operario)
    rol = input("Ingrese el rol de la persona (ejecutivo u operario): ").lower()

    # Verificar si el rol es válido
    if rol != "ejecutivo" and rol != "operario":
        print("El rol ingresado no es válido. Por favor ingrese 'ejecutivo' o 'operario'.")
        return

    # Si el rol es 'operario', pedir la edad
    if rol == "operario":
        try:
            edad = int(input("Ingrese la edad de la persona: "))
            # Verificar si la edad es válida
            if edad <= 0:
                print("La edad ingresada no es válida.")
                return
        except ValueError:
            print("La edad ingresada no es un número válido.")
            return

    # Verificar si la persona debe usar guantes y gafas
    if rol == "operario" and edad > 60:
        print("La persona debe usar guantes y gafas de protección.")
    else:
        print("La persona no necesita usar guantes ni gafas de protección.")

# Llamar a la función para iniciar el proceso
verificar_proteccion()

