salario = float(input('Insira seu salário: '))
anos = int(input('Insira a quantidade de anos trabalhado por você dentro da ermpresa: '))

if anos > 5:
    print('Houve um aumento no seu salário, parabéns, você ganhou 5% de aumento.\n Seu novo salário será: {:.3f}.'.format(salario * 1.05))
else:
    print('Você não tem direito ao aumento de salário.')

