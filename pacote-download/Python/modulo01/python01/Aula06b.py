n = input('Digite algo: ')
print('O timpo primitivo do que foi digitado é: {}'.format(type(n)))
print('Ele é numérico? {}'.format(n.isnumeric()))           # Compara se é um numero, se sim envia a mensagem True
print('Ele é um texto? {}'.format(n.isalpha()))             # Compara se é Letra, se sim envia a mensagem True
print('Ele tem um texto ou numero? {}'.format(n.isalnum()))    # Compara se é Letra ou numero, se sim envia a mensagem True
print('Está tudo em maiúscula? {}'.format(n.isupper()))      # Compara se tudo está em letra maíuscola
print('Está dentro da tabela ASCII? {}'.format(n.isascii()))      # Compara se o n esta dentro da tabela ASCII
print('É somente espaços? {}'.format(n.isspace()))
