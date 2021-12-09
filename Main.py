from concurrent.futures import process
from types import MethodDescriptorType
from click.testing import Result
from flask.helpers import flash
from flask.wrappers import Request
from DataAccess import DataAccess
from Bussines import BussinesETL
from flask import (
    Flask ,
    render_template,
    request,
    redirect,
    session,
    url_for,
    g
)

app = Flask(__name__)
app.secret_key = "12345"

#modeling
class Secret:
    def __init__(self,PASS,ID,DESC,NAME):
        self.Descripiton = DESC
        self.Password = PASS 
        self.ID = ID
        self.Name = NAME
class Cliente:
    def _init_(self,ID_Cliente,Nome,Telefone,Email):
        self.ID_Cliente = ID_Cliente
        self.Nome = Nome
        self.Telefone = Telefone
        self.Email = Email

# configurando rotas
@app.route ('/Login', methods = ['GET','POST']) 
def login (): 
    if request.method == 'POST' :
        session.pop('user_id',0)
        username = request.form [ 'username' ] 
        password = request.form [ 'password' ] 
        valid = username != '' and password != ''
        if valid:
            Result = DataAccess.DataFunctions.BuscaUsuario(username,password);    
            if Result[0]:
                session['user_id'] = 2
                session.accessed = True
                return redirect(url_for('Main'))
            else:
                flash('Login\Senha invalidos')
                return redirect(url_for('login'))            
        else:
            return redirect(url_for('login'))
    return render_template('Login.html') 

@app.route('/',methods = ['GET','POST'])
def Home ():
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template('inicio.html')

@app.route ('/Main', methods = ['GET','POST']) 
def Main (): 
    if request.method == 'POST':
        #adiciona novo segredo 
        if request.form['MS_SEC'] == 'CARREGAR':
            nome = request.form ['Name']
            Data = request.form ['Date']
            Local = request.form ['Director']
            if nome != ''  and Data != '' and Local != '':
                ListSecret = BussinesETL.Execution.Import(Local) 
                if ListSecret[0]:
                    Values = []
                    for itens in ListSecret[1]:
                        segredo = itens['secret_data']

                        date = Secret(
                        ID = itens['id'],
                        DESC = itens['description'],
                        PASS = segredo['password']+' - '+segredo['username'],
                        NAME = itens['name']
                        )
                        Values.append(date)

                    return render_template('ListSecrets.html', secrets = Values )
                else:
                    flash(ListSecret[1])
                    return redirect(url_for('Main'))
            else:
                return redirect(url_for('Main'))

        #ReurnMAIN
        elif request.form['MS_SEC'] == 'BACK_MAIN':
            return redirect(url_for('Main'))

        #ListaTodosSegredos
        elif request.form['MS_SEC'] == 'LISTAR':
            ListSecrets = True #Process.SM.SM_SECRETS_ALL()
            if ListSecrets[0] :
                Values = []
                for itens in ListSecrets[1]:
                    date = Secret(
                    ID = itens['id'],
                    DESC = itens['description'],
                    PASS = '###',
                    NAME = itens['name']
                    )
                    Values.append(date)

                return render_template('ListSecrets.html', secrets = Values )
            else:
                flash(ListSecrets[1])
                return redirect(url_for('Main'))

        #busca pelo ID
        elif request.form['MS_SEC'] == 'BUSCAR':
            id = request.form['ID_FIND']
            if id != '':
                ListSecret = True #Process.SM.SM_SECRETS_BY_ID(id)
                if ListSecret[0] :
                    Values = []
                    for itens in ListSecret[1]:
                        segredo = itens['secret_data']

                        date = Secret(
                        ID = itens['id'],
                        DESC = itens['description'],
                        PASS = segredo['password']+' - '+segredo['username'],
                        NAME = itens['name']
                    )
                    Values.append(date)
                    return render_template('ListSecrets.html', secrets = Values )
                else:
                    flash(ListSecret[1])
                    return redirect(url_for('Main'))
            else:
                return redirect(url_for('Main'))
        #Alterar segredo
        elif request.form['MS_SEC'] == 'DELETAR':
            id = request.form['ID_DELETE']
            if id != '':
                ListSecret = True #Process.SM.SM_DELETE_BY_ID(id)
                if ListSecret[0] :
                    flash('- Segredo excluido! -')
                    return redirect(url_for('Main'))  
                else:
                    flash(ListSecret[1])
                    return redirect(url_for('Main'))
            else:
                return redirect(url_for('Main'))
    
    try:
        if session['user_id'] != 2:
            return redirect(url_for('login'))    

    except Exception as Error:
        return redirect(url_for('login')) 

        
    return render_template('MainSite.html')

# area nuclear

if __name__ == '__main__' : 
   app.run (debug = True)
