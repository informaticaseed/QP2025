# 🚀 2º Ano - Semana 4: Integração Completa e Apresentação

**Aulas 7-8:** Front+Back Conectados + Apresentações  
**Duração:** 2 aulas (100 min)  
**Avaliação:** 6,0 pontos

---

## 🎯 Objetivos

- Conectar front-end (Loveable) com back-end (Flask)
- Resolver problemas de CORS
- Sistema completo funcionando
- Apresentar projeto final

---

## 🔗 AULA 7: Conectando Front + Back

### Início (10 min)

**O Problema: CORS**

```
CORS = Cross-Origin Resource Sharing

Problema:
Front-end (loveable.app) → API (replit.app)
❌ Navegador bloqueia por segurança

Solução:
Permitir acesso explicitamente
```

**Configurar CORS no Flask:**

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Libera TUDO (dev)

# OU específico (produção):
CORS(app, origins=[
    "https://seu-projeto.loveable.app",
    "http://localhost:3000"
])
```

**Instalar CORS:**
```bash
pip install flask-cors
```

### Meio (35 min)

**Código JavaScript no Loveable (20 min)**

```javascript
// Configuração da API
const API_URL = 'https://seu-repl.replit.app';

// ===== FUNÇÃO PRINCIPAL: Enviar Mensagem =====
async function enviarMensagemParaBot(mensagem) {
    try {
        // Fazer requisição para API
        const resposta = await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                mensagem: mensagem
            })
        });
        
        // Verificar se deu erro HTTP
        if (!resposta.ok) {
            throw new Error(`Erro HTTP: ${resposta.status}`);
        }
        
        // Converter resposta para JSON
        const dados = await resposta.json();
        
        // Retornar apenas a resposta do bot
        return dados.resposta;
        
    } catch (erro) {
        console.error('Erro ao chamar API:', erro);
        return 'Desculpe, estou com problemas técnicos no momento. Tente novamente.';
    }
}

// ===== EXEMPLO DE USO =====
// Quando usuário clicar em "Enviar"
async function aoClicarEnviar() {
    // Pegar texto do input
    const inputElement = document.getElementById('mensagemUsuario');
    const mensagemUsuario = inputElement.value;
    
    // Validar se não está vazio
    if (!mensagemUsuario.trim()) {
        alert('Digite uma mensagem!');
        return;
    }
    
    // Mostrar mensagem do usuário na tela
    adicionarMensagem('usuario', mensagemUsuario);
    
    // Limpar input
    inputElement.value = '';
    
    // Mostrar "digitando..."
    mostrarDigitando();
    
    // Buscar resposta da API
    const respostaBot = await enviarMensagemParaBot(mensagemUsuario);
    
    // Esconder "digitando..."
    esconderDigitando();
    
    // Mostrar resposta do bot
    adicionarMensagem('bot', respostaBot);
}

// ===== FUNÇÕES AUXILIARES =====
function adicionarMensagem(tipo, texto) {
    const chatContainer = document.getElementById('chatContainer');
    
    const divMensagem = document.createElement('div');
    divMensagem.className = tipo === 'usuario' ? 'mensagem-usuario' : 'mensagem-bot';
    
    const icone = tipo === 'usuario' ? '👤' : '🤖';
    divMensagem.innerHTML = `${icone} ${texto}`;
    
    chatContainer.appendChild(divMensagem);
    
    // Scroll para última mensagem
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

function mostrarDigitando() {
    const chatContainer = document.getElementById('chatContainer');
    const divDigitando = document.createElement('div');
    divDigitando.id = 'digitando';
    divDigitando.className = 'mensagem-bot';
    divDigitando.innerHTML = '🤖 digitando...';
    chatContainer.appendChild(divDigitando);
}

function esconderDigitando() {
    const divDigitando = document.getElementById('digitando');
    if (divDigitando) {
        divDigitando.remove();
    }
}
```

**Checklist de Integração:**

```
□ CORS instalado e ativado no Flask
□ API rodando no Replit (público)
□ URL da API correta no JavaScript
□ Código JavaScript adicionado no Loveable
□ Testou no console do navegador
□ Mensagens aparecem na tela
□ Erros são tratados
```

**Debugando Problemas (15 min)**

**Problema 1: CORS Error**
```
Erro no console:
"Access-Control-Allow-Origin"

Soluções:
1. Adicionar CORS(app) no Flask
2. Reiniciar servidor
3. Verificar se está antes de app.run()
```

**Problema 2: API não responde**
```
Erro: "Failed to fetch"

Verificar:
□ API está rodando no Replit?
□ URL está correta? (https:// e domínio)
□ Replit está "sempre ligado"?
□ Testar URL direto no navegador
```

**Problema 3: Resposta não aparece**
```
Verificar:
□ Console do navegador (F12)
□ Resposta tem campo "resposta"?
□ Função adicionarMensagem existe?
□ chatContainer existe no HTML?
```

**Teste Manual no Console:**
```javascript
// Abrir F12 → Console
// Testar fetch manual
fetch('https://sua-api.replit.app/chat', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({mensagem: 'teste'})
})
.then(r => r.json())
.then(d => console.log(d));
```

### Fim (5 min)

**Status Check:**
- Quantos grupos conectaram?
- Principais problemas?
- Quem precisa de ajuda?

**Para próxima aula:**
- Sistema 100% funcionando
- Testado várias vezes
- Preparar apresentação

---

## 🎤 AULA 8: Apresentações Finais

### Início (10 min)

**Instruções de Apresentação:**

```
FORMATO: 5 minutos por grupo

ESTRUTURA:
1. Demo ao vivo (2 min)
   - Abrir aplicação
   - Fazer 3-4 perguntas
   - Mostrar respostas

2. Explicação técnica (2 min)
   - Como conectou front+back
   - Como integrou IA
   - Principal desafio

3. Perguntas (1 min)
   - Professor faz 1-2 perguntas

AVALIAÇÃO: 6,0 pontos total
```

**Checklist Final:**
```
□ Front-end funcionando
□ Backend funcionando
□ Integração funcionando
□ Pelo menos 5 tipos de pergunta funcionam
□ README.md completo
□ Grupo ensaiou
□ Todos sabem explicar
```

### Meio (35 min)

**Apresentações (5 min cada)**

**Ficha de Avaliação:**

```
═══════════════════════════════════════════
AVALIAÇÃO FINAL - PROJETO COMPLETO
═══════════════════════════════════════════

GRUPO: ______________ TURMA: ______________

─────────────────────────────────────────────
1. FRONT-END (1,5 pts)
─────────────────────────────────────────────

Interface funcional (0,8):
□ Carrega sem erros (0,3)
□ Chat aparece e funciona (0,3)
□ Visual organizado (0,2)

Qualidade visual (0,7):
□ Design adequado (0,3)
□ Responsivo (0,2)
□ Mantido/melhorado do 3º bim (0,2)

SUBTOTAL: _____ / 1,5

─────────────────────────────────────────────
2. BACKEND (2,0 pts)
─────────────────────────────────────────────

API funcional (1,0):
□ Rotas funcionam (0,4)
□ Integração com Groq (0,4)
□ Tratamento de erros (0,2)

Qualidade do código (1,0):
□ Organizado e comentado (0,4)
□ Contexto bem definido (0,4)
□ Sem erros graves (0,2)

SUBTOTAL: _____ / 2,0

─────────────────────────────────────────────
3. INTEGRAÇÃO (1,5 pts)
─────────────────────────────────────────────

Funcionamento (1,0):
□ Front conecta com back (0,5)
□ Mensagens fluem corretamente (0,5)

Demo ao vivo (0,5):
□ Demonstração funciona (0,3)
□ Pelo menos 5 perguntas (0,2)

SUBTOTAL: _____ / 1,5

─────────────────────────────────────────────
4. APRESENTAÇÃO (1,0 pt)
─────────────────────────────────────────────

Explicação técnica (0,5):
□ Explicou integração (0,3)
□ Mostrou conhecimento (0,2)

Comunicação (0,5):
□ Clara e organizada (0,3)
□ Respondeu perguntas (0,2)

SUBTOTAL: _____ / 1,0

═══════════════════════════════════════════
NOTA FINAL: _____ / 6,0
═══════════════════════════════════════════

BÔNUS POSSÍVEL (+0,5):
□ Funcionalidades extras (+0,2)
□ Código excepcionalmente limpo (+0,2)
□ Apresentação profissional (+0,1)

NOTA COM BÔNUS: _____ / 6,5

PONTOS FORTES:
_________________________________________

PONTOS A MELHORAR:
_________________________________________

OBSERVAÇÕES:
_________________________________________
```

**Perguntas Sugeridas:**

```
Para todos os grupos:
- "Qual foi o maior desafio técnico?"
- "Como resolveram o problema de CORS?"
- "Por que escolheram Groq ao invés de outras IAs?"

Técnicas específicas:
- "Mostre a parte do código que conecta front+back"
- "Como funciona o contexto da IA?"
- "O que acontece se a API não responder?"
```

### Fim (5 min)

**Feedback Geral:**

```
PARABÉNS!

Vocês criaram:
✅ Front-end completo
✅ Backend com API REST
✅ Integração com IA
✅ Sistema funcionando end-to-end

ISSO É IMPRESSIONANTE! 🎉

Principais aprendizados da turma:
- _________________________________
- _________________________________
- _________________________________

Para continuar evoluindo:
- Adicionar banco de dados
- Melhorar interface
- Deploy em servidor real
- Adicionar autenticação
```

---

## 📊 Avaliação Final do Bimestre

**Total: 10,0 pontos**

| Semana | Atividade | Pontos |
|--------|-----------|--------|
| 1 | REST API - Conceitos e exercícios | 1,0 |
| 2 | Flask - API do chatbot + testes | 1,5 |
| 3 | Integração IA - Groq + contexto | 1,5 |
| 4 | Projeto Final Integrado | 6,0 |
| **TOTAL** | | **10,0** |

**Composição Semana 4 (6,0 pts):**
- Front-end: 1,5
- Backend: 2,0
- Integração: 1,5
- Apresentação: 1,0

**Bônus possível:** +0,5 (máximo 10,5 no bimestre)

---

## 📄 Template README.md Obrigatório

```markdown
# [Nome do Projeto] - Chatbot Inteligente

## 👥 Integrantes
- Nome 1 - Turma - Front-end
- Nome 2 - Turma - Backend
- Nome 3 - Turma - Integração IA
- Nome 4 - Turma - Testes/Doc

## 🎯 Objetivo
[Descrever o que o chatbot faz e para que serve]

## 🛠️ Tecnologias
**Front-end:**
- Loveable.dev
- JavaScript
- HTML/CSS

**Backend:**
- Python 3.x
- Flask
- Flask-CORS

**IA:**
- Groq API
- Modelo: mixtral-8x7b-32768

## ✨ Funcionalidades
- [x] Chat funcional
- [x] Respostas inteligentes via IA
- [x] Interface responsiva
- [x] Tratamento de erros
- [x] Contexto personalizado

## 🚀 Como Executar

### Backend
```bash
pip install flask flask-cors requests
python main.py
```

### Front-end
Acesse: [link do Loveable]

### Variáveis de Ambiente
```
GROQ_API_KEY=sua_chave_aqui
```

## 📁 Estrutura
```
/
├── backend/
│   └── main.py          # API Flask
├── frontend/
│   └── [Loveable code]
└── README.md
```

## 🎓 Aprendizados
- APIs REST e verbos HTTP
- Integração front-end + back-end
- Uso de LLMs via API
- Prompt engineering
- CORS e segurança web

## 🔮 Melhorias Futuras
- [ ] Banco de dados persistente
- [ ] Autenticação de usuários
- [ ] Histórico de conversas
- [ ] Deploy em servidor real

## 📞 Contato
- Grupo: [email ou contato]
- Professor: [nome do professor]

## 📜 Licença
Projeto educacional - Escola [nome]
```

---

## 🎓 Reflexões Finais

**Para os Alunos:**

```
VOCÊS APRENDERAM:

Conceitos:
✓ O que é API REST
✓ Verbos HTTP (GET, POST, PUT, PATCH, DELETE)
✓ Códigos de status (2xx, 4xx, 5xx)
✓ Arquitetura cliente-servidor
✓ CORS e segurança

Prática:
✓ Criar APIs com Flask
✓ Conectar front-end com back-end
✓ Integrar com IA (LLMs)
✓ Debugar problemas reais
✓ Trabalhar em equipe

Habilidades:
✓ Resolver problemas técnicos
✓ Ler documentação
✓ Testar APIs
✓ Apresentar projetos

ISSO É MUITO! 🎉
```

**Próximos Passos:**

```
1. PORTFÓLIO
   □ Adicionar no GitHub
   □ Fazer README bonito
   □ Link no LinkedIn/currículo

2. MELHORAR
   □ Estudar mais sobre APIs
   □ Aprender bancos de dados
   □ Explorar outras IAs
   □ Deploy em produção

3. PRATICAR
   □ Criar novos projetos
   □ Contribuir open source
   □ Participar de hackathons
   □ Fazer cursos avançados
```

---

## 💡 Dicas para o Futuro

**Carreira em Backend/APIs:**
- Aprender SQL (PostgreSQL, MySQL)
- Estudar autenticação (JWT, OAuth)
- Conhecer Docker
- Praticar Git/GitHub
- Ler sobre Clean Code

**Carreira em IA:**
- Entender como LLMs funcionam
- Estudar prompt engineering
- Conhecer outras APIs (OpenAI, Anthropic)
- Aprender sobre fine-tuning
- Explorar agentes autônomos

**Geral:**
- Fazer projetos pessoais
- Documentar bem o código
- Participar de comunidades
- Nunca parar de aprender

---

## 📚 Recursos Complementares

**Documentação:**
- Flask: flask.palletsprojects.com
- Groq: groq.com/docs
- REST API: restfulapi.net
- MDN Web Docs: developer.mozilla.org

**Cursos:**
- "Python para APIs" - Real Python
- "REST API Design" - Udemy
- "Prompt Engineering" - DeepLearning.AI

**Comunidades:**
- Reddit: r/flask, r/webdev
- Discord: Python Brasil
- Stack Overflow
- GitHub Discussions

---

## 📞 Pós-Apresentação

**Disponibilidade:**
- Feedback individual: agendar
- Dúvidas sobre notas: até [data]
- Mentoria de projetos: sempre

**Contato:**
- Email: [seu email]
- Horário: [definir]

---

**PARABÉNS por chegarem até aqui!** 🎊

**Vocês construíram um sistema completo do zero:**
- Interface
- Backend
- Inteligência Artificial
- Integração

**Isso não é pouca coisa.**

**Usem esse conhecimento, continuem praticando, e boa sorte nas próximas jornadas!** 🚀

**Obrigado pela dedicação de todos.** 🙏
