# Programa para ler o comprimento do cateto oposto e do cateto adjacente de um triangulo, e mostre o valor da hipotenusa

import math

ca = float(input('Cateto Adjacente: '))
co = float(input('Cateto Oposto: '))

hip = math.hypot(ca, co)

print('O valor da Hipotenusa para CA = {:.2f} e CO = {:.2f} é {:.2f}'.format(ca, co, hip))
