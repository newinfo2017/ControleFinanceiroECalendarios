import datetime
import time

# Lista para armazenar as reuniões
reunioes = []

# Função para adicionar uma nova reunião
def adicionar_reuniao(titulo, data_hora):
    reunioes.append({"titulo": titulo, "data_hora": data_hora})
    print(f"Reunião '{titulo}' adicionada para {data_hora}")

# Função para verificar e enviar lembretes
def verificar_lembretes():
    agora = datetime.datetime.now()
    for reuniao in reunioes:
        if reuniao["data_hora"] <= agora:
            print(f"Lembrete: Reunião '{reuniao['titulo']}' agora!")
            reunioes.remove(reuniao)

# Exemplo de uso
adicionar_reuniao("Reunião com Marketing", datetime.datetime(2024, 10, 22, 9, 0))
adicionar_reuniao("Reunião de Projeto", datetime.datetime(2024, 10, 21, 15, 0))

# Verifica lembretes continuamente (a cada 10 segundos)
while True:
    verificar_lembretes()
    time.sleep(10)