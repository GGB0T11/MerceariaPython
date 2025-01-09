from datetime import datetime

class Categoria:
    def __init__(self, nome: str):
        self.nome = nome  # Nome da categoria

class Produto:
    def __init__(self, nome: str, preco: float, categoria: str):
        self.nome = nome  # Nome do produto
        self.preco = preco  # Preço do produto
        self.categoria = categoria  # Categoria do produto

class Estoque:
    def __init__(self, produto: Produto, quantidade: int):
        self.produto = produto  # Instância da classe Produto
        self.quantidade = quantidade  # Quantidade do produto em estoque

class Venda:
    def __init__(self, itensVendido: Produto, qteVendida: int, vendedor: str, comprador: str, data: str = datetime.now().strftime("%d/%m/%y")):
        self.itensVendido = itensVendido  # Produto vendido
        self.qteVendida = qteVendida  # Quantidade vendida
        self.vendedor = vendedor  # Nome do vendedor
        self.comprador = comprador  # Nome do comprador
        self.data = data  # Data da venda, padrão é a data atual

class Fornecedor:
    def __init__(self, nome: str, cnpj: str, telefone: str, quantidade: int):
        self.nome = nome  # Nome do fornecedor
        self.cnpj = cnpj  # CNPJ do fornecedor
        self.telefone = telefone  # Telefone do fornecedor
        self.quantidade = quantidade  # Quantidade fornecida

class Pessoa:
    def __init__(self, nome: str, cpf: str, telefone: str, email: str):
        self.nome = nome  # Nome da pessoa
        self.cpf = cpf  # CPF da pessoa
        self.telefone = telefone  # Telefone da pessoa
        self.email = email  # Email da pessoa

class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: str, telefone: str, email: str, clt: str):
        super(Funcionario, self).__init__(nome, cpf, telefone, email)  # Inicializa a classe base Pessoa
        self.clt = clt  # Número da CLT do funcionário