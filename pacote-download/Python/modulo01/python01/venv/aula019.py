"""
AULAS SOBRE DICIONÁRIO

dados = {}  ou dados = dict()
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])
print(dados['idade'])

Para inserir um novo item na lista, não precisamos utilizar por exemplo a função "append", basta fazer:
dados['sexo'] = 'M'
assim ficamos com: dados = {'nome':'Pedro', 'idade':25, 'sexo': 'M'}

del dados['idade']  -> Comando para remover "idade" da lista

Podemos também criar da seguinte forma:

print(dados.value())  -> Irá mostrar na tela todos os valores que estão na lista "dados", neste caso "Pedro, 25 e M".
print(dados.keys())   -> Neste caso ele irá mostrar a definição de dado, neste caso "nome, idade e sexo".
print(dados.items())  -> Neste caso pegará os dois acima, tanto a definição como os valores

Um exemplo usando com for:

for k, v in filme.items():  -> As letras "k" e "v" são relativas a "keys" e "values", devem ser colocadas nessa ordem
    print(f'A {k} é {v}'}   -> neste caso mostrará "A nome é Pedro


estado = dict()
brasil = list()

brasil.append(estado.copy())  --> Esta é a forma para se copiar um dicionário, a forma estado[:] não funciona

"""