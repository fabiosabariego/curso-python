"""
Dentro do pacote utilidadesCeV que criamos no ex111 temos um modulo chamado dado. Crie uma Função chamada
leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar
apenas valores que sejam monetários
"""

from ex112.utilidadesCeV import moeda
from ex112.utilidadesCeV import dado

p = dado.leiaDinheiro('Digite o Preço: R$')
moeda.resumo(p, 80, 35)