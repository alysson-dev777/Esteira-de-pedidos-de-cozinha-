from gerenciador import (
    pedidos_db,
    fila_cozinha,
    historico_kds,
    cardapio,
    adicionar_item,
    novo_pedido,
    iniciar_preparo,
    desfazer_acao,
    exibir_painel
)

def menu():

    while True:
        print("------------ KITCHEN FLOW ------------")
        print("[1] - NOVO PEDIDO")
        print("[2] - CARDÁPIO")
        print("[3] - ADICIONAR PRATO")
        print("[4] - INICIAR PREPARO")
        print("[5] - DESFAZER AÇÃO")
        print("[6] - EXIBIR PAINEL")
        print("[0] - SAIR")
        indice = int(input(">>> "))

        if indice == 1:
            num_comanda = int(input("Número da comada: "))
            mesa = int(input("Número da mesa: "))

            print("CARDÁPIO:")
            for prato in cardapio:
                print(f"- {prato}")

            item_menu = input("Prato escolhido: ")

            novo_pedido(num_comanda, mesa, item_menu)

        elif indice == 2:
            print("CARDÁPIO:")
            for prato in cardapio:
                print(f"- {prato}")

        elif indice == 3:
            prato = input("Nome do prato: ")

            adicionar_item(prato)

        elif indice == 4:
            iniciar_preparo()

        elif indice == 5:
            desfazer_acao()

        elif indice == 6:
            exibir_painel()

        elif indice == 0:
            print("Sistema Encerrado!")
            break
        else:
            print("Opção Inválida!")