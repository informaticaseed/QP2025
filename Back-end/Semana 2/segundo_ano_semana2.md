# 🚀 2º Ano - Semana 2: API REST - CRUD Completo

**Aulas 3-4:** Criar API com todos os métodos HTTP
**Duração:** 2 aulas (100 min)
**Avaliação:** 1,5 pontos

---

## 🎯 Essência do Back-end

**API = Servidor que responde requisições**

Verbos HTTP (o que você quer fazer):
- **GET** → Buscar/Ler dados
- **POST** → Criar dados novos
- **PUT** → Atualizar dados completos
- **PATCH** → Atualizar parte dos dados
- **DELETE** → Apagar dados

---

## 💻 AULA 3: CRUD Completo

### Início (5 min)

**Setup:**
```
1. Crie pasta: api_produtos
2. Crie arquivo: app.py
3. Terminal: pip install flask
4. Execute: python app.py
```

### Meio (40 min)

**Código Completo - API de Produtos:**

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Banco de dados (lista em memória)
produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3000, "estoque": 5},
    {"id": 2, "nome": "Mouse", "preco": 50, "estoque": 20},
    {"id": 3, "nome": "Teclado", "preco": 150, "estoque": 15}
]

# GET - Listar todos os produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos)

# GET - Buscar um produto específico
@app.route('/produtos/<int:id>', methods=['GET'])
def buscar_produto(id):
    produto = next((p for p in produtos if p['id'] == id), None)
    if produto:
        return jsonify(produto)
    return jsonify({"erro": "Produto não encontrado"}), 404

# POST - Criar novo produto
@app.route('/produtos', methods=['POST'])
def criar_produto():
    novo = request.json
    novo['id'] = max([p['id'] for p in produtos]) + 1
    produtos.append(novo)
    return jsonify(novo), 201

# PUT - Atualizar produto completo
@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_completo(id):
    produto = next((p for p in produtos if p['id'] == id), None)
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404

    dados = request.json
    produto['nome'] = dados.get('nome', produto['nome'])
    produto['preco'] = dados.get('preco', produto['preco'])
    produto['estoque'] = dados.get('estoque', produto['estoque'])

    return jsonify(produto)

# PATCH - Atualizar apenas parte do produto
@app.route('/produtos/<int:id>', methods=['PATCH'])
def atualizar_parcial(id):
    produto = next((p for p in produtos if p['id'] == id), None)
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404

    dados = request.json
    if 'nome' in dados:
        produto['nome'] = dados['nome']
    if 'preco' in dados:
        produto['preco'] = dados['preco']
    if 'estoque' in dados:
        produto['estoque'] = dados['estoque']

    return jsonify(produto)

# DELETE - Remover produto
@app.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    global produtos
    produto = next((p for p in produtos if p['id'] == id), None)
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404

    produtos = [p for p in produtos if p['id'] != id]
    return jsonify({"mensagem": "Produto deletado"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

**Resumo:**
```
GET /produtos           → Lista todos
GET /produtos/1         → Busca produto ID 1
POST /produtos          → Cria novo
PUT /produtos/1         → Atualiza tudo do ID 1
PATCH /produtos/1       → Atualiza só parte do ID 1
DELETE /produtos/1      → Deleta ID 1
```

### Fim (5 min)

**Teste rápido:**
```
Navegador: http://127.0.0.1:5000/produtos
✅ Deve mostrar os 3 produtos
```

**Para próxima aula:**
Instalar ferramenta para testar POST, PUT, PATCH, DELETE

---

## 🧪 AULA 4: Testando todos os métodos

### Início (10 min)

**Instalar Thunder Client (VS Code) ou Postman:**

**Opção 1 - Thunder Client (mais leve):**
```
VS Code → Extensions → "Thunder Client" → Install
```

**Opção 2 - Postman:**
```
postman.com/downloads → Instalar
```

### Meio (30 min)

**TESTES - Fazer junto com o professor:**

**1. GET - Listar todos**
```
Método: GET
URL: http://127.0.0.1:5000/produtos
```

**2. GET - Buscar um específico**
```
Método: GET
URL: http://127.0.0.1:5000/produtos/1
```

**3. POST - Criar novo**
```
Método: POST
URL: http://127.0.0.1:5000/produtos
Body (JSON):
{
  "nome": "Monitor",
  "preco": 800,
  "estoque": 10
}
```

**4. PUT - Atualizar completo**
```
Método: PUT
URL: http://127.0.0.1:5000/produtos/1
Body (JSON):
{
  "nome": "Notebook Gamer",
  "preco": 5000,
  "estoque": 3
}
```

**5. PATCH - Atualizar só o preço**
```
Método: PATCH
URL: http://127.0.0.1:5000/produtos/1
Body (JSON):
{
  "preco": 2800
}
```

**6. DELETE - Remover produto**
```
Método: DELETE
URL: http://127.0.0.1:5000/produtos/2
```

### ATIVIDADE (10 min)

**DESAFIO: Criar API de outro tema**

Adapte o código para um destes temas:
- **Alunos:** id, nome, turma, nota
- **Livros:** id, titulo, autor, ano
- **Filmes:** id, titulo, genero, duracao
- **Tarefas:** id, titulo, concluida, prioridade

**Requisitos:**
1. Implementar todas as rotas (GET, POST, PUT, PATCH, DELETE)
2. Testar todas as operações
3. Ter pelo menos 3 itens no banco inicial

**ENTREGA (Vale 1,5 pontos):**
```
□ Código da API funcionando
□ Prints de todos os 6 testes
□ Arquivo .py enviado
```

---

## 📊 Avaliação

**Total: 1,5 pontos**

| Critério | Pontos |
|----------|--------|
| API completa funcionando (todas as rotas) | 0,6 |
| Testes corretos (6 prints) | 0,6 |
| Código limpo e organizado | 0,3 |

---

## 💡 Problemas Comuns

**"ModuleNotFoundError: flask"**
```bash
pip install flask
```

**"Porta já em uso"**
```python
app.run(debug=True, port=5001)  # Troque a porta
```

**"405 Method Not Allowed"**
```
Verifique se está usando o método HTTP correto
POST/PUT/PATCH/DELETE não funcionam no navegador
Use Thunder Client ou Postman
```

**Erro no DELETE:**
```python
# Adicione 'global produtos' no início da função
global produtos
produtos = [p for p in produtos if p['id'] != id]
```

---

## 🏠 Para Casa

**Estudar para próxima semana:**
- Conectar API com banco de dados (SQLite)
- Autenticação com JWT
- Deploy da API na internet

**Desafio extra (opcional):**
Adicionar rota de busca:
```python
@app.route('/produtos/buscar', methods=['GET'])
def buscar_por_nome():
    nome = request.args.get('nome', '')
    resultado = [p for p in produtos if nome.lower() in p['nome'].lower()]
    return jsonify(resultado)
```
