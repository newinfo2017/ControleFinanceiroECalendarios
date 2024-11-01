from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Função para inicializar o banco de dados e criar a tabela, se necessário
def init_db():
    try:
        conn = sqlite3.connect('meetings.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS meetings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                date TEXT NOT NULL,
                time TEXT NOT NULL,
                description TEXT
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao inicializar o banco de dados: {e}")
    finally:
        conn.close()

# Função para inserir uma reunião no banco de dados
def insert_meeting(title, date, time, description):
    try:
        conn = sqlite3.connect('meetings.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO meetings (title, date, time, description)
            VALUES (?, ?, ?, ?)
        ''', (title, date, time, description))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao adicionar reunião: {e}")
        return {"error": "Erro ao adicionar reunião no banco de dados."}
    finally:
        conn.close()
    return {"message": "Reunião agendada com sucesso!"}

# Função para buscar uma reunião por título no banco de dados
def get_meeting_by_title(title):
    try:
        conn = sqlite3.connect('meetings.db')
        cursor = conn.cursor()
        cursor.execute("SELECT title, date, time, description FROM meetings WHERE LOWER(title) = LOWER(?)", (title,))
        meeting = cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Erro ao buscar reunião: {e}")
        return None
    finally:
        conn.close()
    return {"title": meeting[0], "date": meeting[1], "time": meeting[2], "description": meeting[3]} if meeting else None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/schedule", methods=["POST"])
def schedule_meeting():
    data = request.get_json()
    title = data.get("title")
    date = data.get("date")
    time = data.get("time")
    description = data.get("description")

    result = insert_meeting(title, date, time, description)
    return jsonify(result)

# Rota para buscar reunião por título
@app.route("/get-meeting/<title>", methods=["GET"])
def fetch_meeting(title):
    meeting = get_meeting_by_title(title)
    if meeting:
        return jsonify(meeting)
    else:
        return jsonify({"error": "Reunião não encontrada."})

if __name__ == "__main__":
    init_db()  # Inicializa o banco de dados ao iniciar o servidor
    app.run(debug=True)
