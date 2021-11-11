import mysql.connector
import locale
from util import bd
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/cadastrar')
def cadastro():
    return render_template('cadastrar.html')


@app.route('/cadastro', methods=['POST'])
def cadastro2():
    nome = request.form['nome']
    data = request.form['data']
    cpf = request.form['cpf']
    email = request.form['email']
    username = request.form['username']
    senha = request.form['senha']
    confsenha = request.form['confsenha']

    mysql = bd.SQL("root", "hiragi7", "ebet")
    comando = "INSERT INTO apostador(nmecomp_ap, datanasc_ap, cpf_ap, email_ap, username_ap, senha_ap, confsenha_ap) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    if mysql.executar(comando, [nome, data, cpf, email, username, senha, confsenha]):
        msg = "Cadastro realizado com sucesso!"
    else:
        msg = "Falha no cadastro. Tente novamente!"

    return render_template('cadastro.html', msg=msg)




app.debug = 1
app.run()