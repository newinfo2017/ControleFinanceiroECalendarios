import sqlite3
import pandas as pd

# Conectar ao banco de dados SQLite
conn = sqlite3.connect("db/biblioteca.db")
cursor = conn.cursor()

# Criar a tabela de prompts, caso ainda não exista
cursor.execute('''
    CREATE TABLE IF NOT EXISTS prompts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        categoria TEXT,
        nivel_complexidade TEXT,
        descricao TEXT,
        texto_prompt TEXT NOT NULL,
        tags TEXT,
        exemplo_uso TEXT
    )
''')
conn.commit()

# Função para adicionar um prompt
def adicionar_prompt(titulo, categoria, nivel_complexidade, descricao, texto_prompt, tags, exemplo_uso):
    cursor.execute('''
        INSERT INTO prompts (titulo, categoria, nivel_complexidade, descricao, texto_prompt, tags, exemplo_uso)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (titulo, categoria, nivel_complexidade, descricao, texto_prompt, tags, exemplo_uso))
    conn.commit()
    print("Prompt adicionado com sucesso.")

# Função para visualizar todos os prompts
def visualizar_prompts():
    cursor.execute("SELECT * FROM prompts")
    prompts = cursor.fetchall()
    df = pd.DataFrame(prompts, columns=["ID", "Título", "Categoria", "Nível", "Descrição", "Prompt", "Tags", "Exemplo"])
    print(df)

# Função para buscar prompts com base em palavras-chave
def buscar_prompts(palavra_chave):
    query = "SELECT * FROM prompts WHERE titulo LIKE ? OR categoria LIKE ? OR tags LIKE ?"
    cursor.execute(query, (f"%{palavra_chave}%", f"%{palavra_chave}%", f"%{palavra_chave}%"))
    resultados = cursor.fetchall()
    df = pd.DataFrame(resultados, columns=["ID", "Título", "Categoria", "Nível", "Descrição", "Prompt", "Tags", "Exemplo"])
    if not df.empty:
        print(df)
    else:
        print("Nenhum prompt encontrado com a palavra-chave fornecida.")

# Função para atualizar um prompt específico com base no ID
def atualizar_prompt(id_prompt, novo_texto_prompt):
    cursor.execute("UPDATE prompts SET texto_prompt = ? WHERE id = ?", (novo_texto_prompt, id_prompt))
    conn.commit()
    print(f"Prompt com ID {id_prompt} atualizado com sucesso.")

# Fechar a conexão com o banco de dados (opcional, pode ser usado ao finalizar o programa)
def fechar_conexao():
    conn.close()
