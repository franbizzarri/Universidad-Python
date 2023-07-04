# ESTRUCTURAS DE CONTROL:

# if - else


# condicion = True

# if condicion:
#   print('Condicion Verdadera')
# else:
#   print('Condicion Falsa')
  
# if - elif - else  (if anidado)

# condicion = True

# if condicion == True:
#     print('Condicion Verdadera')
# elif condicion == False:
#     print('Condicion Falsa')
# else:
#     print('Condicion no reconocida')



# EJERCICIO: Conversion de Numero a Texto

# numero = int(input('Ingresa un valor entre 1 y 3: '))
# numeroTexto = ''

# if numero == 1:
#     numeroTexto = 'Número uno'
# elif numero == 2:
#     numeroTexto = 'Número dos'
# elif numero == 3:
#     numeroTexto = 'Número tres'
# else:
#     numeroTexto = 'Valor fuera de rango'
  
# print(f'''
#       Número ingresado: {numero}
#       Número a String: {numeroTexto}
#       ''')


# OPERADOR TERNARIO: Solo recomendado cuando el codigo es pequeño

# condicion = True

# if tradicional
# if condicion:
#     print('Condicion Verdadera')
# else:
#     print('Condicion Falsa')

#Operador Ternario

# print('Condicion Verdadera') if condicion else print('Condicion Falsa')

#EJERCICIO: Estacion segun mes del año

# mes = int(input('Ingresa el mes del año (1-12): '))
# estacion = None

'''if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Verano'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Otoño'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Invierno'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Primavera'''
    
# if simplificado

'''if mes == 12 or 1 <= mes <= 2:
    estacion = 'Verano'
elif 3 <= mes <= 5:
    estacion = 'Otoño'
elif 6 <= mes <= 8:
    estacion = 'Invierno'
elif 9 <= mes <= 11:
    estacion = 'Primavera'
else: 
    print('Mes ingresado inválido')

print(f'Para el mes {mes} la estacion es: {estacion}')'''

# EJERCICIO: Etapas de la vida segun la edad

'''
0-10: La infancia es increible...
10-20: Muchos cambios y mucho estudio...
20-30: Amor y comienza el trabajo...
Otro valor: Etapa de vida no reconocida
'''

'''
edad = int(input('Ingrese la edad: '))
etapa = None

if 0 <= edad < 10:
    etapa = 'La infancia es increíble...'    
elif 10 <= edad < 20:
    etapa = 'Muchos cambios y mucho estudio...'
elif 20 <= edad < 30:
    etapa = 'Amor y comienza el trabajo...'
else:
    etapa = 'Etapa de vida no reconocida.'

print(f'Tu edad es: {edad}, {etapa}')
'''

# EJERCICIO: Sistema de calificaciones
'''
Instrucciones: 
El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario proporcionara un valor entre 0 y 10.
- Si esta entre 9-10: imprimir una A
- Si esta entre 8 y menor a 9: imprimir una B
- Si esta entre 7 y menor a 8: imprimir una C
- Si esta entre 6 y menor a 7: imprimir una D
- Si esta entre 0 y menor a 6: imprimir una F
- Cualquier otro valor: imprimir "Valor incorrecto"
'''

num = float(input('Ingresa un valor: '))
nota = None

if 9 <= num <= 10:
    nota = 'A'
elif 8 <= num < 9:
    nota = 'B'    
elif 7 <= num < 8:
    nota = 'C'    
elif 6 <= num < 7:
    nota = 'D'    
elif 0 <= num < 6:
    nota = 'F'    
else:
    nota = 'Valor incorrecto'    

print(f'Tu calificacion es: {nota} ')

    
