# ------------------------- DESAFIO 005 -------------------------
# Programa para mostrar na tela o sucessor e antecessor de um numero digitado

num = int(input('Digite um Numero: '))

suc = num + 1
ant = num - 1

print('Abaixo seguem os numeros conforme na ordem: \n Antecessor / Numedo Digitado / Sucessor \n {:^10} / {:^15} / {:^8}'.format(ant,num,suc))