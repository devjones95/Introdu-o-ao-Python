# ESTRUTURAS CONDICIONAIS
print('Bem vindo(a) à Auto Escola Python, é um prazer ter você conosco.')
print()
maior_idade = 18
idade_epecial = 16

idade = int(input('Para iniciarmos o atendimento, informe sua idade: '))
if idade >= maior_idade:
    print('Você está apto(a) para tirar sua CNH, inicie o curso teórico e depois as aulas práticas.')
    
elif idade >= idade_epecial:
    print('Sua idade se enquadra na Idade especial, você pode iniciar o curso teórico de direção, mas não poderá fazer as aulas práticas.')
    
else:
    if idade < maior_idade:
        print('Desculpe, sua idade não é suficiente para tirar sua CNH.')        
