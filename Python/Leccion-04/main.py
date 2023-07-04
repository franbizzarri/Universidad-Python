# CICLO WHILE ------------------------------>

# condicion = True

# while condicion:
#   print('Ejecutando ciclo while')
# else:
#     print('Fin del ciclo while')

# contador = 0

# while contador < 3:
#     print(contador)
#     contador += 1;  #contador = contador + 1
# else:
#     print('Fin ciclo while')
    

# EJERCICIO: Imprimir numeros del 0 al 5 con un ciclo While

# contador = 0

# while contador < 6:
#     print(contador)
#     contador += 1
# else:
#     print('Fin ciclo while')

# EJERCICIO: Imprimir numeros descendentemente del 5 al 0 con un ciclo While

# contador = 5

# while contador >= 1:
#     print(contador)
#     contador -= 1



# CICLO FOR -------------------------->

# cadena = 'Hola'

# for letra in cadena:
#     print(letra)


# BREAK ------------------------------>

# for letra in 'Holanda':
#     if letra == 'a':
#         print(f'Letra encontrada: {letra}')
#         break


# CONTINUE --------------------------->

# for i in range(6):
#     if i % 2 == 0:   
#         print(f'Valor: {i}')

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')
    
