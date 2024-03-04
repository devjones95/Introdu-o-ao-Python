'''IMPORTANDO MÓDULOS - MATH 
(Esse módulo permite realizar cálulos matemáticos mais avançados.)'''

'''Exemplo 1:
import math == dessa forma, importamos todo o módulo math, com todas as suas ferramentas.

   Exemplo 2:
from  math import sqrt == aqui, importamos apenas a operação matemática desejada, nesse caso, a raiz quadrada (sqrt).'''

from math import sqrt # ao pé da letra: Do módulo math, importe sqrt(raiz quadrada).

num = int(input('Digite um número para obter sua raiz quadrada: '))
raiz = sqrt(num)
print('A raiz quadrada de {}, é igual a: {}.'.format(num, raiz))



