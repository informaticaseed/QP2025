from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de respostas (nosso "banco de dados")
respostas = [
    {"pergunta": "oi", "resposta": "Olá! Como posso ajudar?"},
    {"pergunta": "horário", "resposta": "Funcionamos de segunda a sexta, 7h-22h"},
    {"pergunta": "telefone", "resposta": "Nosso telefone: (11) 1234-5678"}
]

# Rota 1: Ver todas as respostas
@app.route('/ver')
def ver_todas():
    return jsonify(respostas)

# Rota 2: Perguntar ao bot
@app.route('/perguntar')
def perguntar():
    # Pega a pergunta da URL (?p=oi)
    pergunta = request.args.get('p', '').lower()

    # Busca a resposta
    for item in respostas:
        if item['pergunta'] in pergunta:
            return jsonify({"resposta": item['resposta']})

    return jsonify({"resposta": "Não entendi. Tente outra pergunta."})

# Rota 3: Adicionar resposta nova
@app.route('/adicionar')
def adicionar():
    nova_pergunta = request.args.get('p', '')
    nova_resposta = request.args.get('r', '')

    respostas.append({
        "pergunta": nova_pergunta,
        "resposta": nova_resposta
    })

    return jsonify({"mensagem": "Resposta adicionada!"})

# Iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)