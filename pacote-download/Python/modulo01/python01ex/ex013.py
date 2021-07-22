# ------------------------- DESAFIO 013 -------------------------
# Programa para ler um salário, e mostrar o salário com 15% deu aumento

valor = float(input('Qual Salário: '))
sal = valor + (valor * 0.15)

print('O Salário de R${:.2f}, com 15% de aumento realizado ficará em R${:.2f}'.format(valor, sal))