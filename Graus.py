celsius = float(input('\033[1;36mDigite uma temperatura em graus celsius (°C):\033[m '))
print('\033[1;36mA temperatura {}°C convertidos em Fahrenheit(°F) será de:\033[m \033[1;31m{:.2f}°F\033['.format(celsius, celsius * 1.8 + 32))
