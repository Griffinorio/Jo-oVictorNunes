#Formas de imprimir na tela
'''nome = input(('Digite seu nome: '))

print('Olá, '+ nome + '!')
print('Olá,', nome,'!' )
print('Olá, %s!' % nome )
print('Olá, {}!'.format(nome))
print(f'Olá, {nome}!')'''

'''numeroUm = int(input("Digite um número inteiro: "))
numeroDois = float(input("Digite um número decimal: "))

print(numeroUm + numeroDois)'''

numeroUm = float(input("Digite um número: "))
numeroDois = float(input("Digite outro número: "))

print("A SOMA entre esses dois algarismos é de {}".format(numeroUm + numeroDois))
print("A SUBTRAÇÃO entre esses dois algarismos é de {}".format(numeroUm - numeroDois))
print("A MÚLTIPLICAÇÃO entre esses dois algarismos é de {}".format(numeroUm * numeroDois))
print("A DIVISÃO entre esses dois algarismos é de {:.2f}".format(numeroUm / numeroDois))