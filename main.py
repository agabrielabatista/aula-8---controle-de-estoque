import json

def carregar_produtos():
    try:
        arquivo = open("produtos.json", "r", encoding="utf-8")
        produtos = json.load(arquivo)
        arquivo.close()
        return produtos
    except FileNotFoundError:
        return []

def salvar_produtos(produtos):
    arquivo = open("produtos.json", "w", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()

def listar_produtos():
    produtos = carregar_produtos()
    if not produtos:
        print("Nenhum produto cadastrado no momento.")
        return

    for item in produtos:
        print(f"ID: {item['id']} | Nome: {item['nome']} | Preço: R${item['preco']:.2f} | Estoque: {item['estoque']} | Categoria: {item['categoria']}")

def buscar_produto():
    id_busca = int(input("Digite o ID do produto que deseja buscar: "))
    produtos = carregar_produtos()

    achado = False
    for item in produtos:
        if item["id"] == id_busca:
            print(f"ID: {item['id']} | Nome: {item['nome']} | Preço: R${item['preco']:.2f} | Estoque: {item['estoque']} | Categoria: {item['categoria']}")
            achado = True
            break
            
    if not achado:
        print("Produto não encontrado com este ID.")

def adicionar_produto():
    produtos = carregar_produtos()

    proximo_id = produtos[-1]["id"] + 1 if produtos else 1
    
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    categoria = input("Digite a categoria do produto: ")
    estoque = int(input("Digite a quantidade em estoque: "))

    novo_produto = {
        "id": proximo_id,
        "nome": nome,
        "preco": preco,
        "categoria": categoria,
        "estoque": estoque
    }

    produtos.append(novo_produto)
    salvar_produtos(produtos)
    print("Produto cadastrado e salvo com sucesso!")

def remover_produto():
    nome_alvo = input("Digite o nome do produto a ser removido: ")
    produtos = carregar_produtos()
    produto_remover = None

    for item in produtos:
        if item["nome"].lower() == nome_alvo.lower():
            produto_remover = item
            break

    if produto_remover:
        produtos.remove(produto_remover)
        salvar_produtos(produtos)
        print("Produto removido com sucesso!")
    else:
        print("Produto não localizado no cadastro.")

def alterar_produto():
    id_alvo = int(input("Digite o ID do produto que deseja alterar: "))
    produtos = carregar_produtos()
    item_alvo = None

    for item in produtos:
        if item["id"] == id_alvo:
            item_alvo = item
            break

    if not item_alvo:
        print("Produto não encontrado.")
        return

    print("\nOpções de alteração:")
    print("1 - Alterar Nome")
    print("2 - Alterar Preço")
    print("3 - Alterar Categoria")
    print("4 - Alterar Estoque")

    escolha = input("Escolha o campo a alterar: ")

    if escolha == "1":
        item_alvo["nome"] = input("Digite o novo nome: ")
    elif escolha == "2":
        item_alvo["preco"] = float(input("Digite o novo preço: "))
    elif escolha == "3":
        item_alvo["categoria"] = input("Digite a nova categoria: ")
    elif escolha == "4":
        item_alvo["estoque"] = int(input("Digite a nova quantidade em estoque: "))
    else:
        print("Opção inválida.")
        return

    salvar_produtos(produtos)
    print("Informações atualizadas com sucesso!")

def filtrar_produtos():
    categoria_busca = input("Digite a categoria para filtragem: ")
    produtos = carregar_produtos()
    encontrados = False

    for item in produtos:
        if item["categoria"].lower() == categoria_busca.lower():
            print(f"ID: {item['id']} | Nome: {item['nome']} | Preço: R${item['preco']:.2f} | Estoque: {item['estoque']}")
            encontrados = True

    if not encontrados:
        print("Nenhum produto cadastrado nesta categoria.")

while True:
    print("\n=== CONTROLE DE ESTOQUE ===")
    print("1 - Listar todos os produtos")
    print("2 - Buscar produto por ID")
    print("3 - Adicionar novo produto")
    print("4 - Remover produto por nome")
    print("5 - Alterar dados do produto")
    print("6 - Filtrar produtos por categoria")
    print("7 - Sair do sistema")

    opcao = input("Selecione uma opção: ")

    if opcao == "1":
        listar_produtos()
    elif opcao == "2":
        buscar_produto()
    elif opcao == "3":
        adicionar_produto()
    elif opcao == "4":
        remover_produto()
    elif opcao == "5":
        alterar_produto()
    elif opcao == "6":
        filtrar_produtos()
    elif opcao == "7":
        print("Finalizando o sistema...")
        break
    else:
        print("Opção inválida, tente novamente.")