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
      self.nombre = nombre
      self.apellido = apellido
      self.edad = edad
    
    def mostrarDetalle(self):
        print(f'Persona -> Nombre y apellido: {self.nombre} {self.apellido}, Edad: {self.edad}')


persona1 = Persona('Franco', 'Bizzarri', 30)
persona2 = Persona('Sofia', 'Perviu', 28)
persona3 = Persona('Emma', 'Bizzarri', 2)

persona1.mostrarDetalle()
persona2.mostrarDetalle()
persona3.mostrarDetalle()