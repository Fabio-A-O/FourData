from click.testing import Result
import pyodbc
#from xlrd.compdoc import 

server = 'tcp:kikosandb.cajpqxmeoicq.us-east-1.rds.amazonaws.com' 
database = 'Oficina_Mecanica' 
username = 'Admin' 
password = 'FourData' 

STRConect = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password

class DataAcess:
    """def OpnConect(_init_): 
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+_init_.server+';DATABASE='+_init_.database+';UID='+_init_.username+';PWD='+ _init_.password)
        cursor = cnxn.cursor()
        return cursor"""

    def OpnConect2(conect): 
        #Instance
        cnxn = pyodbc.connect(conect)
        cursor = cnxn.cursor()
        return cursor

# Ações
class DataFunctions:

    def BuscaUsuario(User,Pass):
        try:
            cursor = DataAcess.OpnConect2(STRConect)
            Listparameters = [User,Pass]
            #Select Query
            sqlquery = """
                SET NOCOUNT ON;
                select * from Funcionario where Nome = ? and Senha = ?                   
                """
            cursor.execute(sqlquery, Listparameters)
            the_result = cursor.fetchone()[0]
            cursor.commit()
            cursor.close()
            if the_result == 0:
                return [False,the_result]
            return [True,the_result]
        except Exception as Error:
            cursor.close
            return [False,Error]

    def RegisterOS(Cliente,Veiculo,OS):
        try:
            cursor = DataAcess.OpnConect2(STRConect)
            Listparameters = [Cliente.Nome,Cliente.Telefone,Veiculo.Modelo,Veiculo.Motor,Veiculo.Placa,Veiculo.Km,Veiculo.Ano, 1 , str(OS.DataEntrada), OS.MaoObra]
            #Select Query
            sqlquery = """
                SET NOCOUNT ON;
                EXEC CADASTRA_OS
                 @nome = ?,
                 @telefone = ?,
                 @modelo = ?,
                 @motor = ?,
                 @placa = ?,
                 @km = ?,
                 @ano = ?,
                 @Id_Funcionario = ?,
                 @data = ?,
                 @mao_obra = ? ;                  
                """
            cursor.execute(sqlquery, Listparameters)
            the_result = cursor.fetchone()[0]
            cursor.commit()
            cursor.close()
            return [True,the_result]
        except Exception as Error:
            cursor.close
            return [False,Error]
    def SearchOS():
        return

    def RegisterItem(Produto,IdOs):
        try:
            cursor = DataAcess.OpnConect2(STRConect)
            #Select Query
            stringquery = """
                    SET NOCOUNT ON;
                    INSERT INTO Produtos (ID_OS_FK,Descricao, Produtos_Cliente, Produtos_Loja,QTD, Valor)
                        VALUES (?,?,?,?,?,?)
                    SELECT @@identity
                """
            parametros = [IdOs,Produto.Descricao,Produto.Produtos_Cliente,Produto.Produtos_Loja,Produto.QTD,Produto.Valor]
            cursor.execute(stringquery,parametros) 
            the_result = cursor.fetchone()[0]
            cursor.commit()
            return True
        except Exception as Error:
            cursor.close
            return [False,Error]  
    def SearchItem():
        return


    def RegisterFalhaLeitura(Namexls,Erro):
        try:
            cursor = DataAcess.OpnConect2(STRConect)
            #Select Query
            stringquery = """
                    INSERT Historico_ETL (Nomexls,Descricao, Data_Historico)
                        VALUES(?,?,getdate())
                """
            print(Erro[1])
            parametros = [Namexls,Erro.ARGS[1]]
            cursor.execute(stringquery,parametros) 
            the_result = cursor.fetchone()[0]
            cursor.commit()
            return True
        except Exception as Error:
            print(Error)
            cursor.close
            return Error
    def SearchFalhaLeitura():
        return

    #Metodo de Cadastramento 
    def Inserir(Dados):
        try:
            #AtuantesFizicos
            #_Cliente = DataFunctions.RegisterClient(Dados[1])
            #_Veiculo = DataFunctions.RegisterCar(Dados[3])
            
            #RegistrarOS
            _OS = DataFunctions.RegisterOS(Dados[1],Dados[3],Dados[4])

            if _OS[0]:
                #ProdutosServiço
                for Produto in Dados[5]:
                    _Produto = DataFunctions.RegisterItem(Produto,_OS[1])
            elif _OS[0] == False:
                DataFunctions.RegisterFalhaLeitura(Dados[6],_OS[1])
                return(False)
            return(True)
        
        except Exception as Erro:
            return [False,Erro]


