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

# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)

# resultado = factorial(5)

# print(f'El factorial de 5 es {resultado}')

# EJERCICIO: Imprimir numeros de forma descendente ---------------------------------->
"""
Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas.
Puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5, debe imprimir:
5
4
3
2
1

En caso de pasar el valor de 3, debe imprimir: 
3
2
1

Si se pasan valores negativos, no debe imprimir nada.
"""

# def descendente(num):
#     if num >= 1:
#         print(num)
#         descendente(num - 1)
#     elif num == 0:
#         return
#     elif num <= 0:
#         print('Valor Incorrecto') 
    

# descendente(5)
    
    
# EJERCICIO: Calculadora de impuestos --------------------------------------->
"""
Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado.
Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
"""

# def calculadora_impuestos(pago, imp):
#     total = pago + pago * (imp/100)
#     return total

# pago_sin_impuesto = float(input('Ingrese el monto del pago sin impuesto: '))
# impuesto = float(input('Ingrese el porcentaje del impuesto: '))


# total_a_pagar = calculadora_impuestos(pago_sin_impuesto, impuesto)

# print(f'El monto total a pagar es: {total_a_pagar}')
    

# EJERCICIO: Convertidor de temperaturas -------------------------------------->

"""
Realizar dos funciones para convertir de grados Celsius a Farenheit y viceversa
"""

# Funcion para convertir de Celsius a Farenheit
def cel_a_far(temp):
    return (temp * 9/5) + 32
    
# Funcion para convertir de Farenheit a Celsius
def far_a_cel(temp):
    return (temp - 32) * 5/9

celsius = int(input('Ingrese temperatura en Celsius para convertir a Farenheit: '))
temp_celsius = cel_a_far(celsius)
print(f'Resultado: {celsius}°C a Farenheit: {temp_celsius:.2f}°F')
farenheit = int(input('Ingrese temperatura en Farenheit para convertir a Celsius: '))       # PARA MOSTRAR UNICAMENTE DOS DECIMALES SE UTILIZA {nombre_variable:.2f}
temp_farenheit = far_a_cel(farenheit)
print(f'Resultado: {farenheit}°F a Celsius: {temp_farenheit:.2f}°C')

