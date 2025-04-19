# Diccionario para almacenar los registros de los usuarios
usuarios = {}

# Función para registrar un nuevo usuario
def registrar_usuario():
    # Recibir los datos del usuario
    documento = input("Ingrese el número de documento: ")
    nombres = input("Ingrese los nombres: ")
    apellidos = input("Ingrese los apellidos: ")
    edad = int(input("Ingrese la edad: "))
    peso = float(input("Ingrese el peso: "))
    estatura = float(input("Ingrese la estatura: "))

    # Guardar los datos del usuario en el diccionario
    usuarios[documento] = {
        "nombres": nombres,
        "apellidos": apellidos,
        "edad": edad,
        "peso": peso,
        "estatura": estatura
    }

    print("Registro exitoso")

# Función para consultar el registro de un usuario por su documento
def consultar_registro():
    documento = input("Ingrese el número de documento para consultar: ")
    
    # Verificar si el documento existe en el sistema
    if documento in usuarios:
        usuario = usuarios[documento]
        print("\nRegistro del usuario:")
        print(f"Documento: {documento}")
        print(f"Nombres: {usuario['nombres']}")
        print(f"Apellidos: {usuario['apellidos']}")
        print(f"Edad: {usuario['edad']} años")
        print(f"Peso: {usuario['peso']} kg")
        print(f"Estatura: {usuario['estatura']} m")
    else:
        print("No se encontró un registro con ese documento.")

# Menú de opciones
def menu():
    while True:
        print("\nSeleccione una opción:")
        print("1. Registrar nuevo usuario")
        print("2. Consultar registro de usuario")
        print("3. Salir")
        
        opcion = input("Ingrese el número de opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            consultar_registro()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el sistema
menu()
