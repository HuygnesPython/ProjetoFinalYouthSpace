import mysql.connector
from flask import *

app = Flask(__name__)

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