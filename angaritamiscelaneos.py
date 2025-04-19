## Imprimir los elementos de índice 2 y 4 del arreglo [200, -100, 45, 78, 32]

arreglo1 = [200, -100, 45, 78, 32]
print(arreglo1[2])  # Elemento en el índice 2
print(arreglo1[4])  # Elemento en el índice 4

##Imprimir los elementos "cd" y "gh" del arreglo ["ab", "cd", "ef", "gh"]

arreglo2 = ["ab", "cd", "ef", "gh"]
print(arreglo2[1])  # Elemento en el índice 1 ("cd")
print(arreglo2[3])  # Elemento en el índice 3 ("gh")

##Imprimir todos los elementos del arreglo [10, true, "k200", 20.7] usando un ciclo for

arreglo3 = [10, True, "k200", 20.7]
for elemento in arreglo3:
    print(elemento)

##Recorrer cada elemento del arreglo [17, 4, 64, 79, 109, 112] y imprimir los números impares
    arreglo4 = [17, 4, 64, 79, 109, 112]
for elemento in arreglo4:
    if elemento % 2 != 0:
        print(elemento)  # Imprimir solo los impares
        
  ##Cambiar el elemento de índice 2 por True y el de índice 3 por False en el arreglo [True, True, False, True, False]      
        
arreglo5 = [True, True, False, True, False]
arreglo5[2] = True  # Cambiar el elemento de índice 2
arreglo5[3] = False  # Cambiar el elemento de índice 3
print(arreglo5)

##Cambiar el elemento "jp" por True y el elemento "qr" por 30 en el arreglo ["wc", "jp", "zx", "qr"]

arreglo6 = ["wc", "jp", "zx", "qr"]
arreglo6[1] = True  # Cambiar "jp" por True
arreglo6[3] = 30  # Cambiar "qr" por 30
print(arreglo6)

##Función que reciba el arreglo [2, 5, 7, 9] y recorra e imprima cada uno de sus elementos

def recorrer_arreglo(arreglo):
    for elemento in arreglo:
        print(elemento)

arreglo7 = [2, 5, 7, 9]
recorrer_arreglo(arreglo7)

##Función que reciba un arreglo de n elementos y retorne el número de elementos del arreglo

def contar_elementos(arreglo):
    return len(arreglo)

arreglo8 = [2, 5, 7, 9]
print(contar_elementos(arreglo8))  # Retorna el número de elementos en el arreglo

##Usar index() para mostrar los índices de los elementos 44, 89, y 70 del arreglo [30, 44, 54, 89, 100]

arreglo9 = [30, 44, 54, 89, 100]

# Verificando si el elemento está en el arreglo antes de llamar a index
print(arreglo9.index(44) if 44 in arreglo9 else "No encontrado")  # Índice de 44
print(arreglo9.index(89) if 89 in arreglo9 else "No encontrado")  # Índice de 89
print(arreglo9.index(70) if 70 in arreglo9 else "No encontrado")  # Índice de 70 (no existe)












        
        
