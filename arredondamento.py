'''CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL PELO TECLADO, 
E MOSTRE NA TELA, SUA FORMA ARREDONDADA PARA BAIXO E PARA CIMA.'''

import math # Poderia ser from math import floor , ceil.

num = float(input('Digite um número não inteiro: '))

print('Arredondando o número {} para cima, seria {}.'.format(num , math.ceil(num)))# math.ceil arredonda pra cima

print('Arredondando o número {} para baixo, seria {}.'.format(num, math.floor(num)))# math.floor arredonda pra baixo

