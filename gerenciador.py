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
    