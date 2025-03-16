from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Recebe os dados do corpo da requisição
    dados = request.json
    
    # Verifica se o login e a senha foram fornecidos
    if 'login' not in dados or 'senha' not in dados:
        return jsonify({"erro": "Login e senha são obrigatórios"}), 400
    
    # Extrai o login e a senha
    login = dados['login']
    senha = dados['senha']
    
    # Retorna os dados recebidos como resposta
    return jsonify({"login": login, "senha": senha}), 200

if __name__ == '__main__':
    # Inicia o servidor na porta 5000
    app.run(host='0.0.0.0', port=5000)
