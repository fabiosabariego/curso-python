# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em qual posição ela aparece a primeira vez
# Qual posição ela aparece a ultima vez

frase = str(input('Digite uma Frase: ')).upper().strip()
print('A letra "A" aparece {} vezes!'.format(frase.count('A')))
print('Ela aparece a primeira vez na posição {}'.format(frase.find('A')+1))
print('Ela aparece a ultima vez na posição {}'.format(frase.rfind('A')+1))


