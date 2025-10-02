# 🚀 2º Ano - Semana 1: Fundamentos de REST API

**Aulas 1-2:** Conceitos REST, Verbos HTTP, Códigos de Status  
**Duração:** 2 aulas (100 min)  
**Avaliação:** 1,0 ponto (atividades práticas)

---

## 🎯 Objetivos

- Entender o que é uma API REST
- Conhecer os 5 verbos HTTP principais
- Compreender códigos de status (2xx, 4xx, 5xx)
- Testar APIs públicas
- Preparar ambiente para próximas aulas

---

## 📚 AULA 1: O que é REST API?

### Início (10 min)

**Conceito Visual:**

```
API = GARÇOM DO RESTAURANTE

Você (Front-end / Cliente)
    ↓ faz pedido
Garçom (API)
    ↓ leva pedido para
Cozinha (Servidor / Banco de Dados)
    ↓ prepara
Garçom (API)
    ↓ traz de volta
Você (Front-end / Cliente)
```

**Exemplos do Dia a Dia:**
- **iFood:** App → API → Restaurante → API → App
- **Instagram:** Foto → API → Servidor → API → Amigos veem
- **WhatsApp:** Mensagem → API → Servidor → API → Destino

**REST = Regras para APIs Conversarem**

Princípios básicos:
- Cliente-Servidor separados
- Sem memória entre requisições
- Padrões consistentes

### Meio (35 min)

**Anatomia de uma Requisição REST (15 min)**

```http
VERBO + URL + CABEÇALHOS + CORPO

Exemplo real:
POST https://api.loja.com/produtos
Content-Type: application/json

{
  "nome": "Notebook",
  "preco": 3000
}
```

**Partes:**
- **POST**: O que queremos fazer (criar)
- **URL**: Onde está o recurso
- **Content-Type**: Formato dos dados (JSON)
- **Corpo**: Dados que estamos enviando

**Atividade Prática: Explorar API Pública (20 min)**

**Passo 1:** Abra no navegador:
```
https://api.github.com/users/github
```

**Passo 2:** Observe o JSON retornado

**Passo 3:** Preencha no caderno:

```
ATIVIDADE: Explorando API GitHub
Nome: ______________ Turma: ______

1. Liste 5 informações que aparecem:
   - _____________________________
   - _____________________________
   - _____________________________
   - _____________________________
   - _____________________________

2. Qual verbo HTTP foi usado?
   □ GET  □ POST  □ PUT  □ DELETE

3. Para que serve essa API?
   ________________________________

4. Teste com seu usuário:
   https://api.github.com/users/[seu_username]
   
   Funcionou? □ Sim  □ Não
   O que apareceu? ________________

VALE 0,5 PONTOS - Entregar no final
```

### Fim (5 min)

**Para Casa:**
- Instalar Python (quem não tem)
- Criar conta no Replit.com
- Trazer dúvidas na próxima aula

**Próxima aula:**
- Verbos HTTP detalhados
- Códigos de status
- Exercícios práticos

---

## 🔧 AULA 2: Verbos HTTP e Status Codes

### Início (10 min)

**Os 5 Verbos Principais:**

```
GET    → Buscar/Ler    → "Vejo cardápio"
POST   → Criar         → "Faço pedido"
PUT    → Atualizar     → "Mudo pedido completo"
PATCH  → Modificar     → "Só mudo bebida"
DELETE → Remover       → "Cancelo pedido"
```

**Comparação Simples:**

```
         | Tem Corpo? | Muda Dados? | Idempotente?
---------|------------|-------------|-------------
GET      | Não        | Não         | ✅ Sim
POST     | Sim        | Sim         | ❌ Não
PUT      | Sim        | Sim         | ✅ Sim
PATCH    | Sim        | Sim         | ✅ Geralmente
DELETE   | Não        | Sim         | ✅ Sim
```

**Idempotente = Chamar várias vezes dá mesmo resultado**

### Meio (35 min)

**Detalhando Cada Verbo (15 min)**

**1. GET - Buscar**
```http
GET /produtos           → Lista todos
GET /produtos/5         → Busca o #5
GET /produtos?cor=azul  → Filtra azuis
```
- Não altera nada
- Pode ser armazenado em cache
- Seguro de chamar várias vezes

**2. POST - Criar**
```http
POST /produtos
{
  "nome": "Mouse",
  "preco": 50
}
```
- Cria novo recurso
- Retorna geralmente 201 Created
- Cada chamada cria novo item

**3. PUT - Atualizar Completo**
```http
PUT /produtos/5
{
  "nome": "Mouse Gamer",
  "preco": 80,
  "estoque": 10
}
```
- Substitui recurso inteiro
- Precisa enviar todos os campos
- Mesma chamada = mesmo resultado

**4. PATCH - Atualizar Parcial**
```http
PATCH /produtos/5
{
  "preco": 75
}
```
- Altera só campos enviados
- Outros campos mantêm valores
- Mais eficiente que PUT

**5. DELETE - Remover**
```http
DELETE /produtos/5
```
- Remove recurso
- Retorna 204 No Content
- Chamar de novo = mesmo resultado (já foi removido)

**Códigos de Status HTTP (20 min)**

**Categorias:**
```
1xx - Informação       (raramente usado)
2xx - SUCESSO ✅
3xx - Redirecionamento
4xx - ERRO SEU ❌      (cliente errou)
5xx - ERRO DELES 💥    (servidor quebrou)
```

**Principais Códigos:**

**2xx - Deu Certo:**
```
200 OK           → Sucesso geral
201 Created      → Recurso criado
204 No Content   → Sucesso sem resposta
```

**4xx - Você Errou:**
```
400 Bad Request  → Dados inválidos/malformados
401 Unauthorized → Precisa fazer login
403 Forbidden    → Logado mas sem permissão
404 Not Found    → Recurso não existe
422 Unprocessable→ Dados válidos mas não aceitáveis
```

**5xx - Servidor Errou:**
```
500 Internal     → Erro genérico do servidor
502 Bad Gateway  → Problema no intermediário
503 Unavailable  → Servidor sobrecarregado/manutenção
```

**Exemplo Prático:**
```python
# Tratando status
import requests

resposta = requests.get('https://api.exemplo.com/user/999')

if resposta.status_code == 200:
    print("Sucesso!", resposta.json())
elif resposta.status_code == 404:
    print("Usuário não existe")
elif resposta.status_code >= 500:
    print("Servidor com problemas")
```

### Fim (5 min)

**Exercício para Entregar:**

```
EXERCÍCIO: Verbos e Status
Nome: ______________ Turma: ______

Complete a tabela:

| Ação | Verbo | URL | Status Esperado |
|------|-------|-----|-----------------|
| Listar todos produtos | GET | /produtos | 200 |
| Criar novo produto | ? | ? | ? |
| Buscar produto #10 | ? | ? | ? |
| Atualizar preço do #10 | ? | ? | ? |
| Remover produto #10 | ? | ? | ? |
| Buscar produto #999 (não existe) | ? | ? | ? |
| Criar produto sem nome | ? | ? | ? |

VALE 0,5 PONTOS - Entregar no final
```

**Gabarito para Conferir:**
```
2. POST /produtos 201
3. GET /produtos/10 200
4. PATCH /produtos/10 200
5. DELETE /produtos/10 204
6. GET /produtos/999 404
7. POST /produtos 400
```

---

## 📊 Avaliação da Semana 1

**Total: 1,0 ponto**

| Atividade | Pontos |
|-----------|--------|
| Exploração API GitHub (Aula 1) | 0,5 |
| Exercício Verbos e Status (Aula 2) | 0,5 |

**Critérios:**
- Entregou completo: nota cheia
- Entregou incompleto: proporcional
- Não entregou: 0,0

---

## 📚 Material de Apoio

### Recursos Online:

**Documentação:**
- HTTP Status: httpstatuses.com
- REST API: restfulapi.net
- HTTP Methods: developer.mozilla.org/HTTP/Methods

**Vídeos Recomendados:**
- "O que é API REST" - Código Fonte TV
- "HTTP Status Codes" - Programador BR

### Referência Rápida:

**Verbos HTTP:**
```
GET    = LER (Read)
POST   = CRIAR (Create)
PUT    = ATUALIZAR TUDO (Update)
PATCH  = ATUALIZAR PARTE (Update)
DELETE = REMOVER (Delete)
```

**Status Codes:**
```
2xx = ✅ Deu certo!
4xx = ❌ Você errou
5xx = 💥 Servidor quebrou
```

---

## 🏠 Para Casa

**Preparação para Semana 2:**

1. **Ambiente:**
   - Python instalado OU conta Replit criada
   - Testar se `python --version` funciona

2. **Revisar:**
   - Diferença entre GET e POST
   - Quando usar PUT vs PATCH
   - Principais status codes

3. **Pesquisar (Opcional):**
   - "Flask Python tutorial"
   - "Como criar API REST"
   - "Exemplos de API Python"

**Próxima Semana:**
- Criar primeira API com Flask
- Rodar código localmente
- Testar com ferramentas profissionais

---

## 💡 Dicas

**Para entender melhor:**
- APIs são como garçons: intermediam pedidos
- REST são as regras que todos seguem
- Verbos HTTP dizem O QUE fazer
- Status codes dizem O QUE aconteceu

**Erros comuns:**
- Confundir GET com POST
- Não saber quando usar PUT vs PATCH
- Não tratar códigos de erro

**Para memorizar:**
```
GET = pegar/buscar (não muda nada)
POST = postar/criar (novo recurso)
PUT = substituir tudo
PATCH = consertar/mudar parte
DELETE = deletar/remover
```

---

## 📞 Dúvidas?

**Durante a aula:**
- Levantar a mão
- Perguntar quando explicar

**Fora da aula:**
- Grupo do WhatsApp da turma
- Email: [seu email]

**Próxima semana:**
Começamos a criar nossa própria API! 🚀
