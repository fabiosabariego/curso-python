"""
Crie um programa que leia dois valores e mostre um menu na tela:
1 - Somar
2 - Multiplicar
3 - maior
4 - novos Numeros
5 - Sair do Programa

Seu programa deverá realizar a opção solicitada em cada caso
"""
print('-=' *20)
num1 = float(input('Digite um Valor: '))
num2 = float(input('Digite outro Valor: '))
menu = 1
while 1 <= menu <= 4:
    menu = int(input("""\n========== MENU ==========
[1] Somar
[2] Multiplicar
[3] Maior Numero
[4] Novos Numeros
[5] Sair do Programa
Digite sua Opção: """))
    if menu == 1:
       print('\nOpção [1] - SOMA!!')
       print('{:.1f} + {:.1f} = {:.1f}\n'.format(num1, num2, num1 + num2))
    elif menu == 2:
        print('\nOpção [2] - Multiplicação!!')
        print('{:.1f} x {:.1f} = {:.1f}\n'.format(num1, num2, num1 * num2))
    elif menu == 3:
        if num1 > num2:
            print('\nO maior número é o {:.1f}'.format(num1))
        else:
            print(('\nO menor número é o {:.1f}'.format(num2)))
    elif menu == 4:
        print('\n')
        print('-=' *20)
        num1 = float(input('Digite um Valor: '))
        num2 = float(input('Digite outro Valor: '))
print('\nObrigado Por usar o Programa!!!')