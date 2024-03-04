# FAÇA UM PROGRAMA QUE MOSTRE O PREÇO DE UM PRODUTO COM 5% DE DESCONTO.

item = float(input('Digite o valor do produto: '))
desconto = item - (item * 5/100)

print('O preço do produto com desconto de 5% é de: {}'.format(desconto))
