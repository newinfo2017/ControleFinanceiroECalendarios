document.getElementById("meeting-form").addEventListener("submit", async function (event) {
    event.preventDefault();

    const title = document.getElementById("title").value;
    const date = document.getElementById("date").value;
    const time = document.getElementById("time").value;
    const description = document.getElementById("description").value;

    try {
        const response = await fetch("http://127.0.0.1:5000/schedule", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ title, date, time, description })
        });

        const result = await response.json();
        document.getElementById("message").innerText = result.error || result.message;
    } catch (error) {
        document.getElementById("message").innerText = "Erro de conexão com o servidor.";
        console.error("Erro na requisição:", error);
    }
});

// Função para consultar reunião pelo título
async function consultarReuniaoPorTitulo() {
    const searchTitle = document.getElementById("search-title").value;

    if (!searchTitle) {
        alert("Por favor, insira o título para buscar.");
        return;
    }

    const encodedTitle = encodeURIComponent(searchTitle);

    try {
        const response = await fetch(`http://127.0.0.1:5000/get-meeting/${encodedTitle}`);
        const result = await response.json();

        const reunioesList = document.getElementById("reunioes-list");
        reunioesList.innerHTML = ""; // Limpa a lista antes de adicionar novas reuniões

        if (result.error) {
            reunioesList.innerHTML = `<p>${result.error}</p>`;
        } else {
            reunioesList.innerHTML += `
                <div class="meeting-item">
                    <h3>${result.title}</h3>
                    <p><strong>Data:</strong> ${result.date}</p>
                    <p><strong>Hora:</strong> ${result.time}</p>
                    <p><strong>Descrição:</strong> ${result.description}</p>
                </div>
            `;
        }
    } catch (error) {
        document.getElementById("reunioes-list").innerText = "Erro ao buscar reunião.";
        console.error("Erro na consulta:", error);
    }
}
