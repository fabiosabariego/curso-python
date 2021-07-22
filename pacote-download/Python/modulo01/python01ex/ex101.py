"""
Crie um programa que tenha uma função chamada voto que vai receber como parametro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO NOS CAMPOS
"""
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano

    if idade < 18:
        return f'Com {idade} anos: NÃO VOTA!!'
    elif 18 <= idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!!'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL!!'

resp = voto(int(input('Em que ano você nasceu: ')))
print(resp)