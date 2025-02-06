''''
Calibrar os pneus do carro deve ser uma tarefa cotidiana de todos os motoristas. Para isto, os postos de gasolina possuem uma bomba de ar. A maioria das bombas atuais são eletrônicas, permitindo que o motorista 
indique a pressão desejada num teclado. Ao ser ligada ao pneu, a bomba primeiro lê a pressão atual e calcula a diferença de pressão entre a desejada e a lida. Com esta diferença ela esvazia ou enche o pneu para
chegar na pressão correta.

Sua ajuda foi requisitada para desenvolver o programa da próxima bomba da SBC - Sistemas de Bombas Computadorizadas.

Escreva um programa que, dada a pressão desejada digitada pelo motorista e a pressão do pneu lida pela bomba, indica a diferença entre a pressão desejada e a pressão lida.

QueijoRalado falando, não tenho nada a falar
''''

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
