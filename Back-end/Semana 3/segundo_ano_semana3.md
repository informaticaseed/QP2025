# 🚀 2º Ano - Semana 3: Integração com IA (LLMs)

**Aulas 5-6:** Groq API + Prompt Engineering  
**Duração:** 2 aulas (100 min)  
**Avaliação:** 1,5 pontos

---

## 🎯 Objetivos

- Entender limitações do bot simples
- Integrar com Groq (LLM gratuito)
- Criar contexto personalizado
- Testar respostas inteligentes

---

## 🤖 AULA 5: Conectando com Groq

### Início (10 min)

**Por que usar IA?**

**Bot Simples (atual):**
```
Pergunta: "onde fica o lab?"
✅ Responde

Pergunta: "me fala onde está o laboratório"
❌ Não reconhece
```

**Bot com IA:**
```
Pergunta: "onde fica o lab?"
✅ Responde

Pergunta: "me fala onde está o laboratório"
✅ Responde (entende variações!)

Pergunta: "qual laboratório tem mais computadores?"
✅ Responde com contexto
```

**Vantagens da IA:**
- Entende sinônimos
- Interpreta intenção
- Respostas naturais
- Aprende contexto

**Groq - IA Gratuita:**
- Sem cartão de crédito
- API rápida
- Modelos potentes
- Fácil de usar

### Meio (35 min)

**Criar Conta Groq (5 min)**

```
1. Acesse: groq.com
2. Sign Up (email ou Google)
3. Console → API Keys
4. Create API Key
5. COPIAR e GUARDAR a chave
   (não vai mostrar de novo!)
```

**Código de Integração (30 min)**

```python
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ===== CONFIGURAÇÃO GROQ =====
GROQ_API_KEY = 'gsk_...'  # COLE SUA CHAVE AQUI
GROQ_URL = 'https://api.groq.com/openai/v1/chat/completions'

# ===== CONTEXTO DO BOT =====
CONTEXTO = """
Você é um assistente virtual da Escola TechFlow.

INFORMAÇÕES IMPORTANTES:
- Horário: Segunda a sexta, 7h às 22h
- Laboratórios: 1º andar, salas 201-205
  * Lab Redes: sala 201
  * Lab Hardware: sala 202  
  * Lab Programação: salas 203-205
- Secretaria: térreo, sala 101
- Biblioteca: 2º andar, funcionamento 8h-20h

REGRAS:
1. Seja breve e direto
2. Use linguagem amigável e informal
3. Se não souber, admita e sugira procurar secretaria
4. Use emojis ocasionalmente
5. Sempre termine perguntando se pode ajudar em mais algo

EXEMPLOS:
Pergunta: onde fica o lab de redes?
Resposta: O laboratório de redes fica na sala 201, no 1º andar! 💻

Pergunta: vocês abrem no sábado?
Resposta: Não abrimos aos sábados. Funcionamos de segunda a sexta, das 7h às 22h. 📅

Pergunta: preciso falar com alguém
Resposta: Você pode ir na secretaria, sala 101 no térreo. Eles te ajudam! 😊
"""

# ===== ROTA: Chat com IA =====
@app.route('/chat', methods=['POST'])
def chat_ia():
    dados = request.json
    pergunta = dados.get('mensagem')
    
    if not pergunta:
        return jsonify({'erro': 'Mensagem não fornecida'}), 400
    
    # Montar payload para Groq
    payload = {
        "model": "mixtral-8x7b-32768",  # Modelo gratuito
        "messages": [
            {
                "role": "system",
                "content": CONTEXTO
            },
            {
                "role": "user",
                "content": pergunta
            }
        ],
        "temperature": 0.7,    # Criatividade (0-2)
        "max_tokens": 200,     # Tamanho da resposta
        "top_p": 1,
        "stream": False
    }
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        # Fazer requisição para Groq
        resposta = requests.post(
            GROQ_URL,
            json=payload,
            headers=headers,
            timeout=10
        )
        
        if resposta.status_code == 200:
            resultado = resposta.json()
            mensagem_ia = resultado['choices'][0]['message']['content']
            
            return jsonify({
                'resposta': mensagem_ia,
                'status': 'sucesso'
            }), 200
        else:
            return jsonify({
                'erro': 'IA não respondeu',
                'status_code': resposta.status_code,
                'detalhes': resposta.text
            }), resposta.status_code
            
    except requests.exceptions.Timeout:
        return jsonify({
            'erro': 'Timeout - IA demorou muito para responder'
        }), 504
        
    except Exception as e:
        return jsonify({
            'erro': f'Erro ao conectar com IA: {str(e)}'
        }), 500

# ===== ROTA: Teste =====
@app.route('/teste', methods=['GET'])
def teste():
    return jsonify({
        'status': 'API funcionando',
        'groq_configurado': bool(GROQ_API_KEY and GROQ_API_KEY != 'gsk_...')
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

**Testar no Postman:**

```
POST http://localhost:5000/chat

Body:
{
  "mensagem": "onde fica o laboratório?"
}

✅ Deve retornar: resposta natural da IA
✅ Status: 200
```

**Atividade em Grupo (5 min antes do fim):**

```
TESTAR INTEGRAÇÃO COM IA

1. Adicionar sua API key do Groq
2. Adaptar CONTEXTO para tema do grupo
3. Testar 3 perguntas diferentes
4. Anotar as respostas

VALE 0,5 PONTOS - Entregar Semana 4
(faz parte do projeto completo)
```

### Fim (5 min)

**Verificar:**
- Quantos conseguiram rodar?
- Dúvidas sobre API key?
- Respostas fazem sentido?

**Para próxima aula:**
- API com Groq funcionando
- Pensar em mais informações para contexto
- Testar bastante

---

## 📝 AULA 6: Prompt Engineering

### Início (10 min)

**O que é Prompt Engineering?**

```
Prompt = Instruções que você dá para IA
Engineering = Otimizar para melhores resultados
```

**Exemplo:**

**Prompt Ruim:**
```
"Você é um bot"
```
Resultado: Respostas genéricas

**Prompt Bom:**
```
"Você é assistente da Escola X.
Seja breve, amigável, use emojis.
Informações: [lista detalhada]
Exemplos: [casos de uso]"
```
Resultado: Respostas específicas e úteis

### Meio (35 min)

**Técnicas de Prompt Engineering (20 min)**

**1. Contexto Rico**

```python
# ❌ Contexto fraco
CONTEXTO = "Você é um assistente de escola"

# ✅ Contexto rico
CONTEXTO = """
Você é o EduBot, assistente virtual da Escola TechFlow.

IDENTIDADE:
- Nome: EduBot
- Função: Auxiliar alunos com dúvidas sobre a escola
- Tom: Amigável, informal mas educado

CONHECIMENTO:
Horários:
- Segunda a sexta: 7h-22h
- Sábado: Fechado
- Domingo: Fechado
- Feriados: Consultar site

Localização - Laboratórios (1º andar):
- Sala 201: Lab de Redes (20 computadores)
- Sala 202: Lab de Hardware (15 bancadas)
- Salas 203-205: Labs de Programação (30 computadores cada)
- Horário labs: 7h-21h
- Responsável: Prof. Silva

Secretaria (térreo):
- Sala 101
- Horário: 8h-18h
- Telefone: (61) 3333-4444
- Email: secretaria@techflow.edu.br
- Serviços: matrículas, declarações, históricos

REGRAS DE COMPORTAMENTO:
1. Respostas curtas (máximo 3 linhas)
2. Use emojis com moderação (1-2 por resposta)
3. Se não souber: admitir e sugerir contato com secretaria
4. Sempre perguntar se pode ajudar em mais algo
5. Não inventar informações

EXEMPLOS DE RESPOSTAS:
Q: "onde fica o lab de redes?"
A: "O laboratório de redes fica na sala 201, no 1º andar! 💻 Tem 20 computadores disponíveis. Posso te ajudar com mais alguma coisa?"

Q: "vocês abrem no sábado?"
A: "Não, a escola funciona apenas de segunda a sexta, das 7h às 22h. 📅"

Q: "preciso de histórico escolar"
A: "Para pegar histórico, vai na secretaria (sala 101, térreo) entre 8h-18h. 📋 Ou liga: (61) 3333-4444"
"""
```

**2. Parâmetros de Configuração**

```python
payload = {
    "model": "mixtral-8x7b-32768",
    "messages": [...],
    
    # TEMPERATURA (0-2)
    # Quanto maior, mais criativo/aleatório
    "temperature": 0.7,  # Recomendado: 0.5-0.9
    # 0.3 = muito preciso, robótico
    # 0.7 = balanceado (IDEAL)
    # 1.5 = muito criativo, pode inventar
    
    # MAX TOKENS (tamanho)
    "max_tokens": 200,   # Recomendado: 150-300
    # 50 = muito curto
    # 200 = ideal para chatbot
    # 500 = respostas longas
    
    # TOP_P (diversidade)
    "top_p": 1,          # Deixar em 1
}
```

**3. Histórico de Conversa**

```python
# Lista para guardar histórico
historico = []

@app.route('/chat', methods=['POST'])
def chat_ia():
    global historico
    
    dados = request.json
    mensagem = dados.get('mensagem')
    
    # Adicionar mensagem do usuário
    historico.append({
        "role": "user",
        "content": mensagem
    })
    
    # Manter apenas últimas 10 mensagens (memória limitada)
    if len(historico) > 10:
        historico = historico[-10:]
    
    # Montar mensagens: sistema + histórico
    mensagens_completas = [
        {"role": "system", "content": CONTEXTO}
    ] + historico
    
    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": mensagens_completas,  # Enviar tudo
        "temperature": 0.7,
        "max_tokens": 200
    }
    
    # ... fazer requisição
    
    # Adicionar resposta da IA ao histórico
    if resposta_ia:
        historico.append({
            "role": "assistant",
            "content": resposta_ia
        })
    
    return jsonify({'resposta': resposta_ia})
```

**Atividade em Grupo (15 min)**

```
PERSONALIZAR SEU BOT

1. Criar contexto DETALHADO (10 min)
   - Mínimo 20 informações específicas
   - 8 exemplos de perguntas/respostas
   - Definir personalidade clara
   - Tom de voz específico

2. Testar e ajustar (5 min)
   - Fazer 10 perguntas variadas
   - Anotar o que funcionou bem
   - Anotar o que precisa melhorar
   - Ajustar contexto

DOCUMENTAR:
□ Contexto completo usado
□ 5 melhores respostas obtidas
□ 3 pontos a melhorar

VALE 1,0 PONTO - Entregar Semana 4
(faz parte do projeto completo)
```

### Fim (5 min)

**Compartilhar:**
- 2-3 grupos mostram melhores respostas
- Dicas que funcionaram
- Problemas encontrados

**Próxima Semana:**
- Conectar front-end (Loveable) com back-end
- Sistema completo funcionando
- Apresentações

---

## 📊 Avaliação da Semana 3

**Total: 1,5 pontos**

| Atividade | Pontos |
|-----------|--------|
| Integração com Groq (Aula 5) | 0,5 |
| Contexto personalizado (Aula 6) | 1,0 |

**Obs:** Entrega na Semana 4 como parte do projeto completo

**Critérios:**

**Integração (0,5):**
- ✅ API conecta com Groq
- ✅ Respostas funcionam
- ✅ Tratamento de erros

**Contexto (1,0):**
- ✅ Mínimo 20 informações: 0,4
- ✅ 8 exemplos claros: 0,3
- ✅ Personalidade definida: 0,3

---

## 🔧 Problemas Comuns

**"Invalid API Key"**
```
Soluções:
1. Verificar se copiou chave completa
2. Criar nova chave no Groq
3. Verificar se tem "gsk_" no início
```

**"Rate Limit Exceeded"**
```
Problema: Muitas requisições
Solução: Aguardar 1 minuto
         Criar conta nova se necessário
```

**"Timeout"**
```
Solução:
# Aumentar timeout
resposta = requests.post(
    GROQ_URL,
    json=payload,
    headers=headers,
    timeout=30  # ao invés de 10
)
```

**"IA responde errado"**
```
Soluções:
1. Melhorar contexto (mais específico)
2. Adicionar mais exemplos
3. Ajustar temperatura (0.5-0.7)
4. Especificar formato de resposta
```

---

## 💡 Dicas de Prompt Engineering

**Para Respostas Melhores:**

```python
# ✅ Seja específico
"Responda em até 2 frases"
"Use emojis: 💻 📚 📅"
"Tom amigável, como um colega"

# ✅ Dê exemplos
"Exemplo de resposta boa: [...]"
"NÃO faça isso: [...]"

# ✅ Defina limites
"Se não souber, diga: 'Não tenho essa informação'"
"Nunca invente dados ou números"

# ✅ Estruture o contexto
IDENTIDADE: quem é o bot
CONHECIMENTO: o que ele sabe
REGRAS: como deve se comportar
EXEMPLOS: como deve responder
```

---

## 📚 Recursos

**Groq:**
- groq.com/docs
- console.groq.com

**Prompt Engineering:**
- "Prompt Engineering Guide" - GitHub
- "Best Practices for Prompts" - OpenAI

**Vídeos:**
- "O que são LLMs" - Código Fonte TV
- "Como funciona ChatGPT" - Programador BR

---

## 🏠 Para Casa

**Finalizar para Semana 4:**

1. **Contexto Perfeito:**
   - Mínimo 20 informações
   - Tom bem definido
   - Exemplos variados

2. **Testar Muito:**
   - 20+ perguntas diferentes
   - Anotar problemas
   - Ajustar contexto

3. **Preparar:**
   - API funcionando 100%
   - Saber explicar como funciona
   - Ter backup da API key

**Próxima Semana:**
Conectar tudo e apresentar! 🎉
