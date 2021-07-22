"""
Crie um pacote chamado utilidadesCeV que tenha 2 módulos internos chamados moeda e dado. Transfira as funções utilizadas
no ex110 para o primeiro pacote e mantenha tudo funcionando
"""

from ex111.utilidadesCeV import moeda

p = float(input('Digite o Preço: R$'))
moeda.resumo(p, 80, 35)