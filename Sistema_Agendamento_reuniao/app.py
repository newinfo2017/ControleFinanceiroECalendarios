from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Função para inserir dados no banco de dados
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

# Rota para agendar a reunião
@app.route("/schedule", methods=["POST"])
def schedule_meeting():
    data = request.get_json()

    # Verificação dos dados recebidos
    title = data.get("title")
    date = data.get("date")
    time = data.get("time")
    description = data.get("description")

    if not all([title, date, time]):  # Verifica se todos os campos obrigatórios foram preenchidos
        return jsonify({"message": "Por favor, preencha todos os campos obrigatórios"}), 400

    try:
        insert_meeting(title, date, time, description)
        return jsonify({"message": "Reunião agendada com sucesso!"})
    except Exception as e:
        return jsonify({"message": f"Erro ao agendar reunião: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
