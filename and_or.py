# OPERADORES DE COMPARAÇÃO AND E OR

# Na condição and, TUDO deve ser True
print('Exemplo do AND:')
print(True and True) # True
print(True and False) # False
print(False and False) # False
print()
print('======================================')

# Na condição or, APENAS UM deve ser True
print('Exemplo do OR:')
print(True or True) # True
print(True or False) # False
print(False or False) # False

print('======================================')
print('Exemplo prático:')

saldo = 1000
saque = 250
limite = 200
conta_especial = True


exemplo = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print('Você tem saldo disponível para saque.')