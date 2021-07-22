"""
AULA SOBRE LISTAS

lanche.append('Seu Item') -> Serve para ADICIONAR um novo item. O novo item será adicionado à ultima posição
lanche.insert(0, 'Seu Item') -> Serve também para ADICIONAR um novo item, porém em uma posição definida. Nesse caso, se houver alguma coisa
    na posição 0, ela será deslocada para posição 1, e 'Seu Item' será adicionado à posição 0.

del lanche[3] -> Serve para DELETAR o item na posição 3
lanche.pop(3) -> Serve para DELETAR o item na posição 3
lanche.pop() -> Serve para DELETAR o Último item da lista
lanche.remove('Seu Item') -> Nesse caso ele deleta um item pelo nome, não pela posição. Ele removerá apenas o primeiro valor encontrado.
Nessa opção de deletar, após o item ser removido a lista será numerada. Por exemplo, tenho 5 itens, eu deletei o 3. Desta
    forma, o item 4 passa a ser o 3, e o item 5 passa a ser o 4.

valor = list(range(4, 11)) -> Nesse caso, "valores" receberá uma lista de 4 até 10, ficando: valores = ('4', '5', ... , '11')

valor = [8, 3, 5, 7, 9, 1] -> Os valores foram criados fora de ordem
valor.sort() -> Pegará os valores acima e os colocará na ordem crescente [1, 3, 5, 7, 8, 9]
valor.sort(reverse = True) -> Pegará os valores acima e os colocará na ordem decrescente [9, 8, 7, 5, 3, 1]

len(valor) -> É a quantidade total de elementos dentro, nesse caso serão 6 elementos.

for c, v in enumerate(valor) -> Nesse caso, o "c" dará a posição que o elemento está, e o "v" o valor dele
    Por exemplo, em [9, 2, 7], o primeiro item o "c" irá mostrar posição 0, e o "v" valor = 9

valores.append(int(input('Digite um Valor: ')) -> Nesse caso ele irá adiconar um item na lista

a = [1, 2, 3]
b = a  ->  Nesse caso o Python fará uma ligação entre a lista "b" e a lista "a", sendo assim, qualquer valor mudado na lista "b" também será mudado na lista "a".
b = a[:] -> Nesse caso o Python fará uma cópia de "a" para "b", assim qualquer valor mudado na lista "b" não será mudado na lista "a"

"""

