'''FAÇA UM PROGRAMA QUE LEIA O VALOR DO CATETO OPOSTO, DO CATETO ADJACENTE DE UM TRIÂNGULO RETÂNGULO, 
SOME-OS, E MOSTRE O VALOR DA HIPOTENUSA.
UM TRIÂNGULO RETÂNGULO, SOME-OS, E MOSTRE O VALOR DA HIPOTENUSA.'''

import math

cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

print('O valor da hipotenusa é de: {:.2f}.'.format(hipotenusa))