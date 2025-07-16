#importar flask e sqlite3, criar o app, criar função criar banco, definir uma rota e retornar uma função index para renderizar o template e outra rota para cadastro
# pyright: ignore[reportMissingImports]
from flask import Flask, render_template, request, redirect 

import sqlite3

app = Flask(__name__) #cria o app flask

def criar_banco(): 
    conn = sqlite3.connect('cadastro.db') #realizar uma conexão com um banco de dados.
    c = conn.cursor() #realizar as operações da conexão
    c.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, email TEXT NOT NULL UNIQUE, idade INTEGER)

''') #executar as operações
    
    conn.commit() #salva as alterações das operações
    conn.close() #fecha as conexões das operações


#definir rota principal

@app.route('/')
#PRIMEIRO: mostrar o site para o usuario
def index():
    return render_template('form.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form["nome"]
    email = request.form["email"]
    idade = request.form["idade"]
    
    conn = sqlite3.connect("cadastro.db")
    c = conn.cursor()
    c.execute('INSERT INTO pessoas (nome, email, idade) VALUES (?, ?, ?)', (nome, email, idade))
    conn.commit()
    conn.close()
    return redirect('/lista')



@app.route('/lista', methods=['GET', 'POST'])
def lista():
    conn = sqlite3.connect("cadastro.db")
    c = conn.cursor()

    termo = request.args.get('busca', '')

    if termo:
     c.execute('SELECT * FROM pessoas WHERE nome LIKE ?', (f'%{termo}%',))


    else:
     c.execute('SELECT * FROM pessoas') #seleciona todas as linhas da tabela pessoas

    pessoas = c.fetchall() #pega todos os registros e armazena em uma lista de tuplas
    conn.close()
    return render_template("lista.html", pessoas = pessoas, busca = termo)

if __name__ == "__main__":
    criar_banco()
    app.run(debug=True)