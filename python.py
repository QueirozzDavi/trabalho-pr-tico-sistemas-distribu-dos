from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Recebe os dados do corpo da requisição
    dados = request.json
    login = dados.get('login')
    senha = dados.get('senha')

    # Retorna os mesmos dados como resposta
    return jsonify({
        'login_recebido': login,
        'senha_recebida': senha
    })

if __name__ == '__main__':
    app.run(debug=True)
