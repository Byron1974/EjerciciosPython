# a) Contar mayores de edad
edades = [20, 16, 19, 17, 20, 18, 22, 17]
mayores = 0
for i in edades:
    if i >= 18:
        mayores += 1
print(mayores)

# b) Promedio de datos
datos = [20, 33, 67, 4, 60]
contador = 0
suma = 0
while contador < len(datos):
    suma += datos[contador]
    contador += 1
print(suma / len(datos))

# Función para Shirley: elementos que se repiten

def elementos_repetidos(arr1, arr2):
    comunes = []
    for elem in arr1:
        if elem in arr2:
            comunes.append(elem + elem)
    return comunes

# Ejemplo
print(elementos_repetidos(["s", "w", "@", "3", "a", "p"], ["#", "p", "a", "z", "@"]))

# Función para Mariana: base más repetida

def base_mas_repetida():
    adn = input("Introduce 4 cadenas de ADN separadas por espacio: ").split()
    conteo = {"A": 0, "T": 0, "C": 0, "G": 0}
    for cadena in adn:
        for base in cadena:
            if base in conteo:
                conteo[base] += 1
    base_frecuente = max(conteo, key=conteo.get)
    print(f"La base más repetida es: {base_frecuente}")

# Función para Pedro: verificar si se puede formar 'orbi'

def formar_orbi(arreglo):
    palabra = "orbi"
    resultado = []
    for letra in palabra:
        if letra in arreglo:
            resultado.append(letra)
    if len(resultado) == len(palabra):
        resultado.sort()
        print(resultado)
    else:
        print("No se puede formar la palabra 'orbi'")

# Ejemplo
formar_orbi(["b", "p", "s", "z", "o", "b", "a", "w", "r", "i"])
