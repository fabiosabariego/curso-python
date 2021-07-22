# Programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# Para Salarios sup a 1250,00 aumento de 10%, para inf ou igual aumento de 15%

sal = float(input('Digite o Salario R$: '))
if(sal > 1250.00):
    aum1 = (1250.00 * 0.10) + 1250.00
    print('Salario teve reajuste de 10%, tendo um valor de R${:.2f}' .format(aum1))
else:
    aum2 = (1250.00 * 0.15) + 1250.00
    print('Salario teve um reajuste de 15%, tendo um valor de R${:.2f}'.format(aum2))
