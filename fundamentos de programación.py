#este proceso calcula el área de un triángulo
#defino base y altura
base: int
altura: int
resultado: float
#pido base y altura
base = int(input('Introduce base: '))
altura = int(input('Introduce altura: '))
#los multiplico y divido entre 2
resultado = base * altura / 2
#muestro resultado
print('El resultado es', resultado)