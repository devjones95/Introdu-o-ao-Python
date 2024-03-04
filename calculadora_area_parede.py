'''CRIE UM PROGRAMA QUE LEIA A ALTURA E LARGURA DE UMA PAREDE, 
CALCULE SUA ÁREA E MOSTRE O QUANTO DE TINTA SERÁ NECESSÁRIO PRA PINTAR ESSA PAREDE, 
SABENDO QUE 1L DE TINTA PINTA 2M². (USE APENAS OS OPERADORES ARITMÉTICOS)'''

alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))

area = alt * lar
litros_tinta = area / 2

print('A área da parede é de {}, e será necessário {} litros de tinta para concluir o serviço.'.format(area, litros_tinta))