# # LISTAS EN PYTHON -------------------------->

# nombres = ['Juan', 'Karla', 'Ricardo', 'María']

# # Imprimir la lista de nombres
# print(nombres)

# # Acceder a los elementos de una lista
# print(nombres[0])
# print(nombres[1])
# print(nombres[2])
# print(nombres[3])

# # Acceder a los elementos de una lista de manera inversa
# print(nombres[-1])
# print(nombres[-2])
# print(nombres[-3])

# # Acceder a un rango de una lista
# print(nombres[0:2]) # Sin incluir el índice 2

# # Ir del inicio de la lista al índice sin incluirlo
# print(nombres[:3])

# # Recorrer la lista desde el índice indicado hasta el final
# print(nombres[1:])

# # Cambiar un valor de la lista
# nombres[3] = 'Franco'
# print(nombres)

# # Iterar nuestra lista

# for nombre in nombres:
#     print(nombre)
    
# # Preguntar el largo de una lista
# print(len(nombres))

# # Agregar nuevo elemento a la lista
# nombres.append('Emma')
# print(nombres)

# # Insertar un elemento en un índice en específico
# nombres.insert(3, 'Sofi')
# print(nombres)

# # Eliminar un elemento
# nombres.remove('Ricardo')
# print(nombres)

# # Eliminar el ultimo elemento de la lista
# nombres.pop()
# print(nombres)

# # Eliminar un indice especifico de la lista
# del nombres[1]
# print(nombres)

# # Limpiar la lista
# nombres.clear()
# print(nombres)

# Eliminar la lista por completo
# del nombres
# print(nombres)

# EJERCICIOS ---------------------------->

# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3

# for i in range(11):
#     if i % 3 == 0:
#         print(i)
# else:
#     print('Fin Ejercicio 1')
        
# # Ejercicio 2: Crear un rango de numeros de 2 a 6 e imprimirlos

# rango = range(2,7) # Se crea un rango con valor de inicio "2" y valor final de "6"
# for i in rango:
#     print(i)
# else:
#     print('Fin Ejercicio 2')
    

# # Ejercicio 3: Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1

# rango = range(3,11,2)   # El ultimo parametro indica el incremento, en este caso, se incrementa de 2 en 2

# for i in rango:
#     print(i)
# else:
#     print('Fin Ejercicio 3')
    

# TUPLAS EN PYTHON --------------------------------------->

''' Definir una tupla: A diferencia de una lista, las tuplas se definen con parentesis y no con corchetes.
    Si quisieramos definir una tupla con un solo elemento se debe incluir una coma (,) al final del elemento.
    Por ejemplo: nombres = ('Franco',)
'''

# frutas = ('Naranja', 'Banana', 'Manzana')
# print(frutas)

# Saber el largo de una tupla
# print(len(frutas))

# Acceder a un elemento
# print(frutas[1])

# Acceder a un elemento de manera inversa
# print(frutas[-1])

# Acceder a un rango
# print(frutas[0:2]) # Sin incluir el ultimo indice

# Recorrer los elementos de una tupla
# for fruta in frutas:
#     print(fruta, end=' ')   # ----> Se coloca el parametro end=' ' para que imprima en consola la tupla con un elemento al lado del otro y no con salto de linea

# # Cambiar el valor de una tupla: Debido a que una tupla es inmutable, se debe convertir una tupla en lista, modificar el elemento deseado y luego volver a convertir la lista en tupla
# frutasLista = list(frutas)  # Se convierte la tupla a lista con el metodo list()
# frutasLista[0] = 'Pera'
# frutas = tuple(frutasLista)     # Se convierte la lista de vuelta a tupla con el metodo tuple()
# print('\n', frutas)

# CABE DESTACAR QUE HACER ESTO NO SE CONSIDERA UNA BUENA PRACTICA PERO EN CASO DE NECESITARLO, SE PUEDE HACER.

# Eliminar una tupla
# del frutas
# print(frutas)


# EJERCICIO: Dada la siguiente tupla, crear una lista que solo incluya los numeros menores a 5

# tupla = (13, 1, 8, 3, 2, 5, 8)
# lista = []

# for i in tupla:
#     if i < 5:
#         lista.append(i)
        
# print(lista)
        

# SET en Python: Similar a una lista o tupla pero no mantiene un orden ni permite elementos duplicados. Al no tener un orden, no contiene indices.
# planetas = {'Marte', 'Júpiter', 'Venus'}   #Sintaxis Set: Se utilizan llaves
# print(planetas)

# Conocer el largo de un Set
# print(len(planetas))

# Revisar si un elemento esta en un Set
# print('Marte' in planetas)
# print('Tierra' in planetas)

# Agregar elementos a un Set: método add()
# planetas.add('Tierra')
# print(planetas)

# No permite elementos duplicados
# planetas.add('Tierra')
# print(planetas)

# Eliminar un elemento de un Set: remove()
# planetas.remove('Tierra')
# print(planetas)

# Otra forma de eliminar un elemento de un Set: discard()
# planetas.discard('Marte')
# print(planetas)

# Eliminar todos los elementos de un Set: clear()
# planetas.clear()
# print(planetas)

# Eliminar un Set
# del planetas
# print(planetas)


# DICCIONARIOS en Python: dict(key, value): Sintaxis similar a un objeto en JavaScript. Tampoco posee un orden y por lo tanto no contiene indices

diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}

print(diccionario)

# Largo del Diccionario (length)
print(len(diccionario))

# Acceder a un elemento (proporcionar key)
print(diccionario['OOP'])

# Otra forma de acceder a un elemento
print(diccionario.get('DBMS'))

# Modificar un elemento en un Diccionario
# diccionario['IDE'] = 'integrated development environment' # Minusculas
# print(diccionario['IDE'])

# Recorrer elementos de un Diccionario
for termino, value in diccionario.items():  # Se utiliza la funcion items() para poder recuperar los elementos y sus valores de un diccionario y visualizarlos
    print(termino, value)
    
for termino in diccionario.keys():  # Se utiliza la funcion keys() para recuperar unicamente las keys o propiedades de un diccionario
    print(termino)

for value in diccionario.values():  # Se utiliza la funcion values() para recuperar unicamente el valor de las keys de un diccionario
    print(value)

# Comprobar si ya existe un elemento en un diccionario
print('IDE' in diccionario)
print('ide' in diccionario)

# Agregar un elemento a un diccionario
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar un elemento de un diccionario
diccionario.pop('DBMS')
print(diccionario)

# Eliminar todos los elementos de un diccionario
diccionario.clear()
print(diccionario)

# Eliminar un diccionario
del diccionario
print(diccionario)



    
