"""""
João fez uma pesquisa em seu site de busca predileto, e encontrou a resposta que estava procurando no terceiro link listado. Além disso, ele viu, pelo site, que t pessoas já haviam clicado neste link antes. João 
havia lido anteriormente, também na Internet, que o número de pessoas que clicam no segundo link listado é o dobro de número de pessoas que clicam no terceiro link listado. Nessa leitura, ele também descobriu que o 
número de pessoas que clicam no segundo link é a metade do número de pessoas que clicam no primeiro link.

João está intrigado para saber quantas pessoas clicaram no primeiro link da busca, e, como você é amigo dele, quer sua ajuda nesta tarefa.

------ QueijoRalado falando, João é burro
"""""
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
