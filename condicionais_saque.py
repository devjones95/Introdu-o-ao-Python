# ESTRUTURAS CONDICIONAIS
'''if == se
   elif == senão se
   else == senão'''
   
print('Bem vindo(a) ao Python Bank!')
print('======================================')

saldo_bancario = 2000
saque = float(input('Informe o valor do saque: '))
if saldo_bancario >= saque:
    print('Realizando saque, aguarde...') 
    
else:
    print('Desculpe, saldo insuficiente para saque, deposite em sua conta para poder sacar a quantia desejada..')     
   