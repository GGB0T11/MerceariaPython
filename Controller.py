from Model import *
from Dao import *
from datetime import datetime

class ControllerCategoria:
    @classmethod
    def cadastrar_categoria(cls, nova_categoria):
        """
        Cadastra uma nova categoria se ela não existir.
        """
        existe = False

        # Lê a lista de categorias existentes
        lista_categorias = DaoCategoria.ler()
        for categoria in lista_categorias:
            if categoria.nome == nova_categoria:
                existe = True

        # Se a categoria não existir, salva a nova categoria
        if not existe:
            DaoCategoria.salvar(nova_categoria)
            print("Categoria cadastrada com sucesso")
        
        else:
            print("A categoria que deseja cadastrar já existe")

    @classmethod
    def remover_categoria(cls, remover):
        """
        Remove uma categoria existente.
        """
        # Lê a lista de categorias existentes
        lista_categorias = DaoCategoria.ler()
        in_lista = list(filter(lambda x: x.nome == remover, lista_categorias))
        
        # Verifica se a categoria existe
        if len(in_lista) <= 0:
            print("A categoria que deseja remover não existe")
        
        else:
            # Remove a categoria da lista
            for i in range(len(lista_categorias)):
                if lista_categorias[i].nome == remover:
                    del lista_categorias[i]
                    break

            # Atualiza o arquivo de categorias
            with open("Registros/categorias.txt", "w") as arq:
                for i in lista_categorias:
                    arq.writelines(i.nome)
                    arq.writelines("\n")
                    
            lista_estoque = DaoEstoque.ler()
            lista_estoque = list(map(lambda x: Estoque(Produto(x.produto.nome, x.produto.preco, "Sem categoria"), x.quantidade) if(x.produto.categoria == remover) else(x), lista_estoque))

            with open("Registros/estoque.txt", "w") as arq:
                for i in lista_estoque:
                    arq.writelines(i.produto.nome + ";" + i.produto.preco + ";" + i.produto.categoria + ";" + str(i.quantidade))
                    arq.writelines("\n")

            print("Categoria removida com sucesso")
        
    @classmethod
    def alterar_categoria(cls, categoria_anterior, nova_categoria):
        #TODO: alterar tbm no estoque
        """
        Altera o nome de uma categoria existente.
        """
        # Lê a lista de categorias existentes
        with open("Registros/categorias.txt", "r") as arq:
            lista_categorias = DaoCategoria.ler()
            in_lista = list(filter(lambda x: x.nome == categoria_anterior, lista_categorias))

        # Verifica se a categoria anterior existe
        if len(in_lista) > 0:
            categoria_exist = list(filter(lambda x: x.nome == nova_categoria, lista_categorias))
            
            # Verifica se a nova categoria já existe
            if len(categoria_exist) == 0:
                # Altera o nome da categoria
                lista_categorias = list(map(lambda x: Categoria(nova_categoria) if(x.nome == categoria_anterior) else(x), lista_categorias))

                # Atualiza o arquivo de categorias
                with open("Registros/categorias.txt", "w") as arq:
                    for categoria in lista_categorias:
                        arq.writelines(categoria.nome)
                        arq.writelines("\n")
                
                print("Categoria alterada com sucesso")

                lista_estoque = DaoEstoque.ler()
                lista_estoque = list(map(lambda x: Estoque(Produto(x.produto.nome, x.produto.preco, nova_categoria), x.quantidade) if(x.produto.categoria == categoria_anterior) else(x), lista_estoque))

                with open("Registros/estoque.txt", "w") as arq:
                    for i in lista_estoque:
                        arq.writelines(i.produto.nome + ";" + i.produto.preco + ";" + i.produto.categoria + ";" + str(i.quantidade))
                        arq.writelines("\n")
            
            else:
                print("A categoria que deseja alterar já existe")
        
        else:
            print("A categoria que deseja alterar não existe")

    @classmethod
    def mostrar_categoria(cls):
        """
        Exibe a lista de categorias cadastradas.
        """
        # Lê a lista de categorias existentes
        lista_categorias = DaoCategoria.ler()
        
        # Enumera e imprime cada categoria
        for categoria in enumerate(lista_categorias):
            print(f"{categoria[0] + 1}: {categoria[1].nome}")

class ControllerVenda:
    @classmethod
    def cadastrar_venda(cls, item_vendido, qte_vendida, vendedor, comprador):
        """
        Cadastra uma venda de um item, atualizando o estoque.
        """
        lista_estoque = DaoEstoque.ler()
        temp = []
        produto_exist =  False
        qte_exist = False

        # Verifica se o produto existe no estoque e se a quantidade é suficiente
        for i in lista_estoque:
            if produto_exist == False:
                if i.produto.nome == item_vendido:
                    produto_exist = True
                    if i.quantidade >= qte_vendida:
                        qte_exist = True
                        i.quantidade = int(i.quantidade) - int(qte_vendida)

                        vendido = Venda(Produto(i.produto.nome, i.produto.preco, i.produto.categoria), qte_vendida, vendedor, comprador)
                        valor_compra = int(i.produto.preco) * int(qte_vendida)

                        DaoVenda.salvar(vendido)
            
            temp.append([Produto(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade])
            
            # Atualiza o arquivo de estoque
            arq = open("Registros/estoque.txt", "w")
            arq.write("")

            for i in temp:
                with open("Registros/estoque.txt", "a") as arq:
                    arq.writelines(i[0].nome + ";" + i[0].preco + ";" + i[0].categoria + ";" + str(i[1]))
                    arq.writelines("\n")

        # Verifica se o produto existe e se a quantidade é suficiente
        if produto_exist == False:
            print("O produto não existe")
            return None
        
        elif not qte_exist:
            print("A quantidade excede o disponível em estoque")
            return None

        else:
            return valor_compra

    @classmethod
    def produtos_mais_vendidos(cls):
        """
        Exibe os produtos mais vendidos.
        """
        lista_vendas = DaoVenda.ler()
        produtos = []

        # Agrupa e soma as quantidades vendidas de cada produto
        for i in lista_vendas:
            nome = i.itensVendido.nome
            quantidade = i.qteVendida
            tamanho = list(filter(lambda x: x["produto"] == nome, produtos))
            
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {"produto": nome, "quantidade": x["quantidade"] + quantidade} if (x["produto"] == nome) else (x), produtos))
            
            else:
                produtos.append({"produto": nome, "quantidade": quantidade})
        
        # Ordena os produtos pela quantidade vendida
        produtos_ordened = sorted(produtos, key = lambda k: k["quantidade"], reverse = True)
        
        # Imprime os produtos mais vendidos
        print("Produtos mais vendidos: ")
        n = 1  
        for i in produtos_ordened:
            print(f"==========Produto {n}==========")
            print(f"produto: {i['produto']} | Quantidade: {i['quantidade']} \n")
            n += 1

    @classmethod
    def mostrar_vendas(cls, data_inicio, data_fim):
        """
        Exibe as vendas realizadas em um intervalo de datas.
        """
        lista_vendas = DaoVenda.ler()
        data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")
        data_fim = datetime.strptime(data_fim, "%d/%m/%Y")

        # Filtra as vendas pelo intervalo de datas
        vendas_selecionadas = list(filter(lambda x: datetime.strptime(x.data, "%d/%m/%Y") >= data_inicio and datetime.strptime(x.data, "%d/%m/%Y") <= data_fim, lista_vendas))

        # Imprime as vendas selecionadas
        n = 1
        preco_total = 0
        qte_total = 0
        for i in vendas_selecionadas:
            print(f"==========Produto {n}==========") 
            print(f"Nome: {i.itensVendido.nome} \n"
                  f"Preço: {i.itensVendido.preco} \n"
                  f"Categoria: {i.itensVendido.categoria} \n"
                  f"Quantidade: {i.qteVendida} \n"
                  f"Vendedor: {i.vendedor} \n"
                  f"Comprador: {i.comprador} \n"
                  f"Data: {i.data} \n")
            
            n += 1
            preco_total += float(i.itensVendido.preco)
            qte_total += int(i.qteVendida)

        print(f"Preço total: {preco_total} | Quantidade total: {qte_total}")
            
class ControllerEstoque:
    @classmethod
    def cadastrar_produto(cls, nome, preco, categoria, quantidade):
        """
        Cadastra um novo produto no estoque.
        """
        lista_estoque = DaoEstoque.ler()
        lista_categorias = DaoCategoria.ler()

        categoria_exists = list(filter(lambda x: x.nome == categoria, lista_categorias))
        produto_exists = list(filter(lambda x: x.produto.nome == nome, lista_estoque))

        # Verifica se a categoria existe e se o produto já está no estoque
        if len(categoria_exists) > 0:
            if len(produto_exists) == 0:
                DaoEstoque.salvar(Produto(nome, preco, categoria), quantidade)
                print("Produto cadastrado com sucesso")

            else:
                print("O produto já existe no estoque")

        else:
            print("Categoria inexistente")

    @classmethod  
    def remover_produto(cls, remover):
        """
        Remove um produto do estoque.
        """
        lista_estoque = DaoEstoque.ler()
        in_estoque = list(filter(lambda x: x.produto.nome == remover, lista_estoque))

        # Verifica se o produto existe no estoque
        if len(in_estoque) <= 0:
            print("O produto que deseja remover não existe")

        else:
            # Remove o produto do estoque
            for i in range(len(lista_estoque)):
                if lista_estoque[i].produto.nome == remover:
                    del lista_estoque[i]
                    break
            
            # Atualiza o arquivo de estoque
            with open("Registros/estoque.txt", "w") as arq:
                for i in lista_estoque:
                    arq.writelines(i.produto.nome + ";" + i.produto.preco + 
                           ";" + i.produto.categoria + ";" + str(i.quantidade))
                    arq.writelines("\n")
            
            print("Produto removido com sucesso")

    @classmethod
    def alterar_produto(cls, nome_anterior, novo_nome, novo_preco, nova_categoria, nova_quantidade):
        """
        Altera os dados de um produto no estoque.
        """
        lista_estoque = DaoEstoque.ler()
        lista_categorias = DaoCategoria.ler()
        categoria_exists = list(filter(lambda x: x.nome == nova_categoria, lista_categorias))

        # Verifica se a nova categoria existe
        if len(categoria_exists) > 0:
            in_estoque = list(filter(lambda x: x.produto.nome == nome_anterior, lista_estoque))
            if len(in_estoque) > 0:
                # Altera os dados do produto
                lista_estoque = list(map(lambda x: Estoque(Produto(novo_nome, novo_preco, nova_categoria), nova_quantidade) if(x.produto.nome == nome_anterior) else(x), lista_estoque))
                
                # Atualiza o arquivo de estoque
                with open("Registros/estoque.txt", "w") as arq:
                    for i in lista_estoque:
                        arq.writelines(i.produto.nome + ";" + i.produto.preco + 
                            ";" + i.produto.categoria + ";" + str(i.quantidade))
                        arq.writelines("\n")

                print("Produto alterado com sucesso")

            else:
                print("O produto que deseja alterar não existe")

        else:
            print("Categoria inexistente")
            
    @classmethod
    def mostrar_estoque(cls):
        """
        Exibe a lista de produtos no estoque.
        """
        lista_estoque = DaoEstoque.ler()
        if len(lista_estoque) == 0:
            print("Estoque vazio")

        else:    
            for i in lista_estoque:
                print(f"{i.produto.nome}, R$ {i.produto.preco}, {i.produto.categoria}, {i.quantidade} unidades")

class ControllerFornecedor:
    @classmethod
    def cadastrar_fornecedor(cls, nome, cnpj, telefone, categoria):
        """
        Cadastra um novo fornecedor.
        """
        lista_fornecedores = DaoFornecedor.ler()

        cnpj_exist = list(filter(lambda x: x.cnpj == cnpj, lista_fornecedores))
        telefone_exist = list(filter(lambda x: x.telefone == telefone, lista_fornecedores))

        # Verifica se o CNPJ e o telefone são válidos e se já existem
        if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
            if len(cnpj_exist) <= 0:
                if len(telefone_exist) <= 0:
                    DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
                    print("Fornecedor cadastrado com sucesso")

                else:
                    print("Já existe um fornecedor com esse telefone")

            else:
                print("Já existe um fornecedor com esse CNPJ")
        
        else:
            print("telefone ou CNPJ inválido")
    
    @classmethod
    # Talvez seja uma boa colocar uma verificação onde não se pode ter 2 CNPJ's iguais
    def alterar_fornecedor(cls, nome_anterior, novo_nome, novo_cnpj, novo_telefone, nova_categoria):
        lista_fornecedores = DaoFornecedor.ler()
        fornecedor_exist = list(filter(lambda x: x.nome == nome_anterior, lista_fornecedores))

        if len(fornecedor_exist) > 0:
            for i in range(len(lista_fornecedores)):
                if nome_anterior == novo_nome:
                    lista_fornecedores[i] = Fornecedor(novo_nome, novo_cnpj, novo_telefone ,nova_categoria)
            with open("Registros/fornecedores.txt", "w") as arq:
                for fornecedor in lista_fornecedores:
                    arq.writelines(fornecedor.nome + ";" + fornecedor.cnpj + ";" + 
                                   fornecedor.telefone + ";" + fornecedor.categoria)


        else:
            print("O fornecedor que deseja alterar não existe")

    @classmethod
    def remover_fornecedor(cls, remover):
        lista_fornecedores = DaoFornecedor.ler()
        fornecedor_exist = list(filter(lambda x: x.cnpj == remover, lista_fornecedores))

        if len(fornecedor_exist) <= 0:
            print("O fornecedor que deseja remover não existe")

        else:
            for i in range(len(lista_fornecedores)):
                if lista_fornecedores[i].cnpj == remover:
                    del lista_fornecedores[i]
                    break
        
            with open("Registros/fornecedores.txt", "w") as arq:
                for i in lista_fornecedores:
                    arq.writelines(i.nome + ";" + i.cnpj + ";" + i.telefone + ";" + i.categoria)
                    arq.writelines("\n")
            
            print("Fornecedor removido com sucesso")

    @classmethod
    def mostrar_fornecedores(cls):
        lista_fornecedores = DaoFornecedor.ler()
        if len(lista_fornecedores) == 0:
            print("Nenhum fornecedor registrado")

        else:
            for fornecedor in lista_fornecedores:
                print(f"Nome: {fornecedor.nome} | CNPJ: {fornecedor.cnpj} | Telefone: {fornecedor.telefone} | Categoria: {fornecedor.categoria}")
                print("-"*100)

class ControllerPessoa:
    @classmethod
    #Talvez valha a pena adicionar uma validacao das informacoes
    def cadastrar_cliente(cls, nome, cpf, telefone, email):
        lista_pessoas = DaoPessoa.ler()
        pessoa_exist = list(filter(lambda x: x.cpf == cpf, lista_pessoas))
        
        if len(pessoa_exist) > 0:
            print("Essa pessoa já está cadastrada")

        else:
            DaoPessoa.salvar(Pessoa(nome, cpf, telefone, email))
            print("Cliente cadastrado com sucesso")

    @classmethod
    def remover_cliente(cls, remover):
        lista_pessoas = DaoPessoa.ler()
        pessoa_exist = list(filter(lambda x: x.cpf == remover, lista_pessoas))
        
        if len(pessoa_exist) <= 0:
            print("O cliente que deseja remover não existe")

        else:
            for i in range(len(lista_pessoas)):
                if lista_pessoas[i].cpf == remover:
                    del lista_pessoas[i]
                    break

            with open("Registros/clientes.txt", "w") as arq:
                for pessoa in lista_pessoas:
                    arq.writelines(pessoa.nome + ";" + pessoa.cpf + ";" + 
                                   pessoa.telefone + ";" + pessoa.email)
                    arq.writelines("\n")
    
    @classmethod
    def alterar_cliente(cls, cpf_antigo, novo_nome, novo_cpf, novo_telefone, novo_email):
        lista_pessoas = DaoPessoa.ler()
        pessoa_exist = list(filter(lambda x: x.cpf == cpf_antigo, lista_pessoas))

        if len(pessoa_exist) > 0:
            for i in range(len(lista_pessoas)):
                if lista_pessoas[i].cpf == cpf_antigo:
                    lista_pessoas[i] = Pessoa(novo_nome, novo_cpf, novo_telefone, novo_email)

            with open("Registros/clientes.txt", "w") as arq:
                for pessoa in lista_pessoas:
                    arq.writelines(pessoa.nome + ";" + pessoa.cpf + ";" + 
                                   pessoa.telefone + ";" + pessoa.email)
                    arq.writelines("\n")

            print("Cliente alterado com sucesso")
            
        else:
            print("O cliente que deseja alterar não existe")

    @classmethod
    def mostrar_clientes(cls):
        lista_pessoas = DaoPessoa.ler()
        if len(lista_pessoas) == 0:
            print("Não há nenhum cliente cadastrado ainda")

        else:
            for pessoa in lista_pessoas:
                print(f"Nome: {pessoa.nome} | CPF: {pessoa.cpf} | Telefone: {pessoa.telefone} | Email: {pessoa.email}")
                print("-" * 100)

class ControllerFuncionario:
    @classmethod
    def cadastrar_funcionario(cls, nome, cpf, telefone, email, clt):
        lista_funcionarios = DaoFuncionario.ler()
        funcionario_exist = list(filter(lambda x: x.clt == clt, lista_funcionarios))
        
        if len(funcionario_exist) > 0:
            print("Funcionário já cadastrado")

        else:
            DaoFuncionario.salvar(Funcionario(nome, cpf, telefone, email, clt))
            print("Funcionário salvo com sucesso")

    @classmethod
    def remover_funcionario(cls, remover):
        lista_funcionarios = DaoFuncionario.ler()
        funcionario_exist = list(filter(lambda x: x.cpf == remover, lista_funcionarios))
        
        if len(funcionario_exist) > 0:
            for i in range(len(lista_funcionarios)):
                if lista_funcionarios[i].cpf == remover:
                    del lista_funcionarios[i]
                    break
            with open("Registros/funcionarios.txt", "w") as arq:
                for i in lista_funcionarios:
                    arq.writelines(i.nome + ";" + i.cpf + ";" + i.telefone + ";" + 
                                   i.email + ";" + i.clt)
                    arq.writelines("\n")
            
            print("Funcionário removido com sucesso")

        else:
            print("O funcionário que deseja remover não existe")

    @classmethod
    def alterar_funcionario(cls, cpf_antigo, novo_nome, novo_cpf, novo_telefone, novo_email, novo_clt):
        lista_funcionarios = DaoFuncionario.ler()
        funcionario_exist = list(filter(lambda x: x.cpf == cpf_antigo, lista_funcionarios))

        if len(funcionario_exist) > 0:
            for i in range(len(lista_funcionarios)):
                if lista_funcionarios[i].cpf == cpf_antigo:
                    lista_funcionarios[i] = Funcionario(novo_nome, novo_cpf, novo_telefone, novo_email, novo_clt)
                    break

            with open("Registros/funcionarios.txt", "w") as arq:
                for i in lista_funcionarios:
                    arq.writelines(i.nome + ";" + i.cpf + ";" + i.telefone + ";" + 
                                   i.email + ";" + i.clt)
                    arq.writelines("\n")

            print("Funcionário alterado com sucesso")

        else:
            print("O funcionário que deseja alterar não existe")

    @classmethod
    def mostrar_funcionarios(cls):
        lista_funcionarios = DaoFuncionario.ler()
        if len(lista_funcionarios) == 0:
            print("Não há nenhum cliente cadastrado ainda")

        else:
            for funcionario in lista_funcionarios:
                print(f"Nome: {funcionario.nome} | CPF: {funcionario.cpf} | Telefone: {funcionario.telefone} | Email: {funcionario.email} | CLT: {funcionario.clt}")
                print("-" * 100)
    
if __name__ == "__main__":
    ...