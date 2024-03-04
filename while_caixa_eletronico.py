'''OPERADORES DE REPETIÇÃO - WHILE
(CRIANDO UM SISTEMA BÁSICO DE CAIXA ELETRONICO.)'''
print('==============================================================')
print()
print('Bem vindo ao Python Bank, escolha uma das opções:')
opcao = -1 # Declaramos um valor fixo da variável, que seja diferente de todas as opções disponíveis, para evitar erros.

while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Depósito \n[3] Extrato \n[4] Sair \n')) # Lista de opções do caixa eletronico
    
    if opcao == 1:
        print('Realizando o saque, aguarde...')
        
    elif opcao == 2:
        print('Desosite o valor desejado no caixa.')
        
    elif opcao == 3:
        print('Carregando o extrato da conta, aguarde...')
        
    elif opcao == 4:
        print('Saindo...')
        
else:
    print('Opção inválida, escolha uma das opções.')