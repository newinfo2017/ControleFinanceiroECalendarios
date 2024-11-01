from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Função para inicializar o banco de dados e criar a tabela, se necessário
def init_db():
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

# Função para buscar reuniões por período no banco de dados
def get_meetings_by_period(start_date, end_date):
    try:
        conn = sqlite3.connect('meetings.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, date, time, description FROM meetings WHERE date BETWEEN ? AND ?", (start_date, end_date))
        meetings = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Erro ao buscar reuniões: {e}")
        return []
    finally:
        conn.close()
    return [{"id": row[0], "title": row[1], "date": row[2], "time": row[3], "description": row[4]} for row in meetings]

# Função para excluir uma reunião por ID
def delete_meeting(meeting_id):
    try:
        conn = sqlite3.connect('meetings.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM meetings WHERE id = ?", (meeting_id,))
        conn.commit()
        if cursor.rowcount == 0:
            return {"error": "Reunião não encontrada."}
    except sqlite3.Error as e:
        print(f"Erro ao excluir reunião: {e}")
        return {"error": "Erro ao excluir reunião do banco de dados."}
    finally:
        conn.close()
    return {"message": "Reunião excluída com sucesso."}

# Função para atualizar uma reunião por ID
def update_meeting(meeting_id, title, date, time, description):
    try:
        conn = sqlite3.connect('meetings.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE meetings 
            SET title = ?, date = ?, time = ?, description = ?
            WHERE id = ?
        ''', (title, date, time, description, meeting_id))
        conn.commit()
        if cursor.rowcount == 0:
            return {"error": "Reunião não encontrada para atualização."}
    except sqlite3.Error as e:
        print(f"Erro ao atualizar reunião: {e}")
        return {"error": "Erro ao atualizar a reunião no banco de dados."}
    finally:
        conn.close()
    return {"message": "Reunião atualizada com sucesso."}

@app.route("/")
def index():
    return render_template("index.html")

# Rota para agendar uma reunião
@app.route("/schedule", methods=["POST"])
def schedule_meeting():
    data = request.get_json()
    title = data.get("title")
    date = data.get("date")
    time = data.get("time")
    description = data.get("description")

    result = insert_meeting(title, date, time, description)
    return jsonify(result)

# Rota para buscar reuniões por período
@app.route("/get-meetings/<start_date>/<end_date>", methods=["GET"])
def fetch_meetings_by_period(start_date, end_date):
    meetings = get_meetings_by_period(start_date, end_date)
    return jsonify(meetings)

# Rota para excluir uma reunião por ID
@app.route("/delete-meeting/<int:meeting_id>", methods=["DELETE"])
def delete_meeting_route(meeting_id):
    result = delete_meeting(meeting_id)
    return jsonify(result)

# Rota para atualizar uma reunião por ID
@app.route("/update-meeting/<int:meeting_id>", methods=["PUT"])
def update_meeting_route(meeting_id):
    data = request.get_json()
    title = data.get("title")
    date = data.get("date")
    time = data.get("time")
    description = data.get("description")
    
    result = update_meeting(meeting_id, title, date, time, description)
    return jsonify(result)

if __name__ == "__main__":
    init_db()  # Inicializa o banco de dados ao iniciar o servidor
    app.run(debug=True)
