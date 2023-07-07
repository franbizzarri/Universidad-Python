class Rectangulo:
    def __init__(self, base, altura):
      self.base = base
      self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
       

base = int(input('Ingresa la base del rectangulo: '))
altura = int(input('Ingresa la altura del rectangulo: '))

rectangulo1 = Rectangulo(base, altura)

print(f'El área del rectangulo es: {rectangulo1.calcular_area()}')

