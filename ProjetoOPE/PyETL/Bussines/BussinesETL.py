from DataAccess import DataAccess
from Process import Process

class Execution():

    def Import(Caminho):
        #Instancias
        CarregandoArquivos = Process.Read.LoadFiles("C:\\Users\\LuisG\\Desktop\\ProjetoOPE\\Dados")
        ListaResutados = []
        AuxIndex = 0
        #Lendo lista de arquivos e preparando para inserir
        for File in CarregandoArquivos:
            AuxIndex += 1
            Dados = Process.AutoXrdl.Readxls(File)

            if Dados[0] == True:
                # Registrar dados Sucesso
                ListaResutados.insert(AuxIndex,'True')
                Insercao = DataAccess.DataFunctions.Inserir(Dados);  

            else:
                # Registrar dados Falha
                ListaResutados.insert(AuxIndex,'False')
                DataAccess.DataFunctions.RegisterFalhaLeitura(Dados[2],Dados[1]);
        
        return 'True'