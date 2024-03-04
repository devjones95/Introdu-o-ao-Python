# CRIE UM PROGRAMA QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO, E DEPOIS MOSTRE O SALÁRIO COM 15% DE AUMENTO.

salario = float(input('Digite o salário a receber 15% de aumento: '))

novo_salario = salario + (15 * salario / 100)

print('O salario de {} com o aumento de 15%, passou a ser {:.2f}.'.format(salario, novo_salario))
