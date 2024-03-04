#MANIPULAÇÃO DE STRINGS 2

nome = 'JonI BiGude'

print(nome.upper()) # deixa as letras todas em maiúscula.
print(nome.lower()) # deixa as letras todas em minúsculas.
print(nome.title()) # formata para um padrão de título, com iniciais em maiúscula.

texto = '  Olá mundo!     ' # repare que existem espaços a mais inseridos no valor da variável.

print(texto)
print(texto.strip()) # remove os espaços em branco da variável.
print(texto.lstrip()) # remove os espaços em branco da esquerda.
print(texto.rstrip()) # remove os espaços em branco da direita .

# Junção e Centralização de String
menu = 'Python'

print('####'+ menu + '####') # forma mais errada e difícil de centralizar uma variável .
print(menu) # print somente da variável, sem os caracteres especiais.
print(menu.center(14)) # centraliza a variável no centro, são 14 caracteres ao todo, então esse comando centraliza a variável no centro desses 14 caracteres.(passo 1).
print(menu.center(14, '#')) # ao centralizar a variável, insere então o caractere desejadom nos lados que estão vazios. (passo 2).
print("-".join(menu)) # a cada letra da variável,insere um outro caractere entre os espaços das letras.