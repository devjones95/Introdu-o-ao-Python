# MANIPULAÇÃO DE STRINGS

# Fatiamento

frase = ('Curso em Vídeo Python')

print(frase[1:10]) # Mostra do caractere 1 até o 10 primeiro número é o início, o segundo é o fim.

print(frase[:15]) # Mostra do início até o caractere 15, sendo que não temos o parâmetro de onde se inicia, então, sempre começará pelo caractere zero.

print(frase[2:]) # Monstra a partir do caractere 2 até o fim, já que não temos o parâmetro de fim, então será mostrado até o último caractere automaticamente.

print(frase[::2]) # Não temos os parâmetros de onde se inicia, nem onde é o fim, será mostrado do começo ao fim, porém pulando de 2 em 2 caracteres.

print (frase.count('o')) # .count conta os carateres que eu designar dentro do objeto. Pode ser qualquer tipo de caractere.

print (len(frase)) # .len conta quantos caracteres tem no objeto. lenth = comprimento.