# ------------------------- DESAFIO 014 -------------------------
#Programa para perguntar quantidade de km percorridos por um carro alugado
#e a quantidade de dias que foi alugado. Calcule o valor a pagar sendo R$60 por dia alugado e 0,15 por km rodado.

dia = float(input('Quantos dias Ficou com o carro? '))
km = float(input('Quantos KM rodou? '))

total = (dia * 60) + (km * 0.15)

print('Estando com o carro por {:.1f} dias, e rodando {:.1f}km, o valor total a ser pago é de R${}.'.format(dia, km, total))