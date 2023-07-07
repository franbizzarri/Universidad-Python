class Cubo:
    def __init__(self, ancho, alto, profundidad):
      self.ancho = ancho
      self.alto = alto
      self.profundidad = profundidad
      
    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad

ancho = int(input('Ingresa el ancho del cubo: '))
alto = int(input('Ingresa el alto del cubo: '))
profundidad = int(input('Ingresa la profundidad del cubo: '))

cubo1 = Cubo(ancho, alto, profundidad)

print(f'El volumen del cubo es: {cubo1.calcular_volumen()}')