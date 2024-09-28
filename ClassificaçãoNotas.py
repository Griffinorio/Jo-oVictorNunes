nota = int(input('Digite sua nota: '))

if nota >= 90: 
    print('A classificação da sua nota é: \033[1;32mA\033[m')
elif nota < 90 and nota >= 80: 
    print('A classificação da sua nota é: \033[1;33mB\033[m')
elif nota < 80 and nota >= 70:
    print('A classificação da sua nota é: \033[1;34mC\033[m')
elif nota < 70 and nota >= 60:
    print('A classificação da sua nota é: \033[1;35mD\033[m')
else:
    print('A classificação da sua nota é: \033[1;31mF\033[m')
