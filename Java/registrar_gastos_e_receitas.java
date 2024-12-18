import csv

# Função para registrar uma transação (gasto ou receita)
def registrar_transacao(tipo, descricao, valor):
    with open("financas.csv", "a", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([tipo, descricao, valor])
    print(f"Transação '{descricao}' registrada.")

# Função para visualizar o saldo atual
def exibir_saldo():
    saldo = 0
    with open("financas.csv", "r") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            tipo, descricao, valor = linha
            if tipo == "Receita":
                saldo += float(valor)
            elif tipo == "Gasto":
                saldo -= float(valor)
    print(f"Saldo atual: R$ {saldo:.2f}")

# Exemplo de uso
registrar_transacao("Receita", "Salário", 5000.00)
registrar_transacao("Gasto", "Aluguel", 1200.00)
registrar_transacao("Gasto", "Supermercado", 800.00)

exibir_saldo()