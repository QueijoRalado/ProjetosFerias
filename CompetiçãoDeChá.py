import random

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


