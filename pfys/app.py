import os
from flask import Flask, request, render_template
import mysql.connector as my
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def conectar_banco():
    return my.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "neto2303"),
        database=os.getenv("DB_NAME", "PFYS")
    )






@app.route("/", methods=["GET"])
def index():
    title = "Página inicial"
    return render_template("index.html", title=title)






@app.route("/cadastrar_clientes", methods=["GET", "POST"])
def cadastrar_clientes():
    title = "Cadastrar clientes"

    if request.method == "GET":
        return render_template("cadastrar_clientes.html", title=title)

    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha_hash = request.form.get("senha_hash")
        telefone = request.form.get("telefone")
        documento = request.form.get("documento")
        endereco = request.form.get("endereco")
        observacoes = request.form.get("observacoes")

        conexao = conectar_banco()
        cursor = conexao.cursor()

        sql = "INSERT INTO clientes (nome, email, senha_hash, telefone, documento, endereco, observacoes) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        cursor.execute(sql, (nome, email, senha_hash, telefone, documento, endereco, observacoes))
        conexao.commit()

        cursor.close()
        conexao.close()

        return render_template("cadastrar_clientes.html", title=title)







@app.route("/clientes_deletar", methods=["GET", "POST"])
def deletar_cliente():
    title = "Deletar clientes"
    if request.method == "GET":
        return render_template("clientes_deletar.html")

    id_cliente = request.form.get("id")

    conexao = conectar_banco()
    cursor = conexao.cursor()

    sql = "DELETE FROM clientes WHERE id = %s"
    cursor.execute(sql, (id_cliente,))
    conexao.commit()

    cursor.close()
    conexao.close()

    return render_template("cadastrar_clientes.html")







@app.route("/cadastrar_veiculos", methods=["GET", "POST"])
def cadastrar_veiculo():
    title = "Cadastrar Veículos"
    if request.method == "GET":
        conexao = conectar_banco()
        cursor = conexao.cursor(dictionary=True)
        sql1 = 'SELECT id, nome FROM clientes'
        cursor.execute(sql1)
        resultado = cursor.fetchall()
        cursor.close()
        conexao.close()
        
        return render_template("cadastrar_veiculos.html", resultado=resultado, title=title)
    
    if request.method == "POST":
        cliente_id = request.form.get("cliente_id")
        marca = request.form.get("marca")
        modelo = request.form.get("modelo")
        placa = request.form.get("placa")
        ano = request.form.get("ano")
        observacoes = request.form.get("obs")
        
        conexao = conectar_banco()
        cursor = conexao.cursor()

        sql2 = "INSERT INTO veiculos (cliente_id, marca, modelo, placa, ano, observacoes) VALUES (%s, %s, %s, %s, %s, %s)"

        cursor.execute(sql2, (cliente_id, marca, modelo, placa, ano, observacoes))
        conexao.commit()

        cursor.close()
        conexao.close()

        return render_template("cadastrar_veiculos.html", title=title)






@app.route("/gerenciar_pecas", methods=["GET", "POST"])
def gerenciar_pecas():
    title = "Gerenciar Pecas"
    conexao = conectar_banco()
    cursor = conexao.cursor()

    sql = "SELECT * FROM pecas"

    cursor.execute(sql)
    pecas = cursor.fetchall()
    conexao.commit()

    cursor.close()
    conexao.close()

    return render_template("gerenciar_pecas.html", pecas=pecas, title=title)








@app.route("/cadastrar_pecas", methods=["GET", "POST"])
def cadastrar_pecas():
    title = "Cadastrar Pecas"
    if request.method == "GET":
        return render_template("cadastrar_pecas.html")

    nome = request.form.get("nome")
    codigo = request.form.get("codigo")
    quantidade_estoque = request.form.get("quantidade_estoque")
    custo = request.form.get("custo")
    preco_venda = request.form.get("preco_venda")
    observacoes = request.form.get("observacoes")

    conexao = conectar_banco()
    cursor = conexao.cursor()

    sql = "INSERT INTO pecas (nome, codigo, quantidade_estoque, custo, preco_venda, observacoes) VALUES (%s, %s, %s, %s, %s, %s)"

    cursor.execute(sql, (nome, codigo, quantidade_estoque, custo, preco_venda, observacoes))
    conexao.commit()

    cursor.close()
    conexao.close()

    return render_template("cadastrar_pecas.html", title=title)

@app.route("/cadastrar_os", methods=["GET", "POST"])
def cadastrar_os():
    title = "Cadastrar Ordem de Servicos"
    if request.method == "GET":
        conexao = conectar_banco()
        cursor = conexao.cursor(dictionary=True)
        sql1 = 'SELECT id, nome FROM clientes'
        cursor.execute(sql1)
        cliente = cursor.fetchall()
        cursor.close()
        conexao.close()

        conexao = conectar_banco()
        cursor = conexao.cursor(dictionary=True)
        sql2 = 'SELECT id, marca, modelo, placa FROM veiculos'
        cursor.execute(sql2)
        veiculo = cursor.fetchall()
        cursor.close()
        conexao.close()

        conexao = conectar_banco()
        cursor = conexao.cursor(dictionary=True)
        sql3 = 'SELECT id, nome FROM mecanicos'
        cursor.execute(sql3)
        mecanico = cursor.fetchall()
        cursor.close()
        conexao.close()
        return render_template("cadastrar_os.html", cliente=cliente, veiculo=veiculo, mecanico=mecanico, title=title)
    
    if request.method == "POST":
        cliente_id = request.form.get("cliente_id")
        veiculo_id = request.form.get("veiculo_id")
        mecanico_id = request.form.get("mecanico_id")
        problema_relatado = request.form.get("problema_relatado")
        diagnostico = request.form.get("diagnostico")
        observacoes = request.form.get("observacoes")
        status = request.form.get("status")
        valor_total = request.form.get("valor_total")

        conexao = conectar_banco()
        cursor = conexao.cursor()

        sql = "INSERT INTO ordem_servicos (cliente_id, veiculo_id, mecanico_id, problema_relatado, diagnostico, observacoes, status, valor_total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        

        cursor.execute(sql, (cliente_id, veiculo_id, mecanico_id, problema_relatado, diagnostico, observacoes, status, valor_total))

        conexao.commit()

        cursor.close()
        conexao.close()

        return render_template("cadastrar_os.html", title=title)


@app.route("/cadastrar_mecanico", methods=["GET", "POST"])
def cadastrar_mecanico():
    title = "Cadastrar Mecânico"
    if request.method == "GET":
        return render_template("cadastrar_mecanico.html")

    nome = request.form.get("nome")
    especialidade = request.form.get("especialidade")
    telefone = request.form.get("telefone")
    observacoes = request.form.get("observacoes")

    conexao = conectar_banco()
    cursor = conexao.cursor()

    sql = "INSERT INTO mecanicos (nome, especialidade, telefone, observacoes, ativo) VALUES (%s, %s, %s, %s, 1)"
    

    cursor.execute(sql, (nome, especialidade, telefone, observacoes))
    conexao.commit()

    cursor.close()
    conexao.close()

    return render_template("cadastrar_mecanico.html", title=title)

@app.route("/gerenciar_os", methods=["GET"])
def gerenciar_os():
    title = "Gerenciar OS"
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql1 = 'SELECT * FROM ordem_servicos'
    cursor.execute(sql1)
    ordens = cursor.fetchall()
    cursor.close()
    conexao.close()

    if ordens:  
        conexao = conectar_banco()
        cursor = conexao.cursor(dictionary=True)
        sql4 = 'SELECT data_abertura FROM ordem_servicos'
        cursor.execute(sql4)
        data = cursor.fetchall()
        cursor.close()
        conexao.close()
        print(data)
        return render_template("gerenciar_os.html", title=title, ordens=ordens, data=data)
    


    else:
        return render_template("gerenciar_os.html", title=title)
    
if __name__ == "__main__":
    app.run(debug=True)
