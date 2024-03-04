# CRIE UM ALGORITMO QUE LEIA UM NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA.

num = int(input('Digite um número inteiro: '))

'''Fazemos a operação dentro do próprio print() para sermos mais produtivos
e não precisando criar outra variável para o valor do dobro, triplo ou raiz quadrada.'''
print('O dobro de {} é: {}.'.format(num, num*2))
print('O triplo de {} é: {}.'.format(num, num*3))
print('A raiz quadrada de {} é: {}.'.format(num, num**0.5))
 