# ------------------------- DESAFIO 006 -------------------------
# Criar um programa para mostrar o dobro, o triplo e a raiz quadrada de um nomedo digitado

num = int(input('Digite um Numero: '))

dob = num * 2
trip = num * 3
sqr = num ** (1/2)

print('Abaixo seguem os numeros conforme a ordem: \n Numero / Dobro / Triplo / Raiz Quadrada \n {:^6} / {:^5} / {:^6} / {:^13.2f}'.format(num, dob, trip, sqr))