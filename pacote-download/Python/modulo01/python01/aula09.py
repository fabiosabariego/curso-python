# ---------------------------------- MANIPULANDO CADEIAS DE CARACTERES ----------------------------------

# FATIAMENTO
# ANÁLISE

# ******* FUNÇÕES DE TRANSFORMAÇÕES
#fase.strip()  -> Utilizada para remover espaços inúteis no começo ou fim da frase
#fase.rstrip()  -> Remove somente espaços inúteis no fim da frase
#fase.lstrip()  -> Remove somente espaços inúteis no começo da frase


# ******* FUNÇÕES DE DIVISÃO DE STRING
#fase.split()  -> Divide cada palavra dentro de uma frase (Recebe uma indexação nova)


# ******* FUNÇÕES DE JUNÇÃO DE STRING
#'-'.join(frase)'  -> irá juntar a frase novamente, porém ao invés do espaço irá colocar o - entre as palavras.




# --------------------------------------- PRATICA ---------------------------------------

frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])         # No Python começamos a primeia palavra com 0, ou seja, na nossa frase irá mostrar o caractere "s".
print(frase[3:13])      # Neste caso vamos mostrar o caractere 3 até o 12, o 13 não aparece.
print(frase[:13])       # Neste caso ele mostratá os caracteres do 0 até o 12.
print(frase[1:15:2])    # O ultimo elemento colocado, significa que ele irá mostrar do 1 ao 14, pulando de 2 em 2 caracteres
print(frase[::2])       # Aqui não sabemos onde a string começa ou termina, assim ela irá do inicio até o final, pulando de 2 em 2 caracteres

print("""Texto muito grande Texto muito grande Texto muito grande Texto muito grande Texto muito grande 
Texto muito grande Texto muito grande Texto muito grande Texto muito grande Texto muito grande 
Texto muito grande Texto muito grande Texto muito grande Texto muito grande Texto muito grande 
Texto muito grande Texto muito grande Texto muito grande Texto muito grande Texto muito grande""")
# Acima temos a condição de, para não precisarmos de um print  em cada linha, usamos três aspas duplas """ para que textos grandes.

print(frase.count('o'))                 # Irá contar quantas vezes a letra "o" se repete dentro da frase escrita, no nosso caso 3. Lembrando que maiuscula e minuscula são diferentes.
print(frase.upper().count('O'))         # Irá colocar toda frase em maíusculo (comando upper), e contará quantas letras "O" existem, agora teremos 3 maiúsculas e 0 minúsculas
print(len(frase))                       # Irá mostrar qual a quantidade total de caracteres da frase. Teremos neste caso 27 caracteres
print(len(frase.strip()))               # Aqui ele remove todos os espaços no inicio e final da frase, deixando ela com 21 caracteres.
frase.replace('Python', 'Android')      # Nesta instância ele irá substituir Python por Android, porém não irá salvar
print(frase)
#frase = frase.replace('Python', 'Android')  # Aqui ele irá substituir e salvar a nova forma na frase, ou sejá, irá aparecer "Curso em Vídeo Android"
#print(frase)
print('Curso' in frase)                 # Verifica se existe a palavra curso dentro da frase, caso afirmativo irá retornar True, se não, False.
print('Banana' in frase)                # Verifica se existe a palavra curso dentro da frase, caso afirmativo irá retornar True, se não, False.
print(frase.find('Vídeo'))              # Procura se existe a palavra Curso dentro de frase, se sim retorna em qual posição ela inicia
print(frase.split())                    # Divide a Frase em varias strings (Cada palavra se tornará uma String.
print((frase.split())[0])               # Aqui ele pegará as palavras separadas e mostrará a palavra que estará no primeira área, ou seja, Curso
print((frase.split())[2])               # Aqui ele pegará as palavras separadas e mostrará a palavra que estará no terceira área, ou seja, Vídeo
print((frase.split())[2] [3])           # Aqui ele pegará as palavras separadas e mostrará somente a terceira letra, referente à Palavra Video, será a letra e (começa a contagem do 0)