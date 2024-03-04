# DESENVOLVA UM PROGRAMA QUE LEIA 4 NOTAS DE UM ALUNO,CALCULE E MOSTRE SUA MÉDIA.
print()
print('Caro professor(a), bem vindo(a) á Calculadora de Média da Escola Python!')
print('==========================================')

nota1 = float(input('Digite a nota do 1º bimestre: '))
nota2 = float(input('Digite a nota do 2º bimestre: '))
nota3 = float(input('Digite a nota do 3º bimestre: '))
nota4 = float(input('Digite a nota do 4º bimestre: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print('A média do aluno(a) é de: ', media)

if media >= 7:
    print('Aluno(a) aprovado(a).')
    
else:
    print('Aluno(a) reprovado(a), favor encaminhá-lo(a) para as aulas de reforço.')