# Desenvolva um programa que pergunte a distancia de uma viagem em km, calcule o preco da passagem cobrando
# R$0,50 / km para viagens ate 200km,e 0,45 para mais longas

dist = int(input('Diga a Distancia a percorrer em Km: '))

if dist <= 200:
    val = dist * 0.5
else:
    val = dist * 0.45
print('Valor da Passagem e de R${:.2f}'.format(val))
