import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Função para carregar todos os prompts
def carregar_prompts():
    conn = sqlite3.connect("db/biblioteca.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM prompts")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Função para visualizar todos os prompts
def visualizar_prompts():
    rows = carregar_prompts()
    tree.delete(*tree.get_children())
    for row in rows:
        tree.insert("", "end", values=row)

# Função para buscar prompts por palavra-chave
def buscar_prompt():
    palavra_chave = entry_busca.get()
    conn = sqlite3.connect("db/biblioteca.db")
    cursor = conn.cursor()
    query = "SELECT * FROM prompts WHERE titulo LIKE ? OR categoria LIKE ? OR tags LIKE ?"
    cursor.execute(query, (f"%{palavra_chave}%", f"%{palavra_chave}%", f"%{palavra_chave}%"))
    resultados = cursor.fetchall()
    conn.close()
    tree.delete(*tree.get_children())
    for row in resultados:
        tree.insert("", "end", values=row)
    if not resultados:
        messagebox.showinfo("Busca", "Nenhum prompt encontrado.")

# Função para adicionar um novo prompt ao banco de dados
def adicionar_prompt():
    conn = sqlite3.connect("db/biblioteca.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO prompts (titulo, categoria, nivel_complexidade, descricao, texto_prompt, tags, exemplo_uso)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            entry_titulo.get(),
            entry_categoria.get(),
            entry_nivel.get(),
            entry_descricao.get(),
            entry_texto.get(),
            entry_tags.get(),
            entry_exemplo.get()
        ))
        conn.commit()
        messagebox.showinfo("Sucesso", "Prompt adicionado com sucesso!")
        visualizar_prompts()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao adicionar prompt: {e}")
    finally:
        conn.close()

# Função para abrir o formulário de adição
def abrir_formulario_adicao():
    # Criação da janela de adição de prompt
    add_window = tk.Toplevel(app)
    add_window.title("Adicionar Novo Prompt")
    add_window.geometry("400x400")

    # Labels e campos de entrada para os atributos do prompt
    tk.Label(add_window, text="Título:").pack()
    global entry_titulo
    entry_titulo = tk.Entry(add_window)
    entry_titulo.pack()

    tk.Label(add_window, text="Categoria:").pack()
    global entry_categoria
    entry_categoria = tk.Entry(add_window)
    entry_categoria.pack()

    tk.Label(add_window, text="Nível de Complexidade:").pack()
    global entry_nivel
    entry_nivel = tk.Entry(add_window)
    entry_nivel.pack()

    tk.Label(add_window, text="Descrição:").pack()
    global entry_descricao
    entry_descricao = tk.Entry(add_window)
    entry_descricao.pack()

    tk.Label(add_window, text="Texto do Prompt:").pack()
    global entry_texto
    entry_texto = tk.Entry(add_window)
    entry_texto.pack()

    tk.Label(add_window, text="Tags:").pack()
    global entry_tags
    entry_tags = tk.Entry(add_window)
    entry_tags.pack()

    tk.Label(add_window, text="Exemplo de Uso:").pack()
    global entry_exemplo
    entry_exemplo = tk.Entry(add_window)
    entry_exemplo.pack()

    # Botão para salvar o novo prompt
    tk.Button(add_window, text="Salvar", command=adicionar_prompt).pack(pady=10)

# Função para abrir o formulário de atualização
def abrir_formulario_atualizacao():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror("Erro", "Selecione um prompt para atualizar.")
        return

    prompt_data = tree.item(selected_item)["values"]
    update_window = tk.Toplevel(app)
    update_window.title("Atualizar Prompt")
    update_window.geometry("400x400")

    tk.Label(update_window, text="Título:").pack()
    global entry_update_titulo
    entry_update_titulo = tk.Entry(update_window)
    entry_update_titulo.insert(0, prompt_data[1])
    entry_update_titulo.pack()

    tk.Label(update_window, text="Categoria:").pack()
    global entry_update_categoria
    entry_update_categoria = tk.Entry(update_window)
    entry_update_categoria.insert(0, prompt_data[2])
    entry_update_categoria.pack()

    tk.Label(update_window, text="Nível de Complexidade:").pack()
    global entry_update_nivel
    entry_update_nivel = tk.Entry(update_window)
    entry_update_nivel.insert(0, prompt_data[3])
    entry_update_nivel.pack()

    tk.Label(update_window, text="Descrição:").pack()
    global entry_update_descricao
    entry_update_descricao = tk.Entry(update_window)
    entry_update_descricao.insert(0, prompt_data[4])
    entry_update_descricao.pack()

    tk.Label(update_window, text="Texto do Prompt:").pack()
    global entry_update_texto
    entry_update_texto = tk.Entry(update_window)
    entry_update_texto.insert(0, prompt_data[5])
    entry_update_texto.pack()

    tk.Label(update_window, text="Tags:").pack()
    global entry_update_tags
    entry_update_tags = tk.Entry(update_window)
    entry_update_tags.insert(0, prompt_data[6])
    entry_update_tags.pack()

    tk.Label(update_window, text="Exemplo de Uso:").pack()
    global entry_update_exemplo
    entry_update_exemplo = tk.Entry(update_window)
    entry_update_exemplo.insert(0, prompt_data[7])
    entry_update_exemplo.pack()

    tk.Button(update_window, text="Salvar Alterações", command=lambda: atualizar_prompt(prompt_data[0])).pack(pady=10)

# Função para atualizar um prompt no banco de dados
def atualizar_prompt(prompt_id):
    conn = sqlite3.connect("db/biblioteca.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE prompts
            SET titulo = ?, categoria = ?, nivel_complexidade = ?, descricao = ?, texto_prompt = ?, tags = ?, exemplo_uso = ?
            WHERE id = ?
        """, (
            entry_update_titulo.get(),
            entry_update_categoria.get(),
            entry_update_nivel.get(),
            entry_update_descricao.get(),
            entry_update_texto.get(),
            entry_update_tags.get(),
            entry_update_exemplo.get(),
            prompt_id
        ))
        conn.commit()
        messagebox.showinfo("Sucesso", "Prompt atualizado com sucesso!")
        visualizar_prompts()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar prompt: {e}")
    finally:
        conn.close()

# Interface principal
app = tk.Tk()
app.title("Gerenciador de Prompts")
app.geometry("1280x600")

frame_busca = tk.Frame(app)
frame_busca.pack(pady=10)
tk.Label(frame_busca, text="Buscar:").pack(side="left")
entry_busca = tk.Entry(frame_busca, width=50)
entry_busca.pack(side="left")
btn_buscar = tk.Button(frame_busca, text="Buscar", command=buscar_prompt)
btn_buscar.pack(side="left")

tree = ttk.Treeview(app, columns=("ID", "Título", "Categoria", "Nível de Complexidade", "Descrição", "Texto do Prompt", "Tags", "Exemplo de Uso"), show="headings")
tree.pack(expand=True, fill="both")
for col in tree["columns"]:
    tree.heading(col, text=col)

btn_visualizar = tk.Button(app, text="Visualizar Todos", command=visualizar_prompts)
btn_visualizar.pack(pady=10)

# Botões de Adição e Atualização
btn_adicionar = tk.Button(app, text="Adicionar Prompt", command=abrir_formulario_adicao)
btn_adicionar.pack(pady=5)

btn_atualizar = tk.Button(app, text="Atualizar Prompt", command=abrir_formulario_atualizacao)
btn_atualizar.pack(pady=5)

# Executar a interface gráfica
visualizar_prompts()
app.mainloop()
