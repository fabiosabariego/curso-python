# ------------------------- DESAFIO 012 -------------------------
# Programa para ler um preço, e mostrar o seu preço com 5% de desconto

valor = float(input('Qual Valor: '))

desc = valor - (valor * 0.05)

print('O valor de R${:.2f}, com desconto de 5% ficará em R${:.2f}'.format(valor, desc))