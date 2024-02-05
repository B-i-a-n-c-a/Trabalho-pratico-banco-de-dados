import sqlite3

banco = sqlite3.connect('imobiliaria_banco.db')
cursor = banco.cursor()

def criar_tabelas():
  cursor.execute(
  "CREATE TABLE funcionario (nome text, idade integer, cpf text primary key unique, cargo text, login text, senha text)"
  )

  cursor.execute(
    "CREATE TABLE cliente (nome text, idade integer, cpf text primary key, rg text, telefone text, banco text, agencia text, numero_conta text, tipo_conta text, unique(cpf, banco, agencia, numero_conta))"
  )

  cursor.execute(
    "CREATE TABLE imovel (end_numero integer, end_bairro text, end_cidade text, end_estado text, end_cep text,area_total real, qtd_comodo integer, preco real, status text)"
  )

banco.commit()
banco.close()














































