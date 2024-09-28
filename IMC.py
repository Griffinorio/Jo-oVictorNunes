print("\033[36m-=\033[m" * 22)
print("            \033[1;35mCALCULADOR DE IMC\033[m")
print("\033[36m-=\033[m" * 22)

altura = float(input("Digite sua \033[1;32mALTURA\033[m: "))
peso = float(input("Agora, digite seu \033[1;33mPESO\033[m: "))

print("Seu \033[1;34mIMC (Índice de Massa Corporal)\033[m \ncom base nas suas informaçoes será de: \033[1;34m{:.2f}\033[m".format(peso / altura**2))

print("\033[36m-=\033[m" * 22)