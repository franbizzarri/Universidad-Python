class Aritmetica:
    """
    Clase Aritmetica para realizar las operaciones de sumar, restar, etc.
    """
    def __init__(self, operandoA, operandoB):
      self.operandoA = operandoA
      self.operandoB = operandoB
    
    def sumar(self):
        return self.operandoA + self.operandoB
    def restar(self):
        return self.operandoA - self.operandoB
    def multiplicar(self):
        return self.operandoA * self.operandoB
    def dividir(self):
        return self.operandoA / self.operandoB
    
aritmetica1 = Aritmetica(5, 3)

print(f'Resultado de la suma: {aritmetica1.sumar()}')
print(f'Resultado de la resta: {aritmetica1.restar()}')
print(f'Resultado de la multiplicacion: {aritmetica1.multiplicar()}')
print(f'Resultado de la division: {aritmetica1.dividir():.2f}')
