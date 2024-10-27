import datetime
import time
import tkinter as tk
from tkinter import messagebox
from threading import Thread

# Lista para armazenar as reuniões
reunioes = []

# Função para adicionar uma nova reunião
def adicionar_reuniao(titulo, data_hora):
    reunioes.append({"titulo": titulo, "data_hora": data_hora, "concluida": False})
    messagebox.showinfo("Reunião Adicionada", f"Reunião '{titulo}' adicionada para {data_hora}")

# Função para verificar e enviar lembretes
def verificar_lembretes():
    while True:
        agora = datetime.datetime.now()
        for reuniao in reunioes:
            if not reuniao["concluida"] and reuniao["data_hora"] <= agora:
                messagebox.showinfo("Lembrete", f"Lembrete: Reunião '{reuniao['titulo']}' agora!")
                reuniao["concluida"] = True
        time.sleep(10)

# Função para adicionar reunião através da interface
def adicionar_reuniao_interface():
    titulo = titulo_entry.get()
    data = data_entry.get()
    hora = hora_entry.get()
    
    try:
        # Converte data e hora para objeto datetime
        data_hora = datetime.datetime.strptime(f"{data} {hora}", "%d/%m/%Y %H:%M")
        adicionar_reuniao(titulo, data_hora)
    except ValueError:
        messagebox.showerror("Erro", "Data e hora devem estar no formato correto: DD/MM/AAAA HH:MM")

# Configurações da Interface Gráfica
janela = tk.Tk()
janela.title("Gerenciador de Reuniões")

# Campos de Entrada
tk.Label(janela, text="Título da Reunião:").grid(row=0, column=0, padx=10, pady=5)
titulo_entry = tk.Entry(janela, width=30)
titulo_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Data (DD/MM/AAAA):").grid(row=1, column=0, padx=10, pady=5)
data_entry = tk.Entry(janela, width=15)
data_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Hora (HH:MM):").grid(row=2, column=0, padx=10, pady=5)
hora_entry = tk.Entry(janela, width=15)
hora_entry.grid(row=2, column=1, padx=10, pady=5)

# Botão para Adicionar Reunião
adicionar_btn = tk.Button(janela, text="Adicionar Reunião", command=adicionar_reuniao_interface)
adicionar_btn.grid(row=3, column=0, columnspan=2, pady=10)

# Inicia a verificação de lembretes em um thread separado
lembrete_thread = Thread(target=verificar_lembretes, daemon=True)
lembrete_thread.start()

# Inicia a interface gráfica
janela.mainloop()
