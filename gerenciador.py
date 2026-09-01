pedidos_db = {}
fila_cozinha = []
historico_kds = []
cardapio = ["Pizza", "Hambúrguer", "Água"]

def adicionar_item(prato):

    if prato not in cardapio:
        cardapio.append(prato)
        print("Nova prato adicionado!")
    else:
        print("Prato já existente!")

def novo_pedido(num_comanda, mesa, item_menu):

    if item_menu not in cardapio:
        print("Item não disponível no cardápio!")
        return

    if num_comanda in fila_cozinha:
        print(f"Comanda: {num_comanda} - Já existente!")
        return

    pedido = {
        "comanda": num_comanda,
        "mesa": mesa,
        "prato": item_menu,
        "status": "Na fila"
    }

    pedidos_db[num_comanda] = pedido

    fila_cozinha.append(num_comanda)

    historico_kds.append(("Novo_pedido", num_comanda))

    print("Pedido registrado!")

def iniciar_preparo():

    if len(fila_cozinha) == 0:
        print("Fila da cozinha vazia!")
        return

    num_comanda = fila_cozinha.pop(0)

    pedidos_db[num_comanda]["status"] = ["Preparando"]

    historico_kds.append(("Iniciar_preparo", num_comanda))

    print(f"Comanda: {num_comanda} - Em preparo")

def desfazer_acao():

    if len(historico_kds) == 0:
        print("Historico de ações vazio!")
        return

    acao, num_comanda = historico_kds.pop()

    if acao == "Iniciar_preparo":
        pedidos_db[num_comanda]["status"] = ["Na fila"]
        fila_cozinha.insert(0, num_comanda)

        print("Ação desfeita!\n Pedido retornou para a fila!")
    elif acao == "Novo_pedido":
        if num_comanda in fila_cozinha:
            fila_cozinha.remove(num_comanda)

        if num_comanda in pedidos_db:
            del pedidos_db[num_comanda]

        print("Ação desfeita!\n Pedido removido!")

def exibir_painel():
    print("--------------------------------------")
    print("------------ KITCHEN FLOW ------------")
    print("--------------------------------------\n")
    print("FILA DA COZINHA:")

    if len(fila_cozinha) == 0:
        print("Fila Vazia!")
    else:
        for posicao, numero in enumerate(fila_cozinha, start=1):
            pedido = pedidos_db[numero]

            print(
                f"{posicao}. "
                f"Comanda: {numero} | "
                f"Mesa: {pedido["mesa"]} | "
                f"{pedido["prato"]} | "
                f"{pedido["status"]}"
            )

    print("\nBASE DE DASOS:")

    if len(pedidos_db) == 0:
        print("Nenhum Pedido Cadastrado!")
    else:
        for numero, pedido in pedidos_db.items():
            print(pedido)

    print("\nHISTÓRICO DE AÇÕES:")

    if len(historico_kds) == 0:
        print("Histórico Vazio!")
    else:
        for acao in historico_kds:
            print(acao)