import sqlite3
import pandas as pd

def exportar_prompts_para_csv():
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect("db/biblioteca.db")
    cursor = conn.cursor()

    # Selecionar todos os prompts
    cursor.execute("SELECT * FROM prompts")
    prompts = cursor.fetchall()

    # Verificar se existem prompts para exportar
    if not prompts:
        print("Nenhum prompt encontrado para exportação.")
        return

    # Criar um DataFrame do pandas com os prompts
    df = pd.DataFrame(prompts, columns=["ID", "Título", "Categoria", "Nível de Complexidade", "Descrição", "Texto do Prompt", "Tags", "Exemplo de Uso"])

    # Salvar o DataFrame em um arquivo CSV
    try:
        df.to_csv("prompts_exportados.csv", index=False, encoding="utf-8")
        print("Exportação realizada com sucesso! Arquivo salvo como 'prompts_exportados.csv'")
    except Exception as e:
        print(f"Erro ao exportar para CSV: {e}")
    finally:
        # Fechar a conexão com o banco de dados
        conn.close()

# Executar a função
exportar_prompts_para_csv()
