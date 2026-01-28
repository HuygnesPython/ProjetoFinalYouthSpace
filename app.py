import mysql.connector as my
from flask import *
from dotenv import load_dotenv
import os
load_dotenv()

def conectar():
    return my.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        port=os.getenv("DB_PORT", "3306"),
        database=os.getenv("DB_NAME", "PFYS")
    )

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")
@app.route('/')
def index():
    title = 'Pagina inicial'
    return render_template('index.html', title=title)

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
            if senha == resultado['senha']:
                print('E-mail e senha corretas')
                return redirect(url_for('logado'))
            else:
                print('Senha Errada')
                return render_template('login.html', title=title)
        else:
            print('E-mail errado')
            return render_template('login.html', title=title)
       

@app.route('/logado')
def logado():
    return render_template('logado.html')


if __name__ == '__main__':
    app.run(debug=True)