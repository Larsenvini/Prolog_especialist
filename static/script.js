document.getElementById('diagnosticarBtn').addEventListener('click', async () => {
    const sintoma = document.getElementById('sintomaInput').value;

    if (!sintoma) {
        alert("Por favor, digite um sintoma.");
        return;
    }

    try {
        const response = await fetch('http://localhost:5000/diagnostico', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ sintoma }),

        });
        console.log("Enviando requisição POST...");


        const data = await response.json();
        document.getElementById('resultado').textContent = data.diagnostico || data.erro;
    } catch (error) {
        document.getElementById('resultado').textContent = "Erro ao tentar diagnosticar.";
    }
});