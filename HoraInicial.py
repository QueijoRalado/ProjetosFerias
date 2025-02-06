"""""
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo.

Exemplo de Entrada 	           Exemplo de Saída
    16 2                    O JOGO DUROU 10 HORA(S)

    0 0                     O JOGO DUROU 24 HORA(S)

    2 16                    O JOGO DUROU 14 HORA(S)
"""""

valor_invalido=True

while valor_invalido==True:
    horario = (input("Escreva o horário em que o jogo começou (Exemplo: 12:30):\n" ))
    comeco_h = int(horario[0:2])
    comeco_m = int(horario[3:5])
    if comeco_h<0 or comeco_h>24 or comeco_m<0 or comeco_m>59:
        print("Valor inválido!")
    else:
        valor_invalido=False

valor_invalido=True

while valor_invalido==True:
    horario2 = (input("Escreva o horário em que o jogo terminou (Exemplo: 17:30):\n"))
    fim_h = int(horario2[0:2])
    fim_m = int(horario2[3:5])
    if fim_h<0 or fim_h>24 or fim_m<0 or fim_m>59:
        print("Valor inválido!")
    else:
        valor_invalido=False

horas = 0

if comeco_h>fim_h or fim_h>comeco_h:
    while comeco_h!=fim_h:
        comeco_h+=1
        horas+=1
        if comeco_h==24:
            comeco_h=0
else:
    horas = 24

minutos = 0

if comeco_m>fim_m or fim_m>comeco_m:
    while comeco_m!=fim_m:
        comeco_m+=1
        minutos+=1
        if comeco_m==60:
            comeco_m=0
else:
    minutos = 0
        
print(f"O tempo em que o jogo durou foi de: {horas} horas e {minutos} minutos!")
