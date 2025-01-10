from Model import *

# Classe para manipulação de dados da categoria
class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        # Salva a categoria no arquivo categorias.txt
        with open("Registros/categorias.txt", "a") as arq:
            arq.writelines(categoria)
            arq.writelines("\n")
    
    @classmethod
    def ler(cls):
        # Lê as categorias do arquivo categorias.txt
        with open("Registros/categorias.txt", "r") as arq:
            cls.categorias = arq.readlines()
            
        cls.categorias = list(map(lambda x: x.replace("\n", ""), cls.categorias))

        # Cria uma lista de objetos Categoria
        lista_categorias = [Categoria(i) for i in cls.categorias]

        return lista_categorias

# Classe para manipulação de dados da venda
class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        # Salva a venda no arquivo vendas.txt
        with open("Registros/vendas.txt", "a") as arq:
            arq.writelines(venda.itensVendido.nome + ";" + venda.itensVendido.preco + ";" +
                        venda.itensVendido.categoria + ";" + str(venda.qteVendida) + ";" +
                        venda.vendedor + ";" + venda.comprador + ";" + venda.data)
            arq.writelines("\n")

    @classmethod
    def ler(cls):
        # Lê as vendas do arquivo vendas.txt
        with open("Registros/vendas.txt", "r") as arq:
            cls.vendas = arq.readlines()

        cls.vendas = list(map(lambda x: x.replace("\n", ""), cls.vendas))
        cls.vendas = list(map(lambda x: x.split(";"), cls.vendas))

        # Cria uma lista de objetos Venda
        lista_vendas = [Venda(Produto(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]) for i in cls.vendas]

        return lista_vendas

# Classe para manipulação de dados do estoque
class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produto, quantidade):
        # Salva o produto no arquivo estoque.txt
        with open("Registros/estoque.txt", "a") as arq:
            arq.writelines(produto.nome + ";" + produto.preco + 
                           ";" + produto.categoria + ";" + str(quantidade))
            arq.writelines("\n")
            
    @classmethod
    def ler(cls):
        # Lê os produtos do arquivo estoque.txt
        with open("Registros/estoque.txt", "r") as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace("\n", ""), cls.estoque))
        cls.estoque = list(map(lambda x: x.split(";"), cls.estoque))
        
        lista_estoque = []
        if len(cls.estoque) > 0:
            # Cria uma lista de objetos Estoque
            lista_estoque = [(Estoque(Produto(i[0], i[1], i[2]), int(i[3]))) for i in cls.estoque]

        return lista_estoque

# Classe para manipulação de dados do fornecedor
class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        # Salva o fornecedor no arquivo fornecedores.txt
        with open("Registros/fornecedores.txt", "a") as arq:
            arq.writelines(fornecedor.nome + ";" + fornecedor.cnpj + ";" +
                           fornecedor.telefone + ";" + fornecedor.categoria)
            arq.writelines("\n")
            
    @classmethod
    def ler(cls):
        # Lê os fornecedores do arquivo fornecedores.txt
        with open("Registros/fornecedores.txt", "r") as arq:
            cls.fornecedores = arq.readlines()

        cls.fornecedores = list(map(lambda x: x.replace("\n", ""), cls.fornecedores))
        cls.fornecedores = list(map(lambda x: x.split(";"), cls.fornecedores))

        # Cria uma lista de objetos Fornecedor
        lista_fornecedores = [Fornecedor(i[0], i[1], i[2], i[3]) for i in cls.fornecedores]

        return lista_fornecedores

# Classe para manipulação de dados da pessoa
class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        # Salva a pessoa no arquivo clientes.txt
        with open("Registros/clientes.txt", "a") as arq:
            arq.writelines(pessoa.nome + ";" + pessoa.cpf + ";" +
                           pessoa.telefone + ";" + pessoa.email)
            arq.writelines("\n")
            
    @classmethod
    def ler(cls):
        # Lê as pessoas do arquivo clientes.txt
        with open("Registros/clientes.txt", "r") as arq:
            cls.clientes = arq.readlines()

        cls.clientes = list(map(lambda x: x.replace("\n", ""), cls.clientes))
        cls.clientes = list(map(lambda x: x.split(";"), cls.clientes))

        # Cria uma lista de objetos Pessoa
        lista_clientes = [Pessoa(i[0], i[1], i[2], i[3]) for i in cls.clientes]

        return lista_clientes

# Classe para manipulação de dados do funcionário
class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        # Salva o funcionário no arquivo funcionarios.txt
        with open("Registros/funcionarios.txt", "a") as arq:
            arq.writelines(funcionario.nome + ";" + funcionario.cpf + ";" +
                           funcionario.telefone + ";" + funcionario.email + ";" +
                            funcionario.clt)
            arq.writelines("\n")
            
    @classmethod
    def ler(cls):
        # Lê os funcionários do arquivo funcionarios.txt
        with open("Registros/funcionarios.txt", "r") as arq:
            cls.funcionarios = arq.readlines()

        cls.funcionarios = list(map(lambda x: x.replace("\n", ""), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split(";"), cls.funcionarios))

        # Cria uma lista de objetos Funcionario
        lista_funcionarios = [Funcionario(i[0], i[1], i[2], i[3], i[4]) for i in cls.funcionarios]

        return lista_funcionarios
    
# Teste das funções de leitura
if __name__ == "__main__":
    ...