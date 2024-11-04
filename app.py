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

@app.route('/')
def index():
    print("Requisição GET recebida na rota /")
    return send_from_directory('static', 'index.html')

@app.route('/diagnostico', methods=['POST'])
def diagnosticar():
    print("Requisição POST recebida na rota /diagnostico.")
    dados = request.json
    print(f"Dados recebidos: {dados}")
    
    sintoma = dados.get('sintoma')
    if not sintoma:
        print("Sintoma não fornecido.")
        return jsonify({"erro": "Sintoma não fornecido"}), 400

    try:
        print(f"Consultando Prolog com o sintoma: {sintoma}")
        resultado = list(prolog.query(f"diagnostico_causa('{sintoma}', Problema, Causa)"))
        print(f"Resultado da consulta: {resultado}")

        if resultado:
            problema = resultado[0]['Problema']
            causa = resultado[0]['Causa']
            
            # Converte a causa para string se for do tipo bytes
            if isinstance(causa, bytes):
                causa = causa.decode('utf-8')
            
            print(f"Diagnóstico encontrado: Problema - {problema}, Causa - {causa}")
            return jsonify({
                "diagnostico": f"Problema identificado: {problema}",
                "causa": causa
            }), 200
        else:
            print("Nenhum problema identificado.")
            return jsonify({"diagnostico": "Nenhum problema identificado para o sintoma fornecido"}), 404
    except Exception as e:
        print(f"Erro durante a consulta Prolog: {e}")
        return jsonify({"erro": "Erro interno ao processar a consulta"}), 500


if __name__ == '__main__':
    app.run(debug=True)
