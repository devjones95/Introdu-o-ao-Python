'''OPERADORES ARITMÉTICOS AVANÇADOS.
( PRINTANDO VÁRIOS RESULTADOS EM UMA MESMA STRING, SEM FAZER VÁRIOS PRINTS.)'''

n1  = int(input('Digite um número: '))
n2 = int(input('Digite um outro número: '))
soma = n1+n2
sub = n1-n2
mult = n1*n2
div = n1/n2
resto_div = n1//n2
exponenciacao = n1**n2

# Agora vamos printar todas as operações em uma única linha de print:

print('A soma de {} e {} é de {}, a subtração é de {}, a multiplicação é de {}, a divisão é de {}, o resto inteiro é de {}, e a exponenciação é de {}.'.format(n1, n2, soma, sub, mult, div, resto_div, exponenciacao))

