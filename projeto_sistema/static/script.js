// Adicionar Reunião
async function adicionarReuniao() {
    const titulo = document.getElementById('titulo').value;
    const dataHora = document.getElementById('data_hora').value;
    
    const response = await fetch('/add_reuniao', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ titulo: titulo, data_hora: dataHora })
    });
    const result = await response.json();
    alert(result.status);
}

// Consultar Reuniões
async function consultarReunioes() {
    const response = await fetch('/consultar_reunioes');
    const reunioes = await response.json();
    const reunioesList = document.getElementById('reunioes-list');
    reunioesList.innerHTML = '';

    reunioes.forEach(reuniao => {
        const div = document.createElement('div');
        div.className = 'reuniao';
        div.innerHTML = `<h3>${reuniao[1]}</h3><p>${reuniao[2]}</p>`;
        reunioesList.appendChild(div);
    });
}

// Excluir Reunião (necessita id para exclusão)
async function excluirReuniao() {
    const id = prompt("Digite o ID da reunião a ser excluída:");
    const response = await fetch(`/excluir_reuniao?id=${id}`, { method: 'DELETE' });
    const result = await response.json();
    alert(result.status);
}
