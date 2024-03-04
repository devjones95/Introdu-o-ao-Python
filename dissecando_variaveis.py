'''Faça um programa que leia algo no teclado, e mostre seu
tipo primitivo e todas as informações possíveis sobre ela.'''

a = input('Digite algo: ')
print('O tipo primitivo desse valor é: ',type(a))
print('Só tem espaços?: ',a.isspace())
print('É um número?: ',a.isnumeric())
print('É alfabético?: ',a.isalpha())
print('É alfanumérico?: ',a.isalnum())
print('Está somente com letras maiúsculas?: ',a.isupper())
print('Está somente com letras minúsculas?: ',a.islower())