from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Conexão e criação do banco de dados
def init_db():
    conn = sqlite3.connect('./database/reunioes.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reunioes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        data_hora TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Rota para adicionar reunião
@app.route('/add_reuniao', methods=['POST'])
def add_reuniao():
    data = request.json
    titulo = data['titulo']
    data_hora = data['data_hora']
    conn = sqlite3.connect('./database/reunioes.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO reunioes (titulo, data_hora) VALUES (?, ?)', (titulo, data_hora))
    conn.commit()
    conn.close()
    return jsonify({"status": "Reunião adicionada com sucesso!"}), 201

# Rota para consultar reuniões
@app.route('/consultar_reunioes', methods=['GET'])
def consultar_reunioes():
    conn = sqlite3.connect('./database/reunioes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reunioes')
    reunioes = cursor.fetchall()
    conn.close()
    return jsonify(reunioes)

# Rota para excluir reunião
@app.route('/excluir_reuniao', methods=['DELETE'])
def excluir_reuniao():
    id = request.args.get('id')
    conn = sqlite3.connect('./database/reunioes.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM reunioes WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({"status": "Reunião excluída com sucesso!"})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
