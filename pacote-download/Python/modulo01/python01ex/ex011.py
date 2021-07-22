# ------------------------- DESAFIO 011 -------------------------
# Programa para calcular a área de uma parede, e quantidade de latas de tinta, sabendo que uma lata pinta 2m².

larg = float(input('Largura da Parede: '))
alt = float(input('Altura da Parede: '))

area = larg * alt
tinta = area / 2

print('A area calculada é de {}m², e para pintar essa área serão necessárias {} latas de tinta!'.format(area, tinta))