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
        #TODO: Remover tbm do estoque, deixar sem categoria
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
            
            else:
                print("A categoria que deseja alterar já existe")
        
        else:
            print("A categoria que deseja alterar não existe")

    @classmethod
    def mostrar_categoria(cls):
        lista_categorias = DaoCategoria.ler()
        
        for categoria in enumerate(lista_categorias):
            print(f"{categoria[0] + 1}: {categoria[1].nome}")

class ControllerEstoque:
    @classmethod
    def cadastrar_produto(cls, nome, preco, categoria, quantidade):
        lista_estoque = DaoEstoque.ler()
        lista_categorias = DaoCategoria.ler()

        categoria_exists = list(filter(lambda x: x.nome == categoria, lista_categorias))
        produto_exists = list(filter(lambda x: x.produto.nome == nome, lista_estoque))

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
        lista_estoque = DaoEstoque.ler()
        in_estoque = list(filter(lambda x: x.produto.nome == remover, lista_estoque))

        if len(in_estoque) <= 0:
            print("O produto que deseja remover não existe")

        else:
            for i in range(len(lista_estoque)):
                if lista_estoque[i].produto.nome == remover:
                    del lista_estoque[i]
                    break
            
            with open("Registros/estoque.txt", "w") as arq:
                for i in lista_estoque:
                    arq.writelines(i.produto.nome + ";" + i.produto.preco + 
                           ";" + i.produto.categoria + ";" + str(i.quantidade))
                    arq.writelines("\n")
            
            print("Categoria removida com sucesso")

    @classmethod
    def alterar_produto(cls,nome_anterior, novo_nome, novo_preco, nova_categoria, nova_quantidade):
        lista_estoque = DaoEstoque.ler()
        lista_categorias = DaoCategoria.ler()
        categoria_exists = list(filter(lambda x: x.nome == nova_categoria, lista_categorias))

        if len(categoria_exists) > 0:
            in_estoque = list(filter(lambda x: x.produto.nome == nome_anterior, lista_estoque))
            if len(in_estoque) > 0:
                lista_estoque = list(map(lambda x: Estoque(Produto(novo_nome, novo_preco, nova_categoria), nova_quantidade) if(x.produto.nome == nome_anterior) else(x), lista_estoque))
                
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
        lista_estoque = DaoEstoque.ler()
        if len(lista_estoque) == 0:
            print("Estoque vazio")

        else:    
            for i in lista_estoque:
                print(f"{i.produto.nome}, R$ {i.produto.preco}, {i.produto.categoria}, {i.quantidade} unidades")

class ControllerVenda:
    @classmethod
    def cadastrar_venda(cls, item_vendido, qte_vendida, vendedor, comprador):
        lista_estoque = DaoEstoque.ler()
        temp = []
        produto_exist =  False
        qte_exist = False
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
            
            arq = open("Registros/estoque.txt", "w")
            arq.write("")

            for i in temp:
                with open("Registros/estoque.txt", "a") as arq:
                    arq.writelines(i[0].nome + ";" + i[0].preco + ";" + i[0].categoria + ";" + str(i[1]))
                    arq.writelines("\n")

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
        lista_vendas = DaoVenda.ler()
        produtos = []

        for i in lista_vendas:
            nome = i.itensVendido.nome
            quantidade = i.qteVendida
            tamanho = list(filter(lambda x: x["produto"] == nome, produtos))
            
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {"produto": nome, "quantidade": x["quantidade"] + quantidade} if (x["produto"] == nome) else (x), produtos))
            
            else:
                produtos.append({"produto": nome, "quantidade": quantidade})
        
            produtos_ordened = sorted(produtos, key = lambda k: k["quantidade"], reverse = True)
            
            print("Produtos mais vendidos: ")
            n = 1  
            for i in produtos:
                print(f"==========Produto {n}==========")
                print(f"produto: {i["produto"]} | Quantidade: {i["quantidade"]} \n")

                n += 1

if __name__ == "__main__":
    ...