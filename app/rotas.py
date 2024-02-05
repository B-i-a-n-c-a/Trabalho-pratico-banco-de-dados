from app import app
from flask import render_template, request, redirect, url_for
import sqlite3

@app.route('/')
def index():
    return render_template('inicial_form.html')

@app.route('/cadastro_funcionario')
def cadastro_funcionario():
    return render_template('funcionario_form.html')

def verifica_existencia_funcionario():
    banco = sqlite3.connect('imobiliaria_banco.db')
    cursor = banco.cursor()
    cursor.execute("SELECT COUNT(*) FROM funcionario")
    quantidade_funcionarios = cursor.fetchone()[0]
    banco.close()
    return quantidade_funcionarios > 0

@app.route('/cadastraF', methods=['POST'])
def cadastraF():
    if verifica_existencia_funcionario():
        return "Já existe um funcionário cadastrado."
    
    nome = request.form.get('nome')
    idade = request.form.get('idade')
    cpf = request.form.get('cpf')
    cargo = request.form.get('cargo')
    login = request.form.get('login')
    senha = request.form.get('senha')

    banco = sqlite3.connect('imobiliaria_banco.db')
    cursor = banco.cursor()
     
    cursor.execute('INSERT INTO funcionario (nome, idade, cpf, cargo, login, senha) VALUES (?, ?, ?, ?, ?, ?)', (nome, idade, cpf, cargo, login, senha))

    banco.commit()
    banco.close()

    return render_template('inicial_funcionario.html')


@app.route('/login')
def login_funcionario():
    return render_template('login_form.html')

@app.route('/verifica_login', methods=['GET', 'POST'])
def verifica_login():
    login = request.form.get('login')
    senha = request.form.get('senha')
    banco = sqlite3.connect('imobiliaria_banco.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM funcionario WHERE login=? AND senha=?", (login, senha))
    resultado = cursor.fetchone()   
    banco.close()

    if resultado:    
        return render_template('inicial_funcionario.html')
    else: 
        return 'login errado!!! Tente novamente, seu tonhão!!!!!!'
    
@app.route('/cadastro_cliente')
def cadastro_cliente():
    return render_template('cliente_form.html')

@app.route('/cadastraC', methods=['POST'])
def cadastraC():
    nome = request.form.get('nome')
    idade = request.form.get('idade')
    cpf = request.form.get('cpf')
    rg = request.form.get('rg')
    telefone = request.form.get('telefone')
    banco = request.form.get('banco')
    agencia = request.form.get('agencia')
    numero_conta = request.form.get('numero_conta')
    tipo_conta = request.form.get('tipo_conta')
    
    conexao_banco = sqlite3.connect('imobiliaria_banco.db')
    cursor = conexao_banco.cursor()
     
    cursor.execute('INSERT INTO cliente (nome, idade, cpf, rg, telefone, banco, agencia, numero_conta, tipo_conta) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (nome, idade, cpf, rg, telefone, banco, agencia, numero_conta, tipo_conta))

    conexao_banco.commit()
    conexao_banco.close()

    return render_template('inicial_funcionario.html')

@app.route('/cadastro_imovel')
def cadastro_imovel():
    return render_template('imovel_form.html')

@app.route('/cadastroI', methods=['POST'])
def cadastroI():
    end_numero = request.form.get('end_numero')
    end_bairro = request.form.get('end_bairro')
    end_cidade = request.form.get('end_cidade')
    end_estado = request.form.get('end_estado')
    end_cep = request.form.get('end_cep')
    area_total = request.form.get('area_total')
    qtd_comodo = request.form.get('qtd_comodo')
    preco = request.form.get('preco')
    status = request.form.get('status')

    banco = sqlite3.connect('imobiliaria_banco.db')
    cursor = banco.cursor()
 
    cursor.execute('INSERT INTO imovel (end_numero, end_bairro, end_cidade, end_estado, end_cep,area_total, qtd_comodo, preco, status) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', (end_numero, end_bairro, end_cidade, end_estado, end_cep, area_total, qtd_comodo, preco, status))

    banco.commit()
    banco.close()

    return render_template('inicial_funcionario.html')

@app.route('/imprime_imovel')
def imprime_imovel():
    banco = sqlite3.connect('imobiliaria_banco.db')
    cursor = banco.cursor()

    cursor.execute("SELECT * FROM imovel")
    dados = cursor.fetchall()

    banco.close()
    return render_template('imprime_imovel.html', dados=dados)

@app.route('/imprime_cliente')
def imprime_cliente():
    banco = sqlite3.connect('imobiliaria_banco.db')
    cursor = banco.cursor()

    cursor.execute("SELECT * FROM cliente")
    dados = cursor.fetchall()

    banco.close()
    return render_template('imprime_cliente.html', dados=dados)

def exclui_cadastro(tabela, chave, valor):
    banco = sqlite3.connect('imobiliaria_banco.db')
    cursor = banco.cursor()

    sql = f"DELETE FROM {tabela} WHERE {chave} = ?"
    cursor.execute(sql, (valor,))

    banco.commit()
    banco.close()

    return 'Dado excluido!!!'

@app.route('/exclui_imovel')
def exclui_imovel():
    return render_template('exclui_imovel.html')

@app.route('/exclui_I', methods=['POST'])
def exclui_I():
    end_cep = request.form.get('end_cep')
    tabela_a_excluir = 'imovel'
    exclui_cadastro(tabela_a_excluir, 'end_cep', end_cep)

    return render_template('inicial_funcionario.html')

@app.route('/exclui_cliente')
def exclui_cliente():
    return render_template('exclui_cliente.html')

@app.route('/exclui_C', methods=['POST'])
def exclui_C():
    cpf = request.form.get('cpf')
    tabela_a_excluir = 'cliente'
    exclui_cadastro(tabela_a_excluir, 'cpf', cpf)

    return render_template('inicial_funcionario.html')

#venv\Scripts\activate
#deactivate
