# 🚀 2º Ano - Semana 2: Flask - Criando API para o Chatbot

**Aulas 3-4:** Primeira API Flask + Testes com Postman  
**Duração:** 2 aulas (100 min)  
**Avaliação:** 1,5 pontos

---

## 🎯 Objetivos

- Criar primeira API com Flask
- Implementar rotas para o chatbot
- Testar APIs com Postman/Thunder Client
- Adaptar para o projeto do grupo

---

## 💻 AULA 3: Primeira API Flask

### Início (10 min)

**Setup Rápido:**

**Opção 1: Replit (Recomendado)**
```
1. Acesse replit.com
2. Create Repl → Python
3. Flask já vem instalado
4. Crie arquivo: main.py
```

**Opção 2: Computador Local**
```bash
pip install flask
pip install flask-cors
```

**Testar Instalação:**
```python
# teste.py
from flask import Flask
print("Flask instalado!")
```

### Meio (35 min)

**Código Inicial - Fazer Juntos (20 min)**

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# "Banco de dados" em memória
perguntas_respostas = [
    {
        "id": 1,
        "palavras_chave": ["laboratório", "lab", "onde fica"],
        "resposta": "O laboratório fica no 1º andar, sala 205"
    },
    {
        "id": 2,
        "palavras_chave": ["horário", "hora", "abre", "fecha"],
        "resposta": "Funcionamos de segunda a sexta, das 7h às 22h"
    }
]

# ===== ROTA 1: Página Inicial (Documentação) =====
@app.route('/')
def inicio():
    """Mostra endpoints disponíveis"""
    return jsonify({
        "mensagem": "API do Chatbot",
        "endpoints": {
            "GET /": "Esta página",
            "GET /respostas": "Lista todas respostas",
            "POST /perguntar": "Fazer uma pergunta",
            "POST /respostas": "Adicionar nova resposta"
        }
    })

# ===== ROTA 2: Listar Todas Respostas =====
@app.route('/respostas', methods=['GET'])
def listar_respostas():
    """Lista todas as perguntas e respostas cadastradas"""
    return jsonify(perguntas_respostas), 200

# ===== ROTA 3: Perguntar ao Bot =====
@app.route('/perguntar', methods=['POST'])
def perguntar():
    """Recebe pergunta e retorna resposta"""
    dados = request.json
    pergunta = dados.get('pergunta', '').lower()
    
    # Buscar resposta por palavras-chave
    for item in perguntas_respostas:
        for palavra in item['palavras_chave']:
            if palavra in pergunta:
                return jsonify({
                    'resposta': item['resposta'],
                    'encontrado': True
                }), 200
    
    # Nenhuma resposta encontrada
    return jsonify({
        'resposta': 'Desculpe, não entendi sua pergunta. Pode reformular?',
        'encontrado': False
    }), 200

# ===== ROTA 4: Adicionar Nova Resposta =====
@app.route('/respostas', methods=['POST'])
def adicionar_resposta():
    """Adiciona nova pergunta/resposta ao banco"""
    dados = request.json
    
    # Validação básica
    if 'palavras_chave' not in dados or 'resposta' not in dados:
        return jsonify({
            'erro': 'Campos obrigatórios: palavras_chave, resposta'
        }), 400
    
    nova_resposta = {
        'id': len(perguntas_respostas) + 1,
        'palavras_chave': dados['palavras_chave'],
        'resposta': dados['resposta']
    }
    
    perguntas_respostas.append(nova_resposta)
    
    return jsonify({
        'mensagem': 'Resposta adicionada com sucesso',
        'dados': nova_resposta
    }), 201

# ===== INICIAR SERVIDOR =====
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

**Explicação Passo a Passo:**

```
1. IMPORTS
   - Flask: framework principal
   - jsonify: converte Python dict → JSON
   - request: acessa dados da requisição

2. BANCO DE DADOS
   - Lista Python como "banco"
   - Estrutura: id, palavras_chave, resposta
   - Em memória (perde ao reiniciar)

3. ROTAS
   @app.route('/caminho', methods=['VERBO'])
   - Define URL e método HTTP
   - Função abaixo é executada

4. RETORNOS
   return jsonify(dados), status_code
   - Primeiro: corpo da resposta
   - Segundo: código HTTP (200, 201, 400, etc)
```

**Atividade em Grupo (15 min)**

```
ADAPTAR PARA SEU CHATBOT

1. Mudar perguntas_respostas para tema do grupo
   Mínimo 5 pares de pergunta/resposta

2. Testar no navegador:
   http://localhost:5000/
   
3. Verificar se JSON aparece

ENTREGAR ao final da aula:
□ Link do Replit funcionando
□ Print da rota "/" respondendo
□ Lista das 5 perguntas cadastradas

VALE 0,5 PONTOS
```

### Fim (5 min)

**Verificação:**
- Quantos grupos conseguiram rodar?
- Dúvidas comuns?
- Resolver problemas básicos

**Para próxima aula:**
- API funcionando
- Instalar Postman OU Thunder Client
- Trazer lista de mais perguntas

---

## 🧪 AULA 4: Testando APIs

### Início (10 min)

**Ferramentas de Teste:**

**Opção 1: Thunder Client (VS Code)**
```
1. Abrir VS Code
2. Extensions → "Thunder Client"
3. Instalar
4. Ícone ⚡ na barra lateral
```

**Opção 2: Postman**
```
1. Baixar: postman.com
2. Criar conta (gratuito)
3. New Request
```

**Opção 3: Online (Backup)**
```
httpie.io/app
- Sem instalar nada
- Direto no navegador
```

### Meio (35 min)

**Tutorial Postman/Thunder (20 min)**

**Teste 1: GET - Listar Respostas**
```
Método: GET
URL: http://localhost:5000/respostas

Botão: Send

✅ Deve retornar: lista com todas perguntas
✅ Status: 200 OK
```

**Teste 2: POST - Perguntar ao Bot**
```
Método: POST
URL: http://localhost:5000/perguntar

Headers:
  Content-Type: application/json

Body → raw → JSON:
{
  "pergunta": "onde fica o laboratório?"
}

Botão: Send

✅ Deve retornar: resposta do bot
✅ Status: 200 OK
```

**Teste 3: POST - Adicionar Resposta**
```
Método: POST
URL: http://localhost:5000/respostas

Body:
{
  "palavras_chave": ["wifi", "internet", "senha"],
  "resposta": "A senha do WiFi está no quadro de avisos"
}

Botão: Send

✅ Deve retornar: mensagem de sucesso
✅ Status: 201 Created
```

**Teste 4: Validação de Erro**
```
Método: POST
URL: http://localhost:5000/respostas

Body:
{
  "palavras_chave": ["teste"]
  // sem campo "resposta"
}

Botão: Send

✅ Deve retornar: mensagem de erro
✅ Status: 400 Bad Request
```

**Prática Individual (15 min)**

```
EXERCÍCIO: Testar Sua API

1. Fazer 3 testes GET
   - Listar respostas
   - Verificar dados retornados
   - Print do resultado

2. Fazer 5 testes POST /perguntar
   - Perguntas diferentes
   - Algumas que funcionam
   - Algumas que não funcionam
   - Anotar resultados

3. Adicionar 3 novas respostas via POST
   - Confirmar que foram adicionadas
   - Testar se funcionam

ENTREGAR:
□ Prints dos 3 testes principais
□ Lista das 3 respostas adicionadas
□ Observações sobre o que funcionou/não funcionou

VALE 1,0 PONTO
```

### Fim (5 min)

**Checklist de Entrega:**
```
□ API do chatbot rodando
□ Pelo menos 8 perguntas cadastradas
□ Testou com Postman/Thunder
□ Prints dos testes salvos
□ Link do Replit funcionando

Se falta algo: completar agora!
```

**Próxima Semana:**
- Integração com IA (Groq)
- Respostas mais inteligentes
- Chatbot de verdade

---

## 📊 Avaliação da Semana 2

**Total: 1,5 pontos**

| Atividade | Pontos |
|-----------|--------|
| API do chatbot funcionando (Aula 3) | 0,5 |
| Testes com Postman (Aula 4) | 1,0 |

**Critérios:**

**API Funcionando (0,5):**
- ✅ Roda sem erros: 0,3
- ✅ Pelo menos 5 respostas: 0,1
- ✅ Adaptado ao tema do grupo: 0,1

**Testes (1,0):**
- ✅ Testou todas rotas principais: 0,4
- ✅ Adicionou respostas novas: 0,3
- ✅ Documentou resultados: 0,3

---

## 🔧 Melhorias Opcionais

**Para Avançados:**

```python
# Busca mais inteligente
def buscar_resposta(pergunta):
    """Busca com score de relevância"""
    melhor_match = None
    maior_score = 0
    
    for item in perguntas_respostas:
        score = 0
        for palavra in item['palavras_chave']:
            if palavra in pergunta:
                score += 1
        
        if score > maior_score:
            maior_score = score
            melhor_match = item
    
    return melhor_match

# Tratamento de erros
@app.errorhandler(404)
def nao_encontrado(erro):
    return jsonify({'erro': 'Rota não encontrada'}), 404

@app.errorhandler(500)
def erro_servidor(erro):
    return jsonify({'erro': 'Erro interno do servidor'}), 500
```

---

## 💡 Problemas Comuns

**"ModuleNotFoundError: flask"**
```bash
Solução:
pip install flask
# ou
pip3 install flask
```

**"Address already in use"**
```python
Solução:
# Mudar porta
app.run(port=5001)  # ao invés de 5000
```

**"Can't connect to localhost"**
```
Soluções:
1. Verificar se API está rodando
2. Checar URL (http://localhost:5000)
3. Ver mensagens de erro no terminal
4. Usar 127.0.0.1:5000 ao invés de localhost
```

**"CORS Error"**
```python
Solução:
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # Adicionar esta linha
```

---

## 📚 Referências

**Documentação:**
- Flask: flask.palletsprojects.com
- Postman: learning.postman.com
- Thunder Client: thunderclient.com

**Tutoriais:**
- "Flask Básico" - Código Fonte TV
- "API REST com Flask" - Programador BR
- "Postman Tutorial" - FreeCodeCamp

---

## 🏠 Para Casa

**Preparar para Semana 3:**

1. **Melhorar API:**
   - Adicionar mais 10 perguntas
   - Testar exaustivamente
   - Corrigir erros

2. **Criar conta:**
   - groq.com (IA gratuita)
   - Guardar API key

3. **Estudar (opcional):**
   - O que são LLMs
   - Como funcionam ChatGPT/Claude
   - APIs de IA

**Próxima semana:**
Seu chatbot vai ficar inteligente! 🤖
