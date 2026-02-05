import mysql.connector as my
from flask import *
from dotenv import load_dotenv
import os

load_dotenv()


def proteger_pagina():
    if not session.get('usuario'):
        return redirect(url_for('login'))
    return None # Indica que pode prosseguir

        


def conectar():
    return my.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "12345"),
        port=os.getenv("DB_PORT", "3306"),
        database=os.getenv("DB_NAME", "PFYS")
    )

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY","1234")

@app.route('/')
def index():
    title = 'Pagina inicial'
    return render_template('index.html', title=title)


@app.route('/sair')
def sair():
    print(session.get('usuario'))
    session.clear()
    print(session.get('usuario'))
    print('Saindo.')
    return redirect(url_for('index'))




@app.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Login'
    if request.method == 'GET':
        return render_template('login.html', title=title)
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        email = request.form.get('email') 
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        sql = "SELECT * FROM usuarios WHERE email = %s"
        cursor.execute(sql, (email,))
        resultado = cursor.fetchone()
        cursor.close()
        conexao.close()
        if resultado:
            if senha == resultado['senha_hash']:
                print('E-mail e senha corretas')
                print(resultado['nome'])
                session['usuario'] = resultado['nome']
                print(session.get('usuario'))
                return redirect(url_for('dashboard'))
            else:
                print('Senha Errada')
                return render_template('login.html', title=title)
        else:
            print('E-mail errado')
            return render_template('login.html', title=title)
       

@app.route('/dashboard')
def dashboard():
    # Você PRECISA retornar o resultado da função de proteção
    resposta = proteger_pagina()
    if resposta: 
        return resposta # Aqui ele realmente executa o redirecionamento
    
    title = 'Dashboard'
    return render_template('logado.html', title=title)










@app.route('/cadastrar_veiculos', methods=['GET', 'POST'])
def cadastrar_veiculos():
    title = 'Cadastrar veiculos'
    resposta = proteger_pagina()

    if resposta: 
        return resposta 
    if request.method == 'GET':
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        sql2 = 'SELECT * FROM clientes'
        cursor.execute(sql2)
        resultado = cursor.fetchall()
        print(resultado)
        return render_template('cadastrar_veiculos.html',title=title, resultado=resultado)
   
    
    
    if request.method == 'POST':
        modelo = request.form.get('modelo')
        marca = request.form.get('marca')
        ano = request.form.get('ano')
        placa = request.form.get('placa')
        obs = request.form.get('obs')
        cliente_vinculado = request.form.get('cliente_vinculado')
        print(modelo,marca,ano,placa,obs)
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        sql = 'INSERT INTO veiculos (modelo,marca,ano,placa,obs,cliente) VALUES (%s,%s,%s,%s,%s)'
        cursor.execute(sql, (modelo,marca,ano,placa,obs,))
        conexao.commit()
        cursor.close()
        conexao.close()
        
        return render_template('cadastrar_veiculos.html', title=title, resultado=resultado)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)