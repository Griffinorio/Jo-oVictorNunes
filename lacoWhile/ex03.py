# TABUADA
'''num = int(input('Digite um número inteiro e descubra sua tabuada: '))

for cont in range(0, 11):
    print('{} X {:2} = {}'.format(num, cont, num * cont))'''
continuar = 'sim'
while continuar == 'sim':
    num = int(input('Digite um número inteiro e descubra sua tabuada: '))

    contador = 0

    while contador <= 10: 
        print('{} X {:2} = {:2}'.format(num, contador, contador * num)) 
        contador += 1

continuar = str(input('Deseja continuar?'))
if continuar == 'sim':
    while contador <= 10: 
        print('{} X {:2} = {:2}'.format(num, contador, contador * num)) 
        contador += 1
else:
    print('fim')


