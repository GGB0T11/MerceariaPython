from Controller import *

# Loop principal do menu
while True:
    # Exibe as opções principais do menu
    print("---Opções: " + ("-" * 35) + "\n",
          "1: Categoria\n",
          "2: Venda\n", 
          "3: Estoque\n", 
          "4: Fornecedor\n", 
          "5: Cliente\n", 
          "6: Funcionário\n",
          "7: Sair")
    escolha = int(input("---> "))

    # Estrutura de decisão para as opções do menu principal
    match escolha:
        case 1:
            # Menu de Categoria
            while True:
                print("---Menu Categoria: " + ("-" * 35) + "\n",
                "1: Cadastrar categoria\n",
                "2: Remover categoria\n", 
                "3: Alterar categoria\n", 
                "4: Mostrar categorias\n", 
                "5: Sair")
                escolha = int(input("---> "))
                match escolha:
                    case 1:
                        # Cadastrar nova categoria
                        nova_categoria = input("Digite a categoria a ser cadastrada: ")
                        print("-" * 50)
                        ControllerCategoria.cadastrar_categoria(nova_categoria)
                        break

                    case 2:
                        # Remover categoria existente
                        remover_categoria = input("Digite a categoria a ser removida: ")
                        print("-" * 50)
                        ControllerCategoria.remover_categoria(remover_categoria)
                        break

                    case 3:
                        # Alterar categoria existente
                        alterar_categoria = input("Digite a categoria a ser alterada: ")
                        nova_categoria = input("Digite a nova categoria")
                        print("-" * 50)
                        ControllerCategoria.alterar_categoria(alterar_categoria, nova_categoria)
                        break

                    case 4:
                        # Mostrar todas as categorias
                        ControllerCategoria.mostrar_categoria()
                        break
                    
                    case 5:
                        # Sair do menu de Categoria
                        break

                    case _:
                        print("\nSelecione uma opção válida\n")
                    
        case 2:
            # Menu de Venda
            while True:
                print("---Menu Venda: " + ("-" * 35) + "\n",
                "1: Cadastrar venda\n",
                "2: Produtos mais vendidos\n", 
                "3: Mostrar vendas\n", 
                "4: Sair")
                escolha = int(input("---> "))
                match escolha:
                    case 1:
                        # Cadastrar nova venda
                        item_vendido = input("Digite o item vendido: ")
                        qte_vendida = input("Digite a quantidade vendida: ")
                        vendedor = input("Digite o nome do vendedor: ")
                        comprador = input("Digite o nome do comprador")
                        print("-" * 50)
                        ControllerVenda.cadastrar_venda(item_vendido, qte_vendida, vendedor, comprador)
                        break

                    case 2:
                        # Mostrar produtos mais vendidos
                        ControllerVenda.produtos_mais_vendidos()
                        break

                    case 3:
                        # Mostrar vendas em um intervalo de datas
                        data_inicio = input("Digite a data do inicio: ")
                        data_fim = input("Digite a data do fim: ")
                        print("-" * 50)
                        ControllerVenda.mostrar_vendas(data_inicio, data_fim)
                        break

                    case 4:
                        # Sair do menu de Venda
                        break

                    case _:
                        print("\nSelecione uma opção válida\n")

        case 3:
            # Menu de Estoque
            while True:
                print("---Menu Estoque: " + ("-" * 35) + "\n",
                "1: Cadastrar estoque\n",
                "2: Remover estoque\n", 
                "3: Alterar estoque\n", 
                "4: Mostrar estoque\n", 
                "5: Sair")
                escolha = int(input("---> "))
                match escolha:
                    case 1:
                        # Cadastrar novo produto no estoque
                        nome = input("Digite o nome do produto: ")
                        preco = input("Digite o preço do produto: ")
                        categoria = input("Digite a categoria do produto: ")
                        quantidade = input("Digite a quantidade do produto: ")
                        print("-" * 50)
                        ControllerEstoque.cadastrar_produto(nome, preco, categoria, quantidade)
                        break

                    case 2:
                        # Remover produto do estoque
                        remover_produto = input("Digite o nome do produto a ser removido: ")
                        print("-" * 50)
                        ControllerEstoque.remover_produto(remover_produto)
                        break

                    case 3:
                        # Alterar produto no estoque
                        alterar_produto = input("Digite o nome do produto a ser alterado: ")
                        novo_nome = input("Digite o novo nome:")
                        novo_preco = input("Digite o novo preço:")
                        nova_categoria = input("Digite a nova categoria: ")
                        nova_quantidade = input("Digite a nova quantidade: ")
                        print("-" * 50)
                        ControllerEstoque.alterar_produto(alterar_produto, novo_nome, novo_preco, nova_categoria, nova_quantidade)
                        break

                    case 4:
                        # Mostrar todos os produtos no estoque
                        ControllerEstoque.mostrar_estoque()
                        break
                    
                    case 5:
                        # Sair do menu de Estoque
                        break

                    case _:
                        print("\nSelecione uma opção válida\n")

        case 4:
            # Menu de Fornecedor
            while True:
                print("---Menu Fornecedor: " + ("-" * 35) + "\n",
                "1: Cadastrar fornecedor\n",
                "2: Remover fornecedor\n", 
                "3: Alterar fornecedor\n", 
                "4: Mostrar fornecedores\n", 
                "5: Sair")
                escolha = int(input("---> "))
                match escolha:
                    case 1:
                        # Cadastrar novo fornecedor
                        nome = input("Digite o nome do fornecedor: ")
                        cnpj = input("Digite o CNPJ do fornecedor: ")
                        telefone = input("Digite o telefone do forencedor: ")
                        categoria = input("Digite a categoria fornecida: ")
                        print("-" * 50)
                        ControllerFornecedor.cadastrar_fornecedor(nome, cnpj, telefone, categoria)
                        break

                    case 2:
                        # Remover fornecedor existente
                        remover_fornecedor = input("Digite o CNPJ do fornecedor: ")
                        print("-" * 50)
                        ControllerFornecedor.remover_fornecedor(remover_fornecedor)
                        break

                    case 3:
                        # Alterar fornecedor existente
                        alterar_fornecedor = input("Digite o CNPJ do fornecedor a ser alterado: ")
                        novo_nome = input("Digite o novo nome:")
                        novo_cnpj = input("Digite o novo CNPJ:")
                        novo_telefone = input("Digite o novo telefone: ")
                        nova_categoria = input("Digite a nova categoria: ")
                        print("-" * 50)
                        ControllerFornecedor.alterar_fornecedor(alterar_fornecedor, novo_nome, novo_cnpj, novo_telefone, nova_categoria)
                        break

                    case 4:
                        # Mostrar todos os fornecedores
                        ControllerFornecedor.mostrar_fornecedores()
                        break
                    
                    case 5:
                        # Sair do menu de Fornecedor
                        break

                    case _:
                        print("\nSelecione uma opção válida\n")

        case 5:
            # Menu de Cliente
            while True:
                print("---Menu Cliente: " + ("-" * 35) + "\n",
                "1: Cadastrar cliente\n",
                "2: Remover cliente\n", 
                "3: Alterar cliente\n", 
                "4: Mostrar clientes\n", 
                "5: Sair")
                escolha = int(input("---> "))
                match escolha:
                    case 1:
                        # Cadastrar novo cliente
                        nome = input("Digite o nome do cliente: ")
                        cpf = input("Digite o CPF do cliente: ")
                        telefone = input("Digite o telefone do cliente: ")
                        email = input("Digite ao email cliente: ")
                        print("-" * 50)
                        ControllerPessoa.cadastrar_cliente(nome, cpf, telefone, email)
                        break

                    case 2:
                        # Remover cliente existente
                        remover_cliente = input("Digite o CPF do fornecedor: ")
                        print("-" * 50)
                        ControllerPessoa.remover_cliente(remover_cliente)
                        break

                    case 3:
                        # Alterar cliente existente
                        alterar_fornecedor = input("Digite o CPF do cliente a ser alterado: ")
                        novo_nome = input("Digite o novo nome:")
                        novo_cpf = input("Digite o novo CPF:")
                        novo_telefone = input("Digite o novo telefone: ")
                        novo_email = input("Digite o novo email: ")
                        print("-" * 50)
                        ControllerPessoa.alterar_cliente(alterar_fornecedor, novo_nome, novo_cpf, novo_telefone, novo_email)
                        break

                    case 4:
                        # Mostrar todos os clientes
                        ControllerPessoa.mostrar_clientes()
                        break
                    
                    case 5:
                        # Sair do menu de Cliente
                        break

                    case _:
                        print("\nSelecione uma opção válida\n")

        case 6:
            # Menu de Funcionário
            while True:
                print("---Menu Funcionário: " + ("-" * 35) + "\n",
                "1: Cadastrar funcionário\n",
                "2: Remover funcionário\n", 
                "3: Alterar funcionário\n", 
                "4: Mostrar funcionário\n", 
                "5: Sair")
                escolha = int(input("---> "))
                match escolha:
                    case 1:
                        # Cadastrar novo funcionário
                        nome = input("Digite o nome do funcionário: ")
                        cpf = input("Digite o CPF do funcionário: ")
                        telefone = input("Digite o telefone do funcionário: ")
                        email = input("Digite ao email funcionário: ")
                        clt = input("Digite a clt do funcionário")
                        print("-" * 50)
                        ControllerFuncionario.cadastrar_funcionario(nome, cpf, telefone, email, clt)
                        break

                    case 2:
                        # Remover funcionário existente
                        remover_funcionario = input("Digite o CPF do funcionário: ")
                        print("-" * 50)
                        ControllerFuncionario.remover_funcionario(remover_funcionario)
                        break

                    case 3:
                        # Alterar funcionário existente
                        alterar_funcionario = input("Digite o CPF do funcionário a ser alterado: ")
                        novo_nome = input("Digite o novo nome:")
                        novo_cpf = input("Digite o novo CPF:")
                        novo_telefone = input("Digite o novo telefone: ")
                        novo_email = input("Digite o novo email: ")
                        nova_clt = ("Digite a nova CLT: ")
                        print("-" * 50)
                        ControllerFuncionario.alterar_funcionario(alterar_funcionario, novo_nome, novo_cpf, novo_telefone, novo_email, nova_clt)
                        break

                    case 4:
                        # Mostrar todos os funcionários
                        ControllerFuncionario.mostrar_funcionarios()
                        break
                    
                    case 5:
                        # Sair do menu de Funcionário
                        break

                    case _:
                        print("\nSelecione uma opção válida\n")

        case 7:
            # Sair do programa
            break

        case _:
            print("\nSelecione uma opção válida\n")

print("\nCódigo encerrado\n")