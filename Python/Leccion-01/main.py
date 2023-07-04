# print("Hola Mundo con Python")  # La funcion print() imprime por pantalla lo que deseemos
 
# Enviar un saludo a consola con Python

# print('Este es mi saludo desde Python')


# VARIABLES EN PYTHON


miVariable = 'Hola desde Python'
# print(miVariable)

miNumero = 10
# print(miNumero)

miNumero = 5
# print(miNumero)

x = 10
y = 2
z = x + y

# print(x)
# print(y)
# print(z)


id(x) # La funcion id() apunta a la direccion de memoria donde se encuentra almacenada la variable

# print(id(x))
# print(id(y))
# print(id(z))


# Ejercicio declaracion de variables

miNombre = 'Franco Bizzarri'
miNumero = 2616525783
miMail = 'frann3112@gmail.com'

# print(miNombre)
# print(miNumero)
# print(miMail)

# Tipos de datos en Python

x =  10 # Numerico
# print(type(x)) # La funcion type() muestra el tipo de dato de la variable

x = 'Franco' # String

x = 10.5 # Float

x = True # Boolean -> Siempre hay que respetar la primera letra en mayusculas

# Concatenacion de Strings

miBandaFavorita = 'La Renga'
# print('Mi banda favorita es: ' + miBandaFavorita)
comentario = 'La mejor banda de Rock de Argentina'
# print('Mi banda favorita es:', miBandaFavorita+'.' ,comentario)

# Convertir Variables

numero1 = '1'
numero2 = '2'
# print('Concatenacion:', numero1 + numero2)

#CONVERSION A ENTERO CON LA FUNCION int()

# print(int(numero1) + int(numero2))


#TIPOS DE DATOS BOOLEANOS

miVariable = True
miVariable = 3 < 2      # Se puede declarar una condicion como una variable y dependiendo del resultado puede ser True o False
# print(miVariable)


# PROCESAR ENTRADA DEL USUARIO -> Funcion input()

# Funcion input()

# resultado = input('Escribe un mensaje: ')
# print('Mensaje:',resultado)
# print('Fin del programa.')

# num1 = int(input('Ingresa el primer numero: '))     #Se encierra la funcion input() en la funcion int() porque por defecto la funcion input() devuelve un string
# num2 = int(input('Ingresa el segundo numero: '))
# resultado = num1 + num2
# print('El resultado de la suma es:', resultado)

# EJERCICIO: Califica tu dia

# dia = int(input('¿Cómo estuvo tu día? Ingresa un número entre 1 y 10: '))

# print('Tuviste un día de:', dia)

# EJERCICIO: Informacion de un libro

# titulo = input('Proporciona el titulo del libro: ')
# autor = input('Proporciona el autor del libro: ')
# libro = print('El libro',titulo, 'fue escrito por', autor)






