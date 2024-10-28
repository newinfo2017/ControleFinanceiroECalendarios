import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

class Evento {
    String titulo;
    LocalDateTime dataHora;

    public Evento(String titulo, LocalDateTime dataHora) {
        this.titulo = titulo;
        this.dataHora = dataHora;
    }

    @Override
    public String toString() {
        return "Evento: " + titulo + " em " + dataHora;
    }
}

public class Calendario {
    private List<Evento> eventos = new ArrayList<>();

    // Adiciona um novo evento ao calendário
    public void adicionarEvento(String titulo, LocalDateTime dataHora) {
        eventos.add(new Evento(titulo, dataHora));
        System.out.println("Evento '" + titulo + "' adicionado.");
    }

    // Exibe todos os eventos agendados
    public void exibirEventos() {
        for (Evento evento : eventos) {
            System.out.println(evento);
        }
    }

    public static void main(String[] args) {
        Calendario calendario = new Calendario();
        calendario.adicionarEvento("Reunião com TI", LocalDateTime.of(2024, 10, 22, 10, 30));
        calendario.adicionarEvento("Apresentação de Projeto", LocalDateTime.of(2024, 10, 23, 14, 0));

        System.out.println("\nEventos Agendados:");
        calendario.exibirEventos();
    }
}