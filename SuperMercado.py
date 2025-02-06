nada = "\n"
carrinho = []
valor_compras = 0
n_produtos = 0

#for produto, preco in congelados_açougue.items():
        #    print(f"{produto} - R$ {preco}")
        #ISSO AQUI EM CIMA PRINTA O VALOR E A CHAVE DOS DICIONÁRIOS, IMPORTANTE

# ------------------------------------------------------------- SETOR ALIMENTÍCIO -------------------------------------------------------------
congelados_açougue = {
    "Peito de Frango c/ Osso (KG)": 22.20,
    "Peito de Frango sem Osso (KG)": 24.20,
    "Picanha (KG)": 59.99,
    "Contra-Filé (KG)": 39.90,
    "Costela (KG)": 19.89
}

tudo_açougue = list(congelados_açougue.items())
produtos_açougue = list(congelados_açougue.keys())
precos_açougue = list(congelados_açougue.values())

laticinios = {
    "Yogurte de Morango (1L, Unidade)": 22.0,
    "Margarina com Sal (500g, Unidade)": 8.0,
    "Requeijão Cremoso (420g, Unidade)": 16.59,
    "Chamyro (450g, 6 Unidades)": 7.59,
    "Sorvete Napolitano (1,5L, Unidade)": 36.90
}

tudo_laticinios = list(laticinios.items())
produtos_laticinios = list(laticinios.keys())
precos_laticinios = list(laticinios.values())

padaria = {
    "Pão de Forma Integral (500g, Pacote)": 8.09,
    "Leite Integral (1L, Caixa)": 5.99,
    "Biscoito de Polvilho (200g, Pacote)": 7.69,
    "Clube Sacial (288g, Pacote)": 11.09,
    "Cereal Socrilhos (690g, Pacote)": 17.90
}

tudo_padaria = list(padaria.items())
produtos_padaria = list(padaria.keys())
precos_padaria = list(padaria.values())

mercearia = {
    "Molho de Tomate (300g, Pacote)": 2.99,
    "Macarrão (500g, Pacote)": 4.59,
    "Arroz (5KG, Pacote)": 27.69,
    "Feijão (1KG, Pacote)": 22.59,
    "Kola Koca (2L, Garrafa)": 10.99
}

tudo_mercearia = list(mercearia.items())
produtos_mercearia = list(mercearia.keys())
precos_mercearia = list(mercearia.values())

# ------------------------------------------------------------- SETOR DO ESTILO -------------------------------------------------------------
camisetas = {
    "Tech T-Shirt Outsider": 153.99,
    "Camiseta Básica": 109.00,
    "Camiseta Xadrez": 119.00,
    "Camiseta Regata": 89.00,
    "Camiseta Oversized": 111.00
}

tudo_camisetas = list(camisetas.items())
produtos_camisetas = list(camisetas.keys())
precos_camisetas = list(camisetas.values())

sapatos = {
    "Tênis Dadidas Response": 340.99,
    "Tênis Nika Low Court": 429.59,
    "Tênis Nika Air Force": 527.49,
    "Tênis Mizano": 1127.69,
    "Tênis Vens": 310.99
}

tudo_sapatos = list(sapatos.items())
produtos_sapatos = list(sapatos.keys())
precos_sapatos = list(sapatos.values())

calcas = {
    "Calça Jeans": 65.90,
    "Calça Tática Militar": 149.59,
    "Calça Slim Algodão": 59.39,
    "Calça Baggy": 203.19,
    "Calça Confort": 94.99
}

tudo_calcas = list(calcas.items())
produtos_calcas = list(calcas.keys())
precos_calcas = list(calcas.values())

shorts = {
    "Bermuda Comum": 27.15,
    "Bermuda Moletom": 59.19,
    "Short Calção": 25.49,
    "Short Samba Canção": 35.79,
    "Bermuda Esportiva": 29.99
}

tudo_shorts = list(shorts.items())
produtos_shorts = list(shorts.keys())
precos_shorts = list(shorts.values())

bolsa_acessorio = {
    "Boné Com Aba Dadidas": 34.99,
    "Garrafa Dadidas 750ML": 24.59,
    "Pochete Dadidas": 36.99,
    "Shoulder Bag Reforçada": 66.40,
    "Mochila de Viagem": 100.89
}

tudo_bolsa_acessorio = list(bolsa_acessorio.items())
produtos_bolsa_acessorio = list(bolsa_acessorio.keys())
precos_bolsa_acessorio = list(bolsa_acessorio.values())

# ------------------------------------------------------------- SETOR DOS ELETRODOMÉSTICOS -------------------------------------------------------------

cozinha = {
    "Fogão Eletrolix 5 Bocas ": 1221.00,
    "Microondas 110 Volts Eletrolix": 699.99,
    "Geladeira Brastamp 3 Portas": 4299.00,
    "Freezer Degalo 1 Porta": 2399.00
}

tudo_cozinha = list(cozinha.items())
produtos_cozinha = list(cozinha.keys())
precos_cozinha  = list(cozinha.values())

ventilação = {
    "Ventilador de Mesa Britanha ": 179.90,
    "Climatizador Portátil Ventisal": 535.90,
    "Ar Condicionado Portátil FOS": 2199.00,
    "Freezer Degalo 1 Porta": 2399.00
}

tudo_cozinha = list(cozinha.items())
produtos_cozinha = list(cozinha.keys())
precos_cozinha  = list(cozinha.values())


# ------------------------------------------------------------- SETOR DOS CUIDADOS PESSOAIS -------------------------------------------------------------

class super_mercado():
    def __init__(self):
        self.menu()
    def menu(self):
        escolha = -1
        while escolha <1 or escolha>5:
            print("( 1 ) - Alimentos")
            print("( 2 ) - Roupas")
            print("( 3 ) - Eletrodomésticos")
            print("( 4 ) - Cuidados Pessoais\n")
            print("( 5 ) - Finalizar a Compra")
            escolha = int(input("---------------------------------------------\nBem vindo(a) ao Super Mercado Nuvelu! Oque deseja comprar?\n---------------------------------------------\n"))
            if escolha <1 or escolha>5:
                print(f"'{escolha}' não é um valor válido, por favor, tente novamente (PS: Escolha conforme os números na esquerda!)")
                print("-"*40)
            elif escolha==1:
                self.alimentos()
            elif escolha==2:
                self.roupas()
            elif escolha==3:
                self.eletro()
            elif escolha==4:
                self.cuidados()
            elif escolha==5:
                self.finalizar()
    def alimentos(self):
        escolha = -1
        print("-"*40)
        while escolha <1 or escolha>5:
            print("SETOR ALIMENTÍCIO")
            print("( 1 ) - Congelados do Açougue")
            print("( 2 ) - Laticínios")
            print("( 3 ) - Padaria")
            print("( 4 ) - Mercearia\n")
            print("( 5 ) - Voltar ao Menu Principal")

            escolha = int(input("----------------------------------------\nQue parte do setor alimentício deseja dar uma olhada?\n----------------------------------------\n"))
            if escolha <1 or escolha>5:
                print(f"'{escolha}' não é um valor válido, por favor, tente novamente (PS: Escolha conforme os números na esquerda!)")
                print("-"*40)
            elif escolha==1:
                self.congelados_acougue()
            elif escolha==2:
                self.laticinios()
            elif escolha==3:
                self.padaria()
            elif escolha==4:
                self.mercearia()
            elif escolha==5:
                self.menu()
    def roupas(self):
        escolha = -1
        print("-"*40)
        while escolha <1 or escolha>6:
            print("SETOR DO ESTILO")
            print("( 1 ) - Camisetas")
            print("( 2 ) - Sapatos")
            print("( 3 ) - Calças")
            print("( 4 ) - Shorts")
            print("( 5 ) - Acessórios\n")
            print("( 6 ) - Voltar ao Menu Principal")

            escolha = int(input("----------------------------------------\nQue parte do setor alimentício deseja dar uma olhada?\n----------------------------------------\n"))
            if escolha <1 or escolha>6:
                print(f"'{escolha}' não é um valor válido, por favor, tente novamente (PS: Escolha conforme os números na esquerda!)")
                print("-"*40)
            elif escolha==1:
                self.camisetas()
            elif escolha==2:
                self.sapatos()
            elif escolha==3:
                self.calças()
            elif escolha==4:
                self.shorts()
            elif escolha==5:
                self.bolsas_acessorios()
            elif escolha==6:
                self.menu()
    def eletro(self):
        print("receba")
    def cuidados(self):
        print("giggity giggity")
    def finalizar(self):
        print("que show da xuxa é esse hein kkkk nossa senhora se mate")

    # --------------------------------------------------- ALTERNATIVAS DENTRO DOS SETORES ---------------------------------------------------

    # ALIMENTICIO: --------------------------------------------------------------------------------------------------------------------------

    def congelados_acougue(self):
        global valor_compras
        global carrinho
        global n_produtos
        escolha=-1
        print("-"*40)
        while escolha!=6:
            print("SETOR DOS CONGELADOS DO AÇOUGUE")
            n = 0
            for produto, preco in congelados_açougue.items():
                n+=1
                print(f"( {n} ) - {produto} - R$ {preco:.2f}")
            print(f"\n( {n+1} ) - Voltar ao Setor Alimentício")
            escolha = int(input("\nEscolha o item desejado: \n"))
            print("-"*40)
            if escolha==6:
                self.alimentos()
            elif escolha>6 or escolha<1:
                print(f"'{escolha}' não é um valor válido, por favor, tente novamente (PS: Escolha conforme os números na esquerda!)")
                print("-"*30)
            else:
                print (f"{produtos_açougue[escolha-1]} adicionado ao carrinho!")
                valor_compras = valor_compras + precos_açougue[escolha-1]
                print (f"Valor total do carrinho: {valor_compras:.2f}")
                carrinho.append(tudo_açougue[escolha-1])
                print ("Produtos atuais no carrinho:")
                n_produtos=0
                for produto in carrinho:
                    n_produtos+=1
                    print(f"[ {n_produtos} ] {produto}")
                print("-"*40)

    def laticinios(self):
        global valor_compras
        global carrinho
        global n_produtos
        escolha=-1
        print("-"*40)
        while escolha!=6:
            print("SETOR DOS LATICÍNIOS")
            n = 0
            for produto, preco in laticinios.items():
                n+=1
                print(f"( {n} ) - {produto} - R$ {preco:.2f}")
            print(f"\n( {n+1} ) - Voltar ao Setor Alimentício")
            escolha = int(input("\nEscolha o item desejado: \n"))
            print("-"*40)
            if escolha==6:
                self.alimentos()
            elif escolha>6 or escolha<1:
                print(f"'{escolha}' não é um valor válido, por favor, tente novamente (PS: Escolha conforme os números na esquerda!)")
                print("-"*30)
            else:
                print (f"{produtos_laticinios[escolha-1]} adicionado ao carrinho!")
                valor_compras = valor_compras + precos_laticinios[escolha-1]
                print (f"Valor total do carrinho: {valor_compras:.2f}")
                carrinho.append(tudo_laticinios[escolha-1])
                print ("Produtos atuais no carrinho:")
                n_produtos=0
                for produto in carrinho:
                    n_produtos+=1
                    print(f"[ {n_produtos} ] {produto}")
                print("-"*40)

    def padaria(self):
        global valor_compras
        global carrinho
        global n_produtos
        escolha=-1
        print("-"*40)
        while escolha!=6:
            print("SETOR DA PADARIA")
            n = 0
            for produto, preco in padaria.items():
                n+=1
                print(f"( {n} ) - {produto} - R$ {preco:.2f}")
            print(f"\n( {n+1} ) - Voltar ao Setor Alimentício")
            escolha = int(input("\nEscolha o item desejado: \n"))
            print("-"*40)
            if escolha==6:
                self.alimentos()
            elif escolha>6 or escolha<1:
                print(f"'{escolha}' não é um valor válido, por favor, tente novamente (PS: Escolha conforme os números na esquerda!)")
                print("-"*30)
            else:
                print (f"{produtos_padaria[escolha-1]} adicionado ao carrinho!")
                valor_compras = valor_compras + precos_padaria[escolha-1]
                print (f"Valor total do carrinho: {valor_compras:.2f}")
                carrinho.append(tudo_padaria[escolha-1])
                print ("Produtos atuais no carrinho:")
                n_produtos=0
                for produto in carrinho:
                    n_produtos+=1
                    print(f"[ {n_produtos} ] {produto}")
                print("-"*40)

    def mercearia(self):
        global valor_compras
        global carrinho
        global n_produtos
        escolha=-1
        print("-"*40)
        while escolha!=6:
            print("SETOR DA MERCEARIA")
            n = 0
            for produto, preco in mercearia.items():
                n+=1
                print(f"( {n} ) - {produto} - R$ {preco:.2f}")
            print(f"\n( {n+1} ) - Voltar ao Setor Alimentício")
            escolha = int(input("\nEscolha o item desejado: \n"))
            print("-"*40)
            if escolha==6:
                self.alimentos()
            elif escolha>6 or escolha<1:
                print(f"'{escolha}' não é um valor válido, por favor, tente novamente (PS: Escolha conforme os números na esquerda!)")
                print("-"*30)
            else:
                print (f"{produtos_mercearia[escolha-1]} adicionado ao carrinho!")
                valor_compras = valor_compras + precos_mercearia[escolha-1]
                print (f"Valor total do carrinho: {valor_compras:.2f}")
                carrinho.append(tudo_mercearia[escolha-1])
                print ("Produtos atuais no carrinho:")
                n_produtos=0
                for produto in carrinho:
                    n_produtos+=1
                    print(f"[ {n_produtos} ] {produto}")
                print("-"*40)

    # ESTILO: --------------------------------------------------------------------------------------------------------------------------

    def camisetas(self):
        global valor_compras
        global carrinho
        global n_produtos
        escolha=-1
        print("-"*40)
        while escolha!=6:
            print("SETOR DO ESTILO")
            n = 0
            for produto, preco in camisetas.items():
                n+=1
                print(f"( {n} ) - {produto} - R$ {preco:.2f}")
            print(f"\n( {n+1} ) - Voltar ao Setor do Estilo")
            escolha = int(input("\nEscolha o item desejado: \n"))
            print("-"*40)
            if escolha==6:
                self.roupas()
            elif escolha>6 or escolha<1:
                print(f"'{escolha}' não é um valor válido, por favor, tente novamente (PS: Escolha conforme os números na esquerda!)")
                print("-"*30)
            else:
                print (f"{produtos_camisetas[escolha-1]} adicionado ao carrinho!")
                valor_compras = valor_compras + precos_camisetas[escolha-1]
                print (f"Valor total do carrinho: {valor_compras:.2f}")
                carrinho.append(tudo_camisetas[escolha-1])
                print ("Produtos atuais no carrinho:")
                n_produtos=0
                for produto in carrinho:
                    n_produtos+=1
                    print(f"[ {n_produtos} ] {produto}")
                print("-"*40)
    
    def sapatos(self):
        global valor_compras
        global carrinho
        global n_produtos
        escolha=-1
        print("-"*40)
        while escolha!=6:
            print("SETOR DO ESTILO")
            n = 0
            for produto, preco in sapatos.items():
                n+=1
                print(f"( {n} ) - {produto} - R$ {preco:.2f}")
            print(f"\n( {n+1} ) - Voltar ao Setor do Estilo")
            escolha = int(input("\nEscolha o item desejado: \n"))
            print("-"*40)
            if escolha==6:
                self.roupas()
            elif escolha>6 or escolha<1:
                print(f"'{escolha}' não é um valor válido, por favor, tente novamente (PS: Escolha conforme os números na esquerda!)")
                print("-"*30)
            else:
                print (f"{produtos_sapatos[escolha-1]} adicionado ao carrinho!")
                valor_compras = valor_compras + precos_sapatos[escolha-1]
                print (f"Valor total do carrinho: {valor_compras:.2f}")
                carrinho.append(tudo_sapatos[escolha-1])
                print ("Produtos atuais no carrinho:")
                n_produtos=0
                for produto in carrinho:
                    n_produtos+=1
                    print(f"[ {n_produtos} ] {produto}")
                print("-"*40)

    def calças(self):
        global valor_compras
        global carrinho
        global n_produtos
        escolha=-1
        print("-"*40)
        while escolha!=6:
            print("SETOR DO ESTILO")
            n = 0
            for produto, preco in calcas.items():
                n+=1
                print(f"( {n} ) - {produto} - R$ {preco:.2f}")
            print(f"\n( {n+1} ) - Voltar ao Setor do Estilo")
            escolha = int(input("\nEscolha o item desejado: \n"))
            print("-"*40)
            if escolha==6:
                self.roupas()
            elif escolha>6 or escolha<1:
                print(f"'{escolha}' não é um valor válido, por favor, tente novamente (PS: Escolha conforme os números na esquerda!)")
                print("-"*30)
            else:
                print (f"{produtos_calcas[escolha-1]} adicionado ao carrinho!")
                valor_compras = valor_compras + precos_calcas[escolha-1]
                print (f"Valor total do carrinho: {valor_compras:.2f}")
                carrinho.append(tudo_calcas[escolha-1])
                print ("Produtos atuais no carrinho:")
                n_produtos=0
                for produto in carrinho:
                    n_produtos+=1
                    print(f"[ {n_produtos} ] {produto}")
                print("-"*40)
    
    def shorts(self):
        global valor_compras
        global carrinho
        global n_produtos
        escolha=-1
        print("-"*40)
        while escolha!=6:
            print("SETOR DO ESTILO")
            n = 0
            for produto, preco in shorts.items():
                n+=1
                print(f"( {n} ) - {produto} - R$ {preco:.2f}")
            print(f"\n( {n+1} ) - Voltar ao Setor do Estilo")
            escolha = int(input("\nEscolha o item desejado: \n"))
            print("-"*40)
            if escolha==6:
                self.roupas()
            elif escolha>6 or escolha<1:
                print(f"'{escolha}' não é um valor válido, por favor, tente novamente (PS: Escolha conforme os números na esquerda!)")
                print("-"*30)
            else:
                print (f"{produtos_shorts[escolha-1]} adicionado ao carrinho!")
                valor_compras = valor_compras + precos_shorts[escolha-1]
                print (f"Valor total do carrinho: {valor_compras:.2f}")
                carrinho.append(tudo_shorts[escolha-1])
                print ("Produtos atuais no carrinho:")
                n_produtos=0
                for produto in carrinho:
                    n_produtos+=1
                    print(f"[ {n_produtos} ] {produto}")
                print("-"*40)
    
    def bolsas_acessorios(self):
        global valor_compras
        global carrinho
        global n_produtos
        escolha=-1
        print("-"*40)
        while escolha!=6:
            print("SETOR DO ESTILO")
            n = 0
            for produto, preco in bolsa_acessorio.items():
                n+=1
                print(f"( {n} ) - {produto} - R$ {preco:.2f}")
            print(f"\n( {n+1} ) - Voltar ao Setor do Estilo")
            escolha = int(input("\nEscolha o item desejado: \n"))
            print("-"*40)
            if escolha==6:
                self.roupas()
            elif escolha>6 or escolha<1:
                print(f"'{escolha}' não é um valor válido, por favor, tente novamente (PS: Escolha conforme os números na esquerda!)")
                print("-"*30)
            else:
                print (f"{produtos_bolsa_acessorio[escolha-1]} adicionado ao carrinho!")
                valor_compras = valor_compras + precos_bolsa_acessorio[escolha-1]
                print (f"Valor total do carrinho: {valor_compras:.2f}")
                carrinho.append(tudo_bolsa_acessorio[escolha-1])
                print ("Produtos atuais no carrinho:")
                n_produtos=0
                for produto in carrinho:
                    n_produtos+=1
                    print(f"[ {n_produtos} ] {produto}")
                print("-"*40)

    # ELETRODOMÉSTICOS: --------------------------------------------------------------------------------------------------------------------------

    # CUIDADOS PESSOAIS: --------------------------------------------------------------------------------------------------------------------------


super_mercado()