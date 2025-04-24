## 1. Dado el arreglo [1,2,3,4,5,6]:


# Arreglo 1
arreglo = [1, 2, 3, 4, 5, 6]

## a) Iterar por todos los elementos dentro del arreglo utilizando while y mostrarlos en pantalla.
index = 0
while index < len(arreglo):
    print(arreglo[index])
    index += 1
    
## Iterar por todos los elementos dentro del arreglo utilizando el ciclo “for” y mostrarlos en pantalla.
for num in arreglo:
    print(num)
    
## Crear una copia del arreglo usando el ciclo “for” pero con todos los elementos incrementados en 1.
new_arreglo = []
for num in arreglo:
    new_arreglo.append(num + 1)

print(new_arreglo)

# Calcular el promedio de todos los elementos del arreglo
promedio = sum(arreglo) / len(arreglo)
print(f"El promedio es: {promedio}")

##-------------------------------------------------------------------------

##2. Función para extraer cadenas de una sola base
def cadenas_sola_base(adn_list):
    bases = ['A', 'T', 'C', 'G']
    for base in bases:
        print(f"Cadenas formadas solo por '{base}':")
        for cadena in adn_list:
            if all(letra == base for letra in cadena):
                print(cadena)

# Ejemplo de uso:
adn = ["AATGAAC", "GTTTTTC", "GGTAAA", "CCCCATGGG"]
cadenas_sola_base(adn)

##-------------------------------------------------------

##3. Función que retorna el número menor

def numero_menor(numeros):
    return min(numeros)

# Ejemplo
print(numero_menor([4, 1, 99, 3]))

##-----------------------------------------------

##4. Función que muestra los números primos

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def mostrar_primos(numeros):
    print("Números primos en el arreglo:")
    for num in numeros:
        if es_primo(num):
            print(num)

# Ejemplo
mostrar_primos([1, 2, 3, 4, 5, 6, 7, 10])

##-----------------------------------------------

##5. Función para nombres y edades de usuarios mayores de edad

def mayores_edad():
    n = int(input("¿Cuántos usuarios desea ingresar? "))
    mayores = []
    for _ in range(n):
        nombre = input("Ingrese nombre: ")
        edad = int(input("Ingrese edad: "))
        if edad >= 18:
            mayores.append(nombre)
    print("Usuarios mayores de edad:", mayores)
    print("Cantidad de mayores de edad:", len(mayores))
    return mayores

# Llamado de la función
mayores_edad()

##-----------------------------------------------

##6. Reasignar ciudades a sus departamentos correctos

# Ciudades mal clasificadas originalmente
valle = ["Cali", "Tulua", "Cartago", "Salento"]
quindio = ["Cordoba", "Armenia", "Palmira", "Circasia"]

# Clasificación real por departamento
ciudades_valle = ["Cali", "Tulua", "Palmira", "Cartago"]
ciudades_quindio = ["Armenia", "Salento", "Cordoba", "Circasia"]

# Listas definitivas
valle_def = []
quindio_def = []

# Recorremos todas las ciudades de ambas listas
for ciudad in valle + quindio:
    if ciudad in ciudades_valle:
        valle_def.append(ciudad)
    elif ciudad in ciudades_quindio:
        quindio_def.append(ciudad)
    else:
        print(f"Ciudad no clasificada: {ciudad}")

print("Valle:", valle_def)
print("Quindío:", quindio_def)


##------------------------------------------------------

##7. Reasignar ciudades a sus departamentos correctos

arreglo1 = ["Pera", "Cebolla", "Limón", "Pimentón"]
arreglo2 = ["Manzana", "Banano", "Lechuga", "Perejíl"]

frutas = []
verduras = []

for item in arreglo1 + arreglo2:
    if item in ["Pera", "Limón", "Manzana", "Banano"]:
        frutas.append(item)
    else:
        verduras.append(item)

print("Frutas:", frutas)
print("Verduras:", verduras)

##------------------------------------------------------

##8. Función que pide arreglo y devuelve el mayor

def numero_mayor():
    numeros = input("Introduce números separados por comas: ")
    lista = list(map(int, numeros.split(",")))
    return max(lista)

# Llamado
print("El número mayor es:", numero_mayor())

##------------------------------------------------------

##9. Función para comparar promedios

def comparar_promedios():
    arr1 = list(map(int, input("Ingrese el primer arreglo (números separados por comas): ").split(",")))
    arr2 = list(map(int, input("Ingrese el segundo arreglo (números separados por comas): ").split(",")))
    
    prom1 = sum(arr1) / len(arr1)
    prom2 = sum(arr2) / len(arr2)
    
    print("Promedio 1:", prom1)
    print("Promedio 2:", prom2)

    if prom1 > prom2:
        print("El primer arreglo tiene mayor promedio.")
    elif prom2 > prom1:
        print("El segundo arreglo tiene mayor promedio.")
    else:
        print("Ambos promedios son iguales.")

comparar_promedios()

##------------------------------------------------------

##10. Contar cuántas veces aparece la letra "c" en nombres

def contar_letra_c():
    nombres = input("Ingrese nombres separados por comas: ").split(",")
    contador = 0
    for nombre in nombres:
        contador += nombre.lower().count("c")
    if contador > 0:
        print(f"La letra 'c' se encuentra {contador} veces en los nombres.")
    else:
        print("La letra 'c' no se encuentra en los nombres.")

contar_letra_c()

##------------------------------------------------------

##11. Contar cuántos números impares hay en el arreglo

def contar_impares():
    numeros = list(map(int, input("Introduce números enteros positivos separados por comas: ").split(",")))
    impares = [num for num in numeros if num % 2 != 0]
    print("Cantidad de números impares:", len(impares))

# Llamado
contar_impares()

##------------------------------------------------------

##12. Cadena de ADN con más Timina ('T')

def adn_mas_timina():
    cadenas = input("Introduce cadenas de ADN separadas por comas: ").split(",")
    max_t = 0
    cadena_resultado = ""

    for cadena in cadenas:
        cantidad_t = cadena.upper().count("T")
        if cantidad_t > max_t:
            max_t = cantidad_t
            cadena_resultado = cadena

    print("Cadena con más Timina (T):", cadena_resultado)
    print("Cantidad de T:", max_t)

# Llamado
adn_mas_timina()

##------------------------------------------------------
##13. Versión simple del juego del ahorcado

import random

def ahorcado():
    palabras = ["python", "programa", "funcion", "variable", "computador"]
    palabra = random.choice(palabras)
    intentos = 6
    letras_adivinadas = []

    print("¡Bienvenido al juego del Ahorcado!")
    print("_ " * len(palabra))

    while intentos > 0:
        letra = input("Adivina una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya intentaste esa letra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            print("¡Bien! La letra está en la palabra.")
        else:
            print("Incorrecto.")
            intentos -= 1

        resultado = [l if l in letras_adivinadas else "_" for l in palabra]
        print(" ".join(resultado))

        if "_" not in resultado:
            print("¡Ganaste! La palabra era:", palabra)
            return

    print("Perdiste. La palabra era:", palabra)

# Llamado
ahorcado()

##------------------------------------------------------
##14. Ordenar un arreglo de números enteros no repetidos

def ordenar_enteros():
    numeros = list(map(int, input("Introduce números enteros no repetidos separados por comas: ").split(",")))
    numeros_ordenados = sorted(numeros)
    print("Arreglo ordenado:", numeros_ordenados)
    return numeros_ordenados

# Llamado
ordenar_enteros()

##------------------------------------------------------
##15. Ordenar alfabéticamente un arreglo de letras no repetidas

def ordenar_letras():
    letras = input("Introduce letras no repetidas separadas por comas: ").split(",")
    letras_ordenadas = sorted([l.strip().lower() for l in letras])
    print("Arreglo ordenado alfabéticamente:", letras_ordenadas)
    return letras_ordenadas

# Llamado
ordenar_letras()






















