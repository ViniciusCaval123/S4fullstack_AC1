import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'usuario'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/gravar', methods=['POST','GET'])
def gravar():
  nome = request.form['nome']
  email = request.form['email']
  senha = request.form['senha']
  if nome and email and senha:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into user (nome, email, senha) VALUES (%s, %s, %s)', (nome, email, senha))
    conn.commit()
  return render_template('index.html')


@app.route('/listar', methods=['POST','GET'])
def listar():
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute('select nome, email, senha from usuario')
  data = cursor.fetchall()
  conn.commit()
  return render_template('lista.html', datas=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
 
 # CREATE TABLE usuario ( user_id BIGINT NOT NULL AUTO_INCREMENT, nome VARCHAR(45) NULL, email VARCHAR(45) NULL, senha VARCHAR(45) NULL, PRIMARY KEY (user_id)); DELIMITER // CREATE PROCEDURE sp_createUser( IN p_nome VARCHAR(20), IN p_email VARCHAR(20), IN p_senha VARCHAR(20)) BEGIN IF ( select exists (select 1 from usuario where email = p_email) ) THEN select 'Email já existe!!'; ELSE insert into usuario ( nome, email, senha ) values ( p_nome, p_email, p_senha );END IF; END // DELIMITER ;