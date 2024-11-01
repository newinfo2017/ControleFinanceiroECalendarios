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

// Função para consultar reuniões por período
async function consultarReunioesPorPeriodo() {
    const startDate = document.getElementById("start-date").value;
    const endDate = document.getElementById("end-date").value;

    if (!startDate || !endDate) {
        alert("Por favor, insira as datas de início e fim para buscar.");
        return;
    }

    try {
        const response = await fetch(`http://127.0.0.1:5000/get-meetings/${startDate}/${endDate}`);
        const meetings = await response.json();

        const reunioesList = document.getElementById("reunioes-list");
        reunioesList.innerHTML = ""; // Limpa a lista antes de adicionar novas reuniões

        if (meetings.length > 0) {
            meetings.forEach(meeting => {
                reunioesList.innerHTML += `
                    <div class="meeting-item">
                        <h3>${meeting.title}</h3>
                        <p><strong>Data:</strong> ${meeting.date}</p>
                        <p><strong>Hora:</strong> ${meeting.time}</p>
                        <p><strong>Descrição:</strong> ${meeting.description}</p>
                        <button class="alterar-btn" onclick="abrirFormularioAlterar('${meeting.id}', '${meeting.title}', '${meeting.date}', '${meeting.time}', '${meeting.description}')">Alterar</button>
                        <button class="excluir-btn" onclick="excluirReuniao('${meeting.id}')">Excluir</button>
                    </div>
                `;
            });
        } else {
            reunioesList.innerHTML = "<p>Nenhuma reunião encontrada para esse período.</p>";
        }
    } catch (error) {
        document.getElementById("reunioes-list").innerText = "Erro ao buscar reuniões.";
        console.error("Erro na consulta:", error);
    }
}

// Função para abrir o formulário de alteração com dados preenchidos
function abrirFormularioAlterar(id, title, date, time, description) {
    const reunioesList = document.getElementById("reunioes-list");
    reunioesList.innerHTML = `
        <h3>Alterar Reunião</h3>
        <form id="alterar-form">
            <label for="edit-title">Título da Reunião:</label>
            <input type="text" id="edit-title" value="${title}" required>
            
            <label for="edit-date">Data:</label>
            <input type="date" id="edit-date" value="${date}" required>

            <label for="edit-time">Hora:</label>
            <input type="time" id="edit-time" value="${time}" required>

            <label for="edit-description">Descrição:</label>
            <textarea id="edit-description" required>${description}</textarea>

            <button type="button" onclick="salvarAlteracoes(${id})">Salvar Alterações</button>
            <button type="button" onclick="consultarReunioesPorPeriodo()">Cancelar</button>
        </form>
    `;
}

// Função para salvar as alterações no backend
async function salvarAlteracoes(id) {
    const title = document.getElementById("edit-title").value;
    const date = document.getElementById("edit-date").value;
    const time = document.getElementById("edit-time").value;
    const description = document.getElementById("edit-description").value;

    try {
        const response = await fetch(`http://127.0.0.1:5000/update-meeting/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ title, date, time, description })
        });

        const result = await response.json();
        alert(result.message || "Reunião atualizada com sucesso.");
        
        // Recarrega a lista de reuniões após salvar alterações
        consultarReunioesPorPeriodo();
    } catch (error) {
        console.error("Erro ao salvar alterações:", error);
        alert("Erro ao atualizar a reunião.");
    }
}

// Função para excluir reunião
async function excluirReuniao(id) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/delete-meeting/${id}`, {
            method: "DELETE"
        });
        const result = await response.json();

        alert(result.message || "Reunião excluída com sucesso.");
        consultarReunioesPorPeriodo(); // Atualiza a lista após exclusão
    } catch (error) {
        console.error("Erro ao excluir reunião:", error);
        alert("Erro ao excluir a reunião.");
    }
}
