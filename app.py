import spacy
from flask import Flask, request, jsonify, send_from_directory
from pyswip import Prolog
from flask_cors import CORS

# Instância do app Flask
app = Flask(__name__)
CORS(app)

# Instância do Prolog
prolog = Prolog()

# Carrega o arquivo Prolog
try:
    prolog.consult("diagnostico.pl")
    print("Arquivo Prolog 'diagnostico.pl' carregado com sucesso.")
except Exception as e:
    print(f"Erro ao carregar o arquivo Prolog: {e}")

# Carregar modelo spaCy
nlp = spacy.load("pt_core_news_sm")

# Lista de sintomas conhecidos e mensagens amigáveis
mensagens_amigaveis = {
    "O motor está superaquecendo.": "O motor pode estar superaquecendo. Verifique o nível de água no radiador e consulte um mecânico.",
    "A ignição está fraca e as luzes do painel estão apagadas.": "A ignição fraca e as luzes apagadas podem indicar bateria descarregada. Verifique ou substitua a bateria.",
    "Há um ruído ao frear.": "O ruído ao frear pode ser causado por discos de freio desgastados. Leve o carro para revisão.",
    "O carro não acelera como deveria.": "O carro não está acelerando corretamente. Pode ser um problema de potência ou combustível contaminado.",
    "O motor está falhando ao ligar ou funcionado de maneira irregular.": "Falhas ao ligar o motor podem ser problemas de ignição ou bateria. Consulte um especialista.",
    "O indicador de temperatura está no vermelho.": "O indicador de temperatura no vermelho sugere superaquecimento. Verifique o sistema de arrefecimento imediatamente.",
    "Há um ruído estranho vindo do motor.": "Ruídos estranhos no motor podem indicar peças desgastadas. Consulte um mecânico."
}

# Função para mapear sintomas
def mapear_sintoma(sintoma_input):
    sintomas_conhecidos = {
        "O motor está superaquecendo.": ["motor superaquecendo", "luz vermelha com gota", "sai fumaca do motor", "motor muito quente", "motor com fumaca", "fumaça no motor"],
        "A ignição está fraca e as luzes do painel estão apagadas.": ["ignição fraca", "luz de bateria vermelha", "luzes fracas", "luzes apagadas"],
        "Há um ruído ao frear.": ["ruído ao frear", "discos de freio desgastados", "barulho no freio", "freio fazendo barulho", "ruido no freio", "ruido ao freiar"],
        "O carro não acelera como deveria.": ["carro não acelera", "carro nao acelera", "carro sem forca", "carro sem força", "carro fraco"],
        "O motor está falhando ao ligar ou funcionado de maneira irregular.": ["falha ao ligar", "ignição falhando", "carro nao liga", "carro não liga"],
        "O indicador de temperatura está no vermelho.": ["temperatura no vermelho", "motor aquecendo", "temperatura elevada"],
        "Há um ruído estranho vindo do motor.": ["ruído estranho no motor", "som estranho no motor", "som no motor", "barulho no motor"]
    }

    for descricao, termos in sintomas_conhecidos.items():
        for termo in termos:
            if termo in sintoma_input.lower():
                print(f"Sintoma mapeado: {descricao}")
                return descricao
    return None

@app.route('/')
def index():
    print("Requisição GET recebida na rota /")
    return send_from_directory('static', 'index.html')

@app.route('/diagnostico', methods=['POST'])
def diagnosticar():
    print("Requisição POST recebida na rota /diagnostico.")
    dados = request.json
    print(f"Dados recebidos: {dados}")
    
    sintoma_input = dados.get('sintoma')
    print(f"Sintoma recebido: {sintoma_input}")  # Verificando a entrada
    if not sintoma_input:
        print("Sintoma não fornecido.")
        return jsonify({"erro": "Sintoma não fornecido"}), 400

    try:
        print(f"Mapeando sintoma: {sintoma_input}")
        sintoma = mapear_sintoma(sintoma_input)
        if not sintoma:
            print(f"Não foi possível mapear o sintoma: {sintoma_input}")
            return jsonify({"erro": "Sintoma não reconhecido"}), 400

        # Consulta Prolog com a descrição completa
        resultado = list(prolog.query(f"diagnostico_causa(\"{sintoma}\", Problema, Causa)"))

        if resultado:
            problema = resultado[0]['Problema']
            causa = resultado[0]['Causa']
            
            if isinstance(causa, bytes):
                causa = causa.decode('utf-8')

            mensagem_amigavel = mensagens_amigaveis.get(sintoma, "Consulte um mecânico para diagnóstico completo.")
            print(f"Diagnóstico encontrado: Problema - {problema}, Causa - {causa}")
            return jsonify({
                "diagnostico": mensagem_amigavel,
                "causa": causa,
                "problema": problema
            }), 200
        else:
            print("Nenhum problema identificado.")
            return jsonify({"diagnostico": "Nenhum problema identificado para o sintoma fornecido"}), 404
    except Exception as e:
        print(f"Erro durante a consulta Prolog: {e}")
        return jsonify({"erro": "Erro interno ao processar a consulta"}), 500

if __name__ == '__main__':
    app.run(debug=True)
