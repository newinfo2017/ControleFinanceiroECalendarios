// Conexão com IndexedDB
let db;
const request = indexedDB.open('agendaReunioesDB', 1);

request.onupgradeneeded = function(event) {
    db = event.target.result;
    const objectStore = db.createObjectStore('reunioes', { keyPath: 'id', autoIncrement: true });
    objectStore.createIndex('titulo', 'titulo', { unique: false });
    objectStore.createIndex('data_hora', 'data_hora', { unique: false });
};

request.onsuccess = function(event) {
    db = event.target.result;
};

request.onerror = function(event) {
    console.log('Erro ao abrir o banco de dados:', event.target.errorCode);
};

// Adicionar Reunião
function adicionarReuniao() {
    const titulo = document.getElementById('titulo').value;
    const dataHora = document.getElementById('data_hora').value;

    const transaction = db.transaction(['reunioes'], 'readwrite');
    const store = transaction.objectStore('reunioes');
    const novaReuniao = { titulo: titulo, data_hora: dataHora };
    const request = store.add(novaReuniao);

    request.onsuccess = function() {
        alert('Reunião adicionada com sucesso!');
        consultarReunioes();
    };

    request.onerror = function() {
        alert('Erro ao adicionar reunião.');
    };
}

// Consultar Reuniões
function consultarReunioes() {
    const transaction = db.transaction(['reunioes'], 'readonly');
    const store = transaction.objectStore('reunioes');
    const request = store.openCursor();
    const reunioesList = document.getElementById('reunioes-list');
    reunioesList.innerHTML = '';

    request.onsuccess = function(event) {
        const cursor = event.target.result;
        if (cursor) {
            const reuniao = cursor.value;
            const div = document.createElement('div');
            div.className = 'reuniao';
            div.innerHTML = `
                <div>
                    <h3>${reuniao.titulo}</h3>
                    <p>${reuniao.data_hora}</p>
                </div>
                <div>
                    <button onclick="excluirReuniao(${reuniao.id})">Excluir</button>
                    <button onclick="alterarReuniao(${reuniao.id})">Alterar</button>
                </div>
            `;
            reunioesList.appendChild(div);
            cursor.continue();
        }
    };
}

// Excluir Reunião
function excluirReuniao(id) {
    const transaction = db.transaction(['reunioes'], 'readwrite');
    const store = transaction.objectStore('reunioes');
    const request = store.delete(id);

    request.onsuccess = function() {
        alert('Reunião excluída com sucesso!');
        consultarReunioes();
    };
    request.onerror = function() {
        alert('Erro ao excluir reunião.');
    };
}

// Alterar Reunião
function alterarReuniao(id) {
    const novoTitulo = prompt('Digite o novo título da reunião:');
    const novaDataHora = prompt('Digite a nova data e hora (AAAA-MM-DDTHH:MM):');

    const transaction = db.transaction(['reunioes'], 'readwrite');
    const store = transaction.objectStore('reunioes');
    const request = store.get(id);

    request.onsuccess = function() {
        const reuniao = request.result;
        reuniao.titulo = novoTitulo;
        reuniao.data_hora = novaDataHora;

        const requestUpdate = store.put(reuniao);
        requestUpdate.onsuccess = function() {
            alert('Reunião alterada com sucesso!');
            consultarReunioes();
        };
    };
    request.onerror = function() {
        alert('Erro ao alterar reunião.');
    };
}
