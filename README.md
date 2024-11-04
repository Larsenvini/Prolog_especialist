# Diagnóstico Automotivo com Flask e Prolog

Este é um projeto de diagnóstico automotivo que utiliza um aplicativo Flask para se comunicar com um sistema de regras em Prolog. O usuário pode inserir sintomas relacionados a problemas automotivos e receber um diagnóstico potencial.

## Estrutura do Projeto
- `app.py`: Código do aplicativo Flask.
- `diagnostico.pl`: Base de conhecimento em Prolog com sintomas e causas.
- `index.html`: Interface HTML para o usuário.
- `styles.css`: Arquivo de estilos para a página.
- `script.js`: Código JavaScript para interação com a página.
- `requirements.txt`: Lista de dependências do projeto.

## Como Executar o Projeto Localmente

### 1. Clonar o Repositório
Clone o repositório do projeto para sua máquina local com o seguinte comando:
bash
git clone <URL_DO_REPOSITORIO>
cd <PASTA_DO_PROJETO>

## 2. Criar um Ambiente Virtual (Opcional, mas Recomendado)
Crie um ambiente virtual para manter as dependências isoladas:
bash
python -m venv venv

No macOS/Linux:
source venv/bin/activate

No Windows:
venv\Scripts\activate

## 3. Instalar Dependências
Instale todas as bibliotecas necessárias listadas em requirements.txt:
pip install -r requirements.txt

## 4. Executar o Aplicativo Flask
Inicie o servidor Flask com o comando:
python app.py

## 5. Acessar a Aplicação
Abra o navegador e acesse:
http://127.0.0.1:5000
