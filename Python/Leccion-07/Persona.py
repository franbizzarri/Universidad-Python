# CLASES Y OBJETOS ------------------------------------->

class Persona: 
    #pass       # La palabra reservada "pass" se utiliza para crear la clase o funcion y colocar el contenido luego.
    mi_atributo = ''
    
    def __init__(self):
      self.nombre = 'Franco'
      self.apellido = 'Bizzarri'
      self.edad = 30
      
persona1 = Persona()
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)