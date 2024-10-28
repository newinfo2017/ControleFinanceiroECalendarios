import java.util.ArrayList;
import java.util.List;

class Transacao {
    String tipo;
    String descricao;
    double valor;

    public Transacao(String tipo, String descricao, double valor) {
        this.tipo = tipo;
        this.descricao = descricao;
        this.valor = valor;
    }
}

public class ControleFinanceiro {
    private List<Transacao> transacoes = new ArrayList<>();

    // Adiciona uma nova transação
    public void adicionarTransacao(String tipo, String descricao, double valor) {
        transacoes.add(new Transacao(tipo, descricao, valor));
        System.out.println("Transação '" + descricao + "' adicionada.");
    }

    // Calcula e exibe o saldo atual
    public void exibirSaldo() {
        double saldo = 0;
        for (Transacao transacao : transacoes) {
            if (transacao.tipo.equalsIgnoreCase("Receita")) {
                saldo += transacao.valor;
            } else if (transacao.tipo.equalsIgnoreCase("Gasto")) {
                saldo -= transacao.valor;
            }
        }
        System.out.println("Saldo atual: R$ " + saldo);
    }

    public static void main(String[] args) {
        ControleFinanceiro cf = new ControleFinanceiro();
        cf.adicionarTransacao("Receita", "Salário", 5000.00);
        cf.adicionarTransacao("Gasto", "Aluguel", 1500.00);
        cf.adicionarTransacao("Gasto", "Supermercado", 700.00);

        cf.exibirSaldo();
    }
}