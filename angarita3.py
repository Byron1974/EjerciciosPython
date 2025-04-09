# Preguntar si el trabajador ha trabajado horas nocturnas
ha_trabajado_nocturnas = input("¿El trabajador ha trabajado horas nocturnas este mes? (sí/no): ").lower()

if ha_trabajado_nocturnas in ["sí", "si"]:
    # Solicitar el número de horas nocturnas trabajadas
    try:
        horas_nocturnas = int(input("Ingrese el número de horas nocturnas trabajadas: "))
        if horas_nocturnas > 0:
            # Calcular la bonificación
            bonificacion = horas_nocturnas * 2000
            print(f"Su bonificación este mes es de: {bonificacion} pesos")
        else:
            print("El número de horas trabajadas debe ser mayor a 0.")
    except ValueError:
        print("Por favor, ingrese un número válido de horas trabajadas.")
else:
    # Mensaje en caso de no trabajar horas nocturnas
    print("Usted no tiene derecho a bonificación este mes.")

    

