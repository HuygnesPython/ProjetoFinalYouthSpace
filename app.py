import mysql.connector as my
from flask import *
from dotenv import load_dotenv
import os
load_dotenv()

def conectar():
    return my.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME")
        
    )

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")
@app.route('/')
def index():
    title = 'Pagina inicial'
    return render_template('index.html', title=title)

@app.route('/login')
def login():
    title = 'Login'
    return render_template('login.html', title=title)





if __name__ == '__main__':
    app.run(debug=True)