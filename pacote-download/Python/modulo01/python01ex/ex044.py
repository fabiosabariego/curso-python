"""
Elabore um Programa que Calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento
- A vista (dinheiro ou cheque): 10% de desconto
- A vista no cartão: 5% de desconto
- Em até 2x no Cartão: Preço normal
- 3x ou mais no cartão: 20% de Juros
"""

prod = float(input('Qual Valor do Produto: R$ '))
pag = float(input("""========== FORMA DE PAGAMENTO ==========
(1) - Dinheiro / Cheque
(2) - Cartão
(3) - Em até 2x
(4) - Em 3x ou mais
Escolha a forma de pagamento: """))

if pag == 1:
    valfim = prod - (prod * 0.1)
    print('Desconto de 10% aplicado, o valor total a ser pago é R${:.2f}'.format(valfim))
elif pag == 2:
    valfim = prod - (prod * 0.05)
    print('Desconto de 5% aplicado, o valor total a ser pago é R${:.2f}'.format(valfim))
elif pag == 3:
    valfim = prod
    print('Não há descontos, o valor total a ser pago é R${:.2f}'.format(valfim))
elif pag == 4:
    valfim = (prod * 0.2) + prod
    print('Juros de 20% aplicado, o valor total a ser pago é R${:.2f}'.format(valfim))
else:
    print('Opção desejada não encontrada, tente novamente!')

