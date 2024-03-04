# CRIE UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER, E MOSTRE NA TELA O SENO, COSSENO E TANGENTE DESSE ÂNGULO.

import math
angle = float(input('Digite o ângulo desejado: '))
radian_angle = math.radians(angle) # Convertemos o ângulo escolhido para radianos, para podermos aplicar as funções trigonométricas.

# Calculando o Seno, Cosseno e Tangente do ângulo desejado:

seno = math.sin(radian_angle) # seno
cosseno = math.cos(radian_angle) # cosseno
tangente = math.tan(radian_angle) # tangente

# Printando os resultados na tela:

print('O valor do seno do ângulo {}, é {:.2f}.'.format(angle, seno))
print('O valor do cosseno do ângulo {}, é {:.2f}.'.format(angle, cosseno))
print('O valor da tangente do ângulo {}, é {:.2f}.'.format(angle, tangente))

