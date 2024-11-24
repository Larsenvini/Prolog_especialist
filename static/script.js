document.getElementById('diagnosticarBtn').addEventListener('click', async () => {
    const sintoma = document.getElementById('sintomaInput').value.trim(); // Remove espaços extras

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

        if (!response.ok) {
            throw new Error(`Erro: ${response.status} - ${response.statusText}`);
        }

        const data = await response.json();
        document.getElementById('resultado').textContent = data.diagnostico || data.erro;

        // Ajustando o modo como o problema é extraído, considerando a chave correta.
        const problema = data.problema ? data.problema.toLowerCase().replace(/ /g, "_") : ''; // A chave do problema com underscores
        console.log(problema);
        
        const imagemDiv = document.getElementById('imagemProblema');
        exibirImagemProblema(problema, imagemDiv); // Chama função modular para exibir a imagem
    } catch (error) {
        console.error("Erro ao diagnosticar:", error);
        document.getElementById('resultado').textContent = "Erro ao tentar diagnosticar.";
    }
});

// Função para mapear problemas a imagens e exibi-las
function exibirImagemProblema(problema, imagemDiv) {
    const imagens = {
        "bateria_fraca": "/static/imagens/bateria_fraca.jpg",
        "falta_de_oleo": "/static/imagens/falta_de_oleo.jpg",
        "disco_freio_desgastado": "/static/imagens/disco_freio_desgastado.jpg",
        "perda_de_potencia": "/static/imagens/perda_de_potencia.jpg",
        "falha_de_ignicao": "/static/imagens/falha_de_ignicao.jpg",
        "aquecimento_motor": "/static/imagens/aquecimento_motor.jpg",
        "ruido_motor": "/static/imagens/ruido_motor.jpg"
    };
    
    if (imagens[problema]) {
        imagemDiv.innerHTML = `<img src="${imagens[problema]}" alt="${problema}" style="max-width: 100%; height: auto;">`;
    } else {
        imagemDiv.innerHTML = '<img src="/static/imagens/ruido_motor.jpg">'; // Imagem padrão caso não tenha match
    }
}
