from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite que o front-end acesse o back-end

@app.route('/api/mensagem', methods=['POST'])
def mensagem():
    dados = request.get_json()
    nome = dados.get('nome')
    resposta = f"Olá, {nome}! Esta resposta veio do back-end Python."
    return jsonify({'resposta': resposta})

if __name__ == '__main__':
    app.run(debug=True)
