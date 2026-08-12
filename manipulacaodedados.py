dados = """ 
ana@gmail.com;Notebook;4500;SP 
carlos@gmail.com;Mouse;80;RJ 
ana@gmail.com;Teclado;250;SP 
maria@gmail.com;Monitor;1200;MG 
carlos@gmail.com;Headset;350;RJ 
joao@gmail.com;Notebook;4500;PR 
maria@gmail.com;Mouse;80;MG 
""" 
dados = dados.strip()
linhas = dados.splitlines()
pedidos = []

for linha in linhas:
    campos = linha.split(";")
    nome = campos[0].strip().lower()
    produto = campos[1].strip().lower()
    valor = float(campos[2].strip().lower())
    estado = campos[3].strip().upper()
    pedido = [nome, produto, valor, estado]
    pedidos.append(pedido)

def listar_pedidos():
    print("==========Lista de pedidos==========")

    for pedido in pedidos:
        print(
            "Nome: ",pedido[0],"|"
            "Produto: ", pedido[1],"|"
            "Valor: R$", pedido[2],"|"
            "Estado: ", pedido[3],"|"
        )

def cadastrar_pedidos():

    email_cadastro = input("Digite o email que deseja cadastrar: ").strip().lower()

    
    if email_cadastro == "":
        print("Digite algum valor")
        return


    produto_cadastro = input("Digite o produto que vai cadastrar: ").strip().lower()

    if produto_cadastro == "":
        print("Digite algum produto")
        return

    try:
        valor_cadastro = float(input("Digite o valor do produto: "))

        if valor_cadastro <= 0:
            print("O valor deve ser maior que zero")
            return

    except ValueError:
        print("Digite um valor numérico válido")
        return

    estado_cadastro = input("Digite o seu estado: ").strip().upper()

    if estado_cadastro == "":
        print("Digite um estado")
        return


    pedido = [
        email_cadastro,
        produto_cadastro,
        valor_cadastro,
        estado_cadastro
    ]

    pedidos.append(pedido)

    print("Cadastro feito com sucesso!")


def buscar_clientes():
    busca_cliente = input("Digite o email do cliente que deseja buscar: ")
    for pedido in pedidos:
        if busca_cliente == pedido[0]:
            print(
                "Produto:", pedido[1],
                "| Valor: R$", pedido[2],
                "| Estado:", pedido[3],
                )
            
    if busca_cliente == False:
        print("Esse usuario n existe")

    if busca_cliente == "":
        raise ValueError("Preencha o espaco")



def buscar_produto():
    busca_produto = input("Digite o produto que deseja buscar: ")
    for pedido in pedidos:
        if busca_produto == pedido[1]:
            print(
                " Nome", pedido[0],
                "| Valor: R$", pedido[2],
                "| Estado:", pedido[3],
                )

    if busca_produto == False:
        print("Esse produto nao existe no banco")

    if busca_produto ==  "":
        raise ValueError("Preencha o espaco")



def buscar_estado():
    busca_estado = input("Digite o estado que deseja buscar: ")
    for pedido in pedidos:
        if busca_estado == pedido[3]:
            print(
                " Nome", pedido[0],
                "| Produto", pedido[1],
                "| Valor", pedido[2],
            )

    if busca_estado == False:
        print("O estado nao possui nenhum pedido")\

    if busca_estado == "":
        raise ValueError("Preencha o espaco")



def analise_financeira():
    valores = []
    for pedido in pedidos:
        valores.append(pedido[2])
        quantidade = len(valores)
        faturamento = sum(valores)
        maior = max(valores)
        menor = min(valores)
        media = faturamento / quantidade


    print("==========Analise de valores==========")
    print("Quantidade de pedidos:", quantidade)
    print("Faturamento total: R$", faturamento)
    print("Ticket médio: R$", round(media, 2))
    print("Maior venda: R$", maior)
    print("Menor venda: R$", menor)
    print("Valores ordenados:", sorted(valores))

    

def exibir_menu():
    print("1 - Listar Pedidos")
    print("2 - Cadastrar pedido")
    print("3 - Buscar por cliente")
    print("4 - Buscar por produto")
    print("5 - Buscar por estado")
    print("6 - Exibir analise financeira")
    print("7 - Sair")

def menu():
    while True:
        exibir_menu()
        opcao = input("Digite sua opcao: ")
        match opcao:
            case "1":
                listar_pedidos()
            case "2":
                cadastrar_pedidos()
            case "3":
                buscar_clientes()
            case "4":
                buscar_produto()
            case "5":
                buscar_estado()
            case "6":
                analise_financeira()
            case "7":
                print("Saindo...")
                break
            case _:
                print("Opcao invalida")

menu()
exibir_menu()