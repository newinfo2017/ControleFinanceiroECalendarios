import tkinter as tk
from tkinter import messagebox
import datetime
import smtplib
import pywhatkit as kit

# Lista para armazenar reuniões
reunioes = []

# Função para enviar e-mail de lembrete
def enviar_email(destinatario, assunto, mensagem):
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login("seuemail@gmail.com", "suasenha")
        corpo = f"Subject: {assunto}\n\n{mensagem}"
        servidor.sendmail("seuemail@gmail.com", destinatario, corpo)
        servidor.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

# Função para enviar mensagem WhatsApp
def enviar_whatsapp(numero, mensagem):
    try:
        hora = datetime.datetime.now().hour
        minuto = datetime.datetime.now().minute + 1  # Enviar em 1 minuto
        kit.sendwhatmsg(numero, mensagem, hora, minuto)
        print("Mensagem enviada com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar mensagem WhatsApp: {e}")

# Função para adicionar uma reunião
def adicionar_reuniao():
    titulo = entrada_titulo.get()
    data = entrada_data.get()
    hora = entrada_hora.get()
    email = entrada_email.get()
    whatsapp = entrada_whatsapp.get()

    try:
        data_hora = datetime.datetime.strptime(f"{data} {hora}", "%d/%m/%Y %H:%M")
        reunioes.append({"titulo": titulo, "data_hora": data_hora, "email": email, "whatsapp": whatsapp})
        messagebox.showinfo("Reunião", f"Reunião '{titulo}' adicionada com sucesso!")
        entrada_titulo.delete(0, tk.END)
        entrada_data.delete(0, tk.END)
        entrada_hora.delete(0, tk.END)
        entrada_email.delete(0, tk.END)
        entrada_whatsapp.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erro", "Data e hora no formato inválido. Use DD/MM/YYYY HH:MM")

# Função para verificar reuniões e enviar lembretes
def verificar_lembretes():
    agora = datetime.datetime.now()
    for reuniao in reunioes:
        if reuniao["data_hora"] <= agora:
            mensagem = f"Lembrete: Reunião '{reuniao['titulo']}' agora!"
            enviar_email(reuniao["email"], "Lembrete de Reunião", mensagem)
            enviar_whatsapp(reuniao["whatsapp"], mensagem)
            reunioes.remove(reuniao)
    janela.after(60000, verificar_lembretes)  # Verificar a cada 60 segundos

# Interface gráfica com Tkinter
janela = tk.Tk()
janela.title("Agenda de Reuniões")

# Widgets de entrada
tk.Label(janela, text="Título:").grid(row=0, column=0, padx=10, pady=5)
entrada_titulo = tk.Entry(janela)
entrada_titulo.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Data (DD/MM/YYYY):").grid(row=1, column=0, padx=10, pady=5)
entrada_data = tk.Entry(janela)
entrada_data.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Hora (HH:MM):").grid(row=2, column=0, padx=10, pady=5)
entrada_hora = tk.Entry(janela)
entrada_hora.grid(row=2, column=1, padx=10, pady=5)

tk.Label(janela, text="E-mail:").grid(row=3, column=0, padx=10, pady=5)
entrada_email = tk.Entry(janela)
entrada_email.grid(row=3, column=1, padx=10, pady=5)

tk.Label(janela, text="WhatsApp (+5511999999999):").grid(row=4, column=0, padx=10, pady=5)
entrada_whatsapp = tk.Entry(janela)
entrada_whatsapp.grid(row=4, column=1, padx=10, pady=5)

# Botão para adicionar reunião
botao_adicionar = tk.Button(janela, text="Adicionar Reunião", command=adicionar_reuniao)
botao_adicionar.grid(row=5, column=0, columnspan=2, pady=10)

# Iniciar verificação de lembretes
janela.after(60000, verificar_lembretes)  # Verificar a cada 60 segundos

# Iniciar o loop da interface gráfica
janela.mainloop()
