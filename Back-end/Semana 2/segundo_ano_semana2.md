# 🚀 2º Ano - Semana 2: Minha Primeira API

**Aulas 3-4:** Criar API Flask do zero
**Duração:** 2 aulas (100 min)
**Avaliação:** 1,5 pontos

---

## 🎯 O que vamos fazer?

Criar uma API (servidor) que responde perguntas automaticamente.

**Essência do Back-end:**
- Receber dados (pergunta)
- Processar (buscar resposta)
- Retornar resultado (resposta)

---

## 💻 AULA 3: Criando a API

### Início (10 min)

**ESCOLHA UMA OPÇÃO:**

**Opção A: Google Colab (Mais simples - Recomendado)**
```
1. Acesse: colab.research.google.com
2. Novo notebook
3. Cole o código
4. Clique em ▶️ Executar
5. Nenhuma instalação necessária!
```

**Opção B: Python.org (Se tiver Python instalado)**
```
1. Crie pasta: chatbot_api
2. Crie arquivo: app.py
3. Abra terminal nesta pasta
4. Execute: pip install flask
```

**Opção C: VS Code com Python**
```
1. Crie arquivo: app.py
2. Terminal: pip install flask
3. Execute: python app.py
```

### Meio (35 min)

**Código Completo - Digite junto com o professor:**

```python
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
```

**O que cada parte faz:**

```
1. LISTA DE RESPOSTAS
   - Guarda perguntas e respostas
   - Como uma lista de contatos no celular

2. ROTAS (URLs que a API responde)
   /ver → mostra todas respostas
   /perguntar?p=oi → faz uma pergunta
   /adicionar?p=pergunta&r=resposta → adiciona nova resposta

3. COMO FUNCIONA
   - Recebe pergunta pela URL
   - Procura na lista
   - Retorna resposta em JSON
```

**Testando no navegador (15 min):**

```
DEPOIS DE EXECUTAR O CÓDIGO:

1. Abra o navegador
2. Acesse: http://127.0.0.1:5000/ver
   ✅ Deve mostrar todas as respostas

3. Teste fazer pergunta:
   http://127.0.0.1:5000/perguntar?p=oi
   ✅ Deve responder "Olá! Como posso ajudar?"

4. Teste adicionar:
   http://127.0.0.1:5000/adicionar?p=email&r=contato@escola.com
   ✅ Depois teste /ver de novo

5. PRÁTICA:
   - Adicione 5 perguntas do seu tema
   - Teste se funcionam
   - Tire print das respostas
```

**ENTREGA (Vale 0,5 pontos):**
```
□ Código rodando
□ 5 perguntas do tema do grupo funcionando
□ Print da rota /ver mostrando suas perguntas
```

### Fim (5 min)

**Checklist:**
- [ ] Conseguiu rodar o código?
- [ ] Entendeu como funciona?
- [ ] Conseguiu adicionar perguntas?

**Para próxima aula:**
- Vamos testar de forma profissional (direto no navegador, sem instalar nada)

---

## 🧪 AULA 4: Testando como profissional

### Início (10 min)

**Vamos testar só usando o NAVEGADOR!**

Nenhuma instalação necessária. Só precisa:
1. Sua API rodando (do código da aula 3)
2. Navegador aberto

**Conceito importante:**
```
GET = pedir informação (como entrar num site)
POST = enviar informação (não dá pra fazer só no navegador)
```

Como só usamos GET na nossa API, o navegador funciona perfeitamente!

### Meio (35 min)

**TESTES PRÁTICOS (Fazer junto)**

**Teste 1: Ver todas respostas**
```
URL: http://127.0.0.1:5000/ver

✅ Mostra lista completa
```

**Teste 2: Fazer 5 perguntas diferentes**
```
http://127.0.0.1:5000/perguntar?p=oi
http://127.0.0.1:5000/perguntar?p=horário
http://127.0.0.1:5000/perguntar?p=telefone
http://127.0.0.1:5000/perguntar?p=email
http://127.0.0.1:5000/perguntar?p=endereço

✅ Cada uma deve retornar resposta diferente
❌ Se não achar, retorna "Não entendi"
```

**Teste 3: Adicionar 3 respostas novas**
```
http://127.0.0.1:5000/adicionar?p=endereço&r=Rua ABC, 123
http://127.0.0.1:5000/adicionar?p=email&r=contato@escola.com
http://127.0.0.1:5000/adicionar?p=whatsapp&r=(11) 99999-9999

Depois: acesse /ver para confirmar que foram adicionadas!
```

**ATIVIDADE INDIVIDUAL (20 min)**

```
MISSÃO: Criar chatbot do seu tema

1. Adicionar 10 perguntas úteis sobre seu tema
   Exemplos de temas:
   - Escola: matérias, professores, horários
   - Loja: produtos, preços, formas de pagamento
   - Restaurante: cardápio, horário, delivery

2. Testar TODAS as perguntas

3. Tirar prints de:
   - /ver com todas as 10 perguntas
   - 3 perguntas sendo respondidas corretamente
   - 1 pergunta que não tem resposta

VALE 1,0 PONTO
```

### Fim (5 min)

**ENTREGA FINAL:**
```
□ 10 perguntas cadastradas
□ Prints dos testes
□ Tudo funcionando
```

**Próxima semana:**
Adicionar inteligência artificial de verdade (ChatGPT/Groq) no seu chatbot!

---

## 📊 Avaliação

**Total: 1,5 pontos**

| Atividade | Pontos |
|-----------|--------|
| API funcionando com 5 perguntas (Aula 3) | 0,5 |
| 10 perguntas testadas (Aula 4) | 1,0 |

---

## 💡 Se der erro

**"ModuleNotFoundError: flask"**
```bash
pip install flask
```

**"Porta já em uso"**
```python
# Mude a última linha para:
app.run(debug=True, port=5001)
```

**"Não consegue acessar no navegador"**
```
1. Veja se o código está rodando (sem erros no terminal)
2. Use: http://127.0.0.1:5000/ver
3. Não use "localhost", use "127.0.0.1"
```

---

## 🏠 Para Casa

**Preparar para Semana 3:**

1. Sua API funcionando com 10+ perguntas
2. Criar conta em: console.groq.com
3. Guardar a chave de API do Groq

**Próxima semana:**
Adicionar IA de verdade no chatbot!
