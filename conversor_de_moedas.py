'''CRIE UM ALGORITMO QUE LEIA O QUANTO DE DINHEIRO A PESSOA TEM, 
E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR COM ESSE DINHEIRO. (U$ = 5,50).'''

print()
print('Bem vindo(a) ao Money Conversor.')
print()

money = float(input('Insira o valor em R$ a ser convertido: '))
dolar = money/5.50 # reais dividido pelo valor do dólar, no caso, U$ 5,50.
euro = money/7.20 # reais dividido pello valor do euro, no caso, EUR 7,20.

print('O valor de R${:.2f} em dólar equivale à U${:.2f} dólares.'.format(money, dolar))
print('O valor de R${:.2f} em euro equivale a EUR{:.2f} euros.'.format(money, euro))


