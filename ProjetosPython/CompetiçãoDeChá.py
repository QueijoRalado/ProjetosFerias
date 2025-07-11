import random

"""""
Degustação de chá às escuras é a habilidade de identificar um chá usando apenas seus sentidos do olfato e paladar.

Isto faz parte da Competição Ideal de Consumidores de Chá Puro (da sigla em inglês ICPC), que um programa de TV local está organizando. Durante o show, um bule de chá completo é 
preparado e são entregues uma xícara de chá para cada um dos cinco competidores. Os participantes devem cheirar, saborear e avaliar a amostra, de modo a identificar o tipo de chá, 
que pode ser: (1) o chá branco; (2) chá verde; (3) chá preto; ou (4) chá de ervas. No final, as respostas são verificadas para determinar o número de suposições corretas.

Dado o tipo de chá real e as respostas fornecidas, determinar o número de participantes que receberam a resposta correta.

----- QueijoRalado falando, decidi colocar mais um tipo de chá porque sim
"""""

chás = {
    1: "Chá Branco",
    2: "Chá Verde",
    3: "Chá Preto",
    4: "Chá De Ervas",
    5: "Chá De Camomila"
}

c = 0
escolha = -1
n = random.randint(1, 5)
acertos = []
erros = []
jogadores = ["Jogador 1", "Jogador 2", "Jogador 3", "Jogador 4", "Jogador 5"]
cha_escolhido = chás[n]

print(n)
while c <= 4:
    escolha = -1
    while escolha<1 or escolha>5:
        escolha = int(input(f"{jogadores[c]}! Experimente o chá e nos diga, qual o tipo de chá que acabamos de te servir?\n")[0])
        if escolha<1 or escolha>5:
            print("Valor inválido, por favor, tente novamente")
        elif escolha==n:
            acertos.append(jogadores[c])
        else:
            erros.append(jogadores[c])
    c+=1
print("Muito bem! Depois de analisar as suas respostas, aqui estão os resultados!")
print(f"O chá escolhido era... {cha_escolhido}! Resposta número {n}!")
print(f"Os jogadores que acertaram foram: {acertos}")
print(f"Os jogadores que não acertaram foram: {erros}")


