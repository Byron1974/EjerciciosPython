# Función que recibe dos números y retorna el mayor de ellos
def obtener_mayor(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Llamar a la función con dos números y guardar el valor de retorno
mayor = obtener_mayor(6, 8)

# Imprimir el valor retornado por la función
print(f"El mayor número es: {mayor}")
