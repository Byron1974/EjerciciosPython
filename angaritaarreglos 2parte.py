##1. Imprimir el número de elementos de los siguientes arreglos

# a)
arreglo_a = [1,2,3,4,5,6,7,8,9,10]
print("a) Número de elementos:", len(arreglo_a))

# b)
arreglo_b = []
print("b) Número de elementos:", len(arreglo_b))

# c)
arreglo_c = ["a", True, -1]
print("c) Número de elementos:", len(arreglo_c))

# d)
arreglo_d = [2, 4, 5, 7, 1, 34, 89, 0]
print("d) Número de elementos:", len(arreglo_d))

##--------------------------------------------------------

##2. Agregar elementos a un arreglo y verificar

# Dado el arreglo
arreglo = [1,2,3,4,5,6,7,8,9,10]

# a) Agregar 345
arreglo.append(345)
print("Después de agregar 345:", arreglo)

# b) Agregar True
arreglo.append(True)
print("Después de agregar True:", arreglo)

# c) Agregar "ADSO"
arreglo.append("ADSO")
print("Después de agregar 'ADSO':", arreglo)

# d) Agregar 455, 78, False
arreglo.extend([455, 78, False])
print("Después de agregar 455, 78, False:", arreglo)

# e) Agregar "ABcd", True, 21
arreglo.extend(["ABcd", True, 21])
print("Después de agregar 'ABcd', True, 21:", arreglo)

##------------------------------------------------------

##3. Eliminar elementos en ciertos índices

# a) [1, 2, false]
arreglo1 = [1, 2, False]
del arreglo1[2]
print("a)", arreglo1)

# b) [99, false, 17, 45, 7, "abc", 78]
arreglo2 = [99, False, 17, 45, 7, "abc", 78]
del arreglo2[6]
print("b)", arreglo2)

# c) [-1, -55, -89- 30, 1000]
# Nota: hay un error en el arreglo original, asumo que es [-1, -55, -89, -30, 1000]
arreglo3 = [-1, -55, -89, -30, 1000]
del arreglo3[1]
print("c)", arreglo3)

# d) ["zxc", 767, 1298, true, false, [3], 1]
arreglo4 = ["zxc", 767, 1298, True, False, [3], 1]
del arreglo4[1:5]
print("d)", arreglo4)

# e) [34, ["q"], 67, 1, 99, 1/2]
arreglo5 = [34, ["q"], 67, 1, 99, 1/2]
del arreglo5[3:5]
print("e)", arreglo5)

##-----------------------------------------------

##6. Para recorrer el arreglo["x", "y", "z", 0, 1, 2, 3]usando un ciclo for e imprimir todos sus elementos
arreglo = ["x", "y", "z", 0, 1, 2, 3]
for elemento in arreglo:
    print(elemento)
    
##----------------------------------------------------------    
    
##7. Dado el siguiente arreglo [1, 17, 8, 9, 3] use ciclo  para recorrer el arreglo e imprimir todos sus elementos aumentados en 1

arreglo = [1, 17, 8, 9, 3]
for elemento in arreglo:
    print(elemento + 1)
    
##------------------------------------------------------
    
##8. Cree una función que reciba un arreglo y retorne su longitud(número de elementos)
    
def obtener_longitud(arreglo):
    return len(arreglo)

mi_arreglo = [10, 20, 30]
print(obtener_longitud(mi_arreglo))  # Salida: 3

##------------------------------------------------------

##9. Cree una función que reciba una letra del alfabeto y muestre si tal letra corresponde a algún elemento del siguiente arreglo ["a", "b", "c", "d", "e", "f", "g"] Use ciclo for en la solución de este problema

def verificar_letra(letra):
    arreglo_letras = ["a", "b", "c", "d", "e", "f", "g"]
    for elemento in arreglo_letras:
        if elemento == letra:
            print(f"La letra {letra} está en el arreglo.")
            return
    print(f"La letra {letra} no está en el arreglo.")

# Ejemplo de uso:
verificar_letra("c")  # La letra c está en el arreglo.
verificar_letra("z")  # La letra z no está en el arreglo.

    
   

    

    
    
    
    
