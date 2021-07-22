# ------------------------- DESAFIO 010 -------------------------
# Programa para ler quanto dinheiro ela tem, e quantos dolares pode comprar. Considerar US$1 = R$3,27

reais = float(input('Valor em Reais: R$'))
dol = reais / 3.27

print('Com R${:.2f}, você pode comprar US${:.2f}!'.format(reais, dol))
