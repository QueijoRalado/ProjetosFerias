valor_invalido=True
while valor_invalido==True:
    terceiro_link = float(input("Escreva o número de pessoas que clicaram no terceiro link (Minimo: 1 - Máximo: 1000)\n"))
    if terceiro_link<1 or terceiro_link>1000:
        print("Valor Inválido!")
    else:
        valor_invalido=False
segundo_link = terceiro_link*2
primeiro_link = segundo_link*2
print(f"O número de pessoas que clicaram no segundo link foi de: {segundo_link}!")
print(f"O número de pessoas que clicaram no primeiro link foi de: {primeiro_link}!")
