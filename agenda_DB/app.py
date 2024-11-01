from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from composio import App
import sqlite3


app = Flask(__name__)
CORS(app)

def insert_meeting(title, date, time, description):
    conn = sqlite3.connect('meetings.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO meetings (title, date, time, description)
        VALUES (?, ?, ?, ?)
    ''', (title, date, time, description))

    conn.commit()
    conn.close()
    
    # Rota para servir o HTML
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

    if not title or not date:
        return jsonify({"message": "Por favor, preencha todos os campos."}), 400

    try:
        insert_meeting(title, date, time, description)
        return jsonify({"message": "Reunião agendada com sucesso!"})
    except Exception as e:
        return jsonify({"message": f"Erro ao agendar reunião: {e}"}), 500
    
if __name__ == "_main_":
    app.run(debug=True)