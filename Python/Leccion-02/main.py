#OPERADORES ARITMETICOS ------------------------->

operandoA = 3
operandoB = 2

suma = operandoA + operandoB

# print('Resultado:',suma)
# print(f'Resultado de la suma: {suma}')     #Forma literal para imprimir valores -> SIMILAR A TEMPLATE STRING EN JS

resta = operandoA - operandoB
# print(f'Resultado de la resta: {resta}')

multiplicacion = operandoA * operandoB
# print(f'Resultado de la multiplicacion: {multiplicacion}')

division = operandoA / operandoB
# print(f'Resultado de la division: {division}')

division = operandoA // operandoB       # Division para visualizar unicamente el valor entero
# print(f'Resultado de la division int: {division}')

modulo = operandoA % operandoB
# print(f'Resultado del modulo: {modulo}')

exponente = operandoA ** operandoB
# print(f'El resultado del exponente: {exponente}')

#EJERCICIO: Calcular el area y el perimetro de un rectangulo

# altura = int(input('Ingrese la altura del rectangulo: '))
# base = int(input('Ingrese la base del rectangulo: '))
# area = base * altura
# print(f'El area del rectangulo es: {area}')
# perimetro = (base + altura) * 2
# print(f'El perimetro del rectangulo es: {perimetro}')



# OPERADORES DE ASIGNACION ---------------------------------> 

miVariable = 10

# Incremento con reasignacion 

miVariable += 1

# Decremento con reasignacion

miVariable -= 1

# Multiplicacion con reasignacion

miVariable *= 3
# print(miVariable)

# Division con reasignacion

miVariable /= 2


# OPERADORES DE COMPARACION ----------------------------->

# Igual a...

a = 4
b = 2

resultado = a == b
# print(f'Resultado ==: {resultado}')

# Distinto de...

resultado = a != b
# print(f'Resultado !=: {resultado}')

# Mayor que...

resultado = a > b
# print(f'Resultado >: {resultado}')

# Menor que... 

resultado = a < b
# print(f'Resultado <: {resultado}')

# Mayor/menor o igual que...

resultado = a >= b
# print(f'Resultado >=: {resultado}')



# EJERCICIO: Par o impar

# num = int(input('Ingrese un número: '))

# if num % 2 == 0:
#     print(f'El número {num} es par.')
# else:
#     print(f'El número {num} es impar.')


# EJERCICIO: Mayoria de edad

# edad = int(input('Ingresa tu edad: '))
# adulto = 18
# if edad >= adulto:
#   print('Mayor de edad')
# else:
#   print('Menor de edad')


# OPERADORES LOGICOS ---------------------------->

# Operador AND (y)

a = True
b = False

# resultado = a and b
# print(resultado)

# Operador OR (o)

# resultado = a or b
# print(resultado)

# Operador NOT (not)

# resultado = not a       # Invierte el valor de la variable 'a'
# print(resultado)


# EJERCICIO: Valor dentro de rango entre 0 y 5 -> OPERADOR AND

# num = int(input('Ingrese un numero: '))

# if num >= 0 and num <= 5:
#   print(f'El numero {num} se encuentra dentro del rango')
# else:
#     print(f'El numero {num} se encuentra fuera del rango')



# EJERCICIO: OPERADOR OR

# vacaciones = True
# diaDescanso = False


# if vacaciones or diaDescanso: 
#     print('Puede asistir al juego')
# else:
#     print('No puede asistir al juego')
    

# EJERCICIO: OPERADOR NOT

# vacaciones = False
# diaDescanso = True

# if not (vacaciones or diaDescanso):
#     print('Puede asistir al juego')    
# else:
#     print('No puede asistir al juego')


# EJERCICIO: Rango entre 20's y 30's

# edad = int(input('Ingresá tu edad: '))

# if edad >= 20 and edad < 30:
#   print("Estás dentro de los 20's")
# elif edad > 29 and edad <= 39:
#     print("Estás dentro de los 30's")
# else: 
#     print('No estás dentro de los rangos requeridos')
    
# Simplificar operador and

# if (20 <= edad < 30):
#   print("Estás dentro de los 20's")
# elif (30 <= edad <= 39):
#     print("Estás dentro de los 30's")
# else: 
#     print('No estás dentro de los rangos requeridos')


# EJERCICIO: Numero mayor

# num1 = int(input('Ingrese el primer numero: '))
# num2 = int(input('Ingrese el segundo numero: '))

# if num1 > num2:
#     print(f'El número mayor es: {num1}')
# else:
#     print(f'El número mayor es: {num2}')


# EJERCICIO: Tienda de libros

# nombre = input('Ingrese el nombre del libro: ')
# id = int(input('Ingrese el ID del libro: '))
# precio = float(input('Ingrese el precio del libro: $ '))
# envioGratuito = input('Envio gratuito (True/False): ')

# if envioGratuito == 'True':
#     envioGratuito = True
# elif envioGratuito == 'False':
#     envioGratuito = False
# else:
#     envioGratuito = 'Valor Incorrecto. Debe escribir True o False'


# Forma estructurada para imprimir

# print(f'''
#       Nombre: {nombre}
#       Id: {id}
#       Precio: {precio}
#       Envío gratuito?: {envioGratuito}
#       ''')

