# Faça um Programa que leia um ângulo qualquer e mostre os valores de sen, cos e tan dele.

from math import radians, sin, cos, tan

ang = float(input('Digite o ângulo: '))

sen = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print('Para o ângulo {:.2f}°, temos: \n Sen = {:.2f} \n Cos = {:.2f} \n Tan = {:.2f}'.format(ang, sen, coss, tang))
