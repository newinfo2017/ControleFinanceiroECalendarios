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

        if (response.ok) {
            const result = await response.json();
            document.getElementById("message").innerText = result.message;
        } else {
            document.getElementById("message").innerText = "Erro ao agendar a reunião. Tente novamente.";
        }
    } catch (error) {
        document.getElementById("message").innerText = "Erro de conexão com o servidor.";
    }
});