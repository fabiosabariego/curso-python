# Escreva um programa que leia a velocidade de um carro, se ele passar de 80km/h mostre mensagem de multado
# A multa vai custar R$7 por km ultrapassado do limite

vel = int(input('Digite a Velocidade: '))
if vel > 80:
    mul = (vel - 80) * 7
    print('A Velocidade Limite de 80km/h foi ultrapassada em {}km/h, sua multa foi de R${:.2f}'.format(vel - 80, mul))
else:
    print('Tenha um bom dia, continue dirigindo com cautela!!')
