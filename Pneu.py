import random

nada = "\n"
pressao_desejada = -1
while pressao_desejada<1 or pressao_desejada>40:
    pressao_desejada = int(input("Escreva a pressão desejada para o seu pneu (Minimo: 1, Máximo: 40):\n"))
    if pressao_desejada<1 or pressao_desejada>40:
        print("ERRO! Valor inválido!")
pressao_lida = random.randint(1, 40)
resultado = pressao_desejada-pressao_lida
print(f"A pressão desejada: {pressao_desejada}")
print(f"A pressão lida pela bomba: {pressao_lida}")
print(f"A diferença entre a pressão desejada e a pressão lida é de: {resultado}")