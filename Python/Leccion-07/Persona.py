# CLASES Y OBJETOS ------------------------------------->

# class Persona: 
#     #pass       # La palabra reservada "pass" se utiliza para crear la clase o funcion y colocar el contenido luego.
#     mi_atributo = ''
    
#     def __init__(self):
#       self.nombre = 'Franco'
#       self.apellido = 'Bizzarri'
#       self.edad = 30
      
# persona1 = Persona()
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)

# CREACION DE OBJETOS CON ARGUMENTOS ------------------------------->

# class Persona:
#     mi_atributo = ''

#     def __init__(self, nombre, apellido, edad):
#       self.nombre = nombre
#       self.apellido = apellido
#       self.edad = edad

# persona1 = Persona('Franco', 'Bizzarri', 30)
# persona2 = Persona('Sofia', 'Perviu', 28)
# persona3 = Persona('Emma', 'Bizzarri', 2)

# print(f'Persona 1 -> Nombre y apellido: {persona1.nombre} {persona1.apellido}, Edad: {persona1.edad}')
# print(f'Persona 2 -> Nombre y apellido: {persona2.nombre} {persona2.apellido}, Edad: {persona2.edad}')
# print(f'Persona 3 -> Nombre y apellido: {persona3.nombre} {persona3.apellido}, Edad: {persona3.edad}')

# persona1.nombre = 'Maximiliano' # SE MODIFICO EL ATRIBUTO NOMBRE 
# print(f'Persona 1 -> Nombre y apellido: {persona1.nombre} {persona1.apellido}, Edad: {persona1.edad}')


# AGREGAR METODOS A UNA CLASE ---------------------------------->

class Persona:
    mi_atributo = ''

    def __init__(self, nombre, apellido, edad):
      self._nombre = nombre
      self._apellido = apellido
      self._edad = edad
    
    def mostrarDetalle(self):
      print(f'Persona -> Nombre y apellido: {self.nombre} {self.apellido}, Edad: {self.edad}')
    
    @property
    def nombre(self):
      return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
      self._nombre = nombre

    @property
    def apellido(self):
      return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
      self._apellido = apellido
    
    @property
    def edad(self):
      return self._edad
    
    @edad.setter
    def edad(self, edad):
      self._edad = edad


persona1 = Persona('Franco', 'Bizzarri', 30)
persona2 = Persona('Sofia', 'Perviu', 28)
persona3 = Persona('Emma', 'Bizzarri', 2)


# persona1.mostrarDetalle()
# persona2.mostrarDetalle()
# persona3.mostrarDetalle()

# Persona.mostrarDetalle(persona1) # Otra forma de ejecutar un metodo de una clase aunque no es lo comun

# CREAR UN NUEVO ATRIBUTO A UN OBJETO

# persona1.telefono = '2616525783'

# print(f'Telefono - Persona 1: {persona1.telefono} ')

# METODO GET()

print(f'Nombre: {persona1.nombre}')

# METODO SET()

persona1.nombre = 'Maximiliano'
print(f'Nombre modificado: {persona1.nombre}')
