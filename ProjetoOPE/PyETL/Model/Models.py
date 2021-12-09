#Representação de objetos reais 

class Os():
    def __init__(self,ID_OS,ID_Funcionario,ID_Cliente,ID_Veiculo,DataEntrada,Pago,Observacao,MaoObra):
        self.ID_OS = ID_OS
        self.ID_Funcionario = ID_Funcionario
        self.ID_Cliente = ID_Cliente
        self.ID_Veiculo = ID_Veiculo
        self.DataEntrada = DataEntrada
        self.Pago = Pago
        self.Observacao = Observacao
        self.MaoObra = MaoObra

class Cliente():
    def __init__(self,ID_Cliente,Nome,Telefone,Email):
        self.ID_Cliente = ID_Cliente
        self.Nome = Nome
        self.Telefone = Telefone
        self.Email = Email
        
class Veiculo():
    def __init__(self,ID_Veiculo,Marca,Modelo,Motor,Placa,Km,Ano):
        self.ID_Veiculo = ID_Veiculo
        self.Marca = Marca
        self.Modelo = Modelo
        self.Motor = Motor
        self.Placa = Placa
        self.Km = Km
        self.Ano = Ano	

class Funcionario():
    def __init__(self,ID_Funcionario,Nome,Telefone,Cargo,Email):
        self.ID_Funcionario = ID_Funcionario
        self.Nome = Nome
        self.Telefone = Telefone
        self.Cargo = Cargo
        self.Email = Email
        
class Produtos():
    def __init__(self,ID_Produtos,ID_OS,Descricao,Produtos_Cliente,Produtos_Loja,QTD,Valor):
        self.ID_Produtos = ID_Produtos
        self.ID_OS = ID_OS
        self.Descricao = Descricao
        self.Produtos_Cliente = Produtos_Cliente
        self.Produtos_Loja = Produtos_Loja
        self.QTD = QTD
        self.Valor = Valor
