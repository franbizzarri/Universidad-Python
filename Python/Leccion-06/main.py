# FUNCIONES: Se utiliza la palabra reservada def ------------------------------------>

# Funcion sin parametros ----------------------------------->
# def miFuncion():
#     print('Saludos desde mi funcion')

# miFuncion()


# Funcion con parametros ----------------------------------->
# def saludo(name, lastname):
#     print(f'¡Hola! Mi nombre es {name} {lastname}')

# saludo('Franco', 'Bizzarri')


# Palabra Return en funciones con Python ------------------------>
# def sumar(a, b):
#     return a + b

# print(f'El resultado de la suma es: {sumar(2, 4)}')

# Valores por defecto en una funcion ---------------------------->
# def suma(a = 2, b = 4):
#     return a + b

# print(f'El resultado de la suma es: {suma()}')
# print(f'El resultado de la suma con valores modificados es: {suma(5, 5)}')

# Argumentos variables en una funcion: (*) Se utiliza cuando no sabemos la cantidad de argumentos que recibira la funcion ---------------------------->

# def listarNombres(*nombres):
#     for nombre in nombres:
#         print(nombre)

# listarNombres('Franco', 'Sofia', 'Emma')
# listarNombres('Alicia', 'Ivo', 'Gaston', 'Cristian', 'Ivana')


'''
EJERCICIO: Crear una funcion para sumar los valores recibidos de tipo numerico,
utilizando argumentos variables *args como parametros de la funcion y regresar
como resultado la suma de todos los valores pasados como argumentos.
'''

# def sumarNumeros(*args):
#     resultado = 0
#     for numero in args:
#         resultado += numero
#     return resultado
    
# print(f'El resultado de la suma es: {sumarNumeros(3, 5, 10, 10, 15, 17)}')


'''
EJERCICIO: Crear una funcion para multiplicar los valores recibidos de tipo numerico, 
utilizando argumentos variables *args como parametro de la funcion y regresar como 
resultado la multiplicacion de todos los valores pasados como argumentos.
'''

# def multiplicarNumeros(*args):
#     resultado = 1
#     for numero in args:
#         resultado *= numero
#     return resultado

# print(f'El resultado de la multiplicacion es: {multiplicarNumeros(2, 4, 3, 2)}')


# ARGUMENTOS VARIABLES: key-value. Se utiliza para recibir un diccionario --------------------------------->

# def listarTerminos(**terminos):
#     for key, value in terminos.items():
#         print(f'{key}: {value}')
    
# listarTerminos(Nombre='Franco', Apellido='Bizzarri', Edad=30, Genero='Masculino')


# DISTINTOS TIPOS DE DATOS COMO ARGUMENTOS: La funcion recibe una lista ------------------------------->

# def desplegarNombres(nombres):
#     for nombre in nombres:
#         print(nombre)
        
# nombres = ['Franco', 'Sofia', 'Emma']

# desplegarNombres(nombres)
# desplegarNombres('Carlos')
# desplegarNombres((10, 11))


# FUNCIONES RECURSIVAS ------------------------------->

# FUNCION FACTORIAL ------------------------>

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

resultado = factorial(5)

print(f'El factorial de 5 es {resultado}')
