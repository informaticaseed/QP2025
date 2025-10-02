# 📚 2º ANO - AULA 05: REVISÃO - DIAGRAMA DE CASO DE USO

## 🎯 **Objetivo da Aula**
Compreender e aplicar conceitos de Diagrama de Caso de Uso no contexto do chatbot

**Meta:** Dominar os conceitos que estarão na prova inter

---

## ⏰ **Cronograma da Aula (50 min)**

### **0-5 min: Contextualização**
```
CONECTAR COM O PROJETO:
□ Revisar o chatbot que criaram
□ Identificar quem usa o sistema
□ Listar o que o sistema faz
□ Introduzir a linguagem técnica
```

### **5-30 min: Conceitos e Exemplos Práticos**
**Usando o próprio chatbot como exemplo:**
- O que são atores e casos de uso
- Como identificar relacionamentos
- Estrutura correta do diagrama
- Exemplos com o projeto da turma

### **30-45 min: Exercícios Práticos**
**Criar diagrama do próprio chatbot**

### **45-50 min: Simulado e Dúvidas**

---

## 🤖 **DIAGRAMA DE CASO DE USO - CONCEITOS SIMPLES**

### **1. O QUE É UM DIAGRAMA DE CASO DE USO?**

#### **Explicação Simples:**
```
É como um MAPA que mostra:
□ QUEM usa o sistema (ATORES)
□ O QUE o sistema faz (CASOS DE USO)
□ COMO eles se relacionam (LINHAS)

PENSE NO SEU CHATBOT:
- Quem conversa com ele? → ATORES
- O que ele consegue fazer? → CASOS DE USO
- Como eles se conectam? → RELACIONAMENTOS
```

#### **Exemplo Visual:**
```
    ALUNO ←→ Fazer Pergunta
              ↕
         [CHATBOT ESCOLAR]
              ↕
ADMINISTRADOR ←→ Gerenciar Respostas
```

### **2. ATORES - QUEM USA O SISTEMA?**

#### **Conceito:**
```
ATOR = Pessoa ou sistema que INTERAGE com seu chatbot

NO SEU CHATBOT ESCOLAR, os atores são:
□ ALUNO - faz perguntas, busca informações
□ ADMINISTRADOR - configura respostas, gerencia
□ SISTEMA EXTERNO - API de IA, banco de dados

ATENÇÃO: O próprio chatbot NÃO é ator!
```

#### **Como Identificar Atores:**
```
PERGUNTE:
- Quem vai USAR o sistema?
- Quem vai CONFIGURAR o sistema?
- Que OUTROS SISTEMAS vão se conectar?

EXEMPLOS CORRETOS:
✅ Estudante, Professor, Secretária
✅ Administrador do sistema
✅ API externa, Banco de dados

EXEMPLOS ERRADOS:
❌ O próprio chatbot
❌ React, Loveable (são ferramentas)
❌ Internet, computador (são recursos)
```

### **3. CASOS DE USO - O QUE O SISTEMA FAZ?**

#### **Conceito:**
```
CASO DE USO = Ação que gera VALOR para o usuário

NO SEU CHATBOT, exemplos:
□ Consultar horário de funcionamento
□ Buscar informação sobre matrícula
□ Fazer pergunta sobre disciplina
□ Gerenciar respostas do bot (admin)
□ Cadastrar nova pergunta frequente
```

#### **Como Identificar Casos de Uso:**
```
PERGUNTE:
- O que cada ator QUER FAZER no sistema?
- Que RESULTADO útil o sistema oferece?
- Que FUNCIONALIDADES são importantes?

FORMATO CORRETO:
✅ Verbo + Complemento
✅ "Consultar horário"
✅ "Enviar mensagem"
✅ "Gerenciar usuários"

FORMATO ERRADO:
❌ Muito técnico: "Executar SQL"
❌ Muito geral: "Usar sistema"
❌ Interno: "Salvar no banco"
```

### **4. RELACIONAMENTOS - COMO SE CONECTAM?**

#### **Tipos Principais:**

##### **ASSOCIAÇÃO SIMPLES (linha normal):**
```
Conecta ATOR com CASO DE USO que ele usa

Exemplo:
ALUNO ←→ Fazer Pergunta
ADMIN ←→ Gerenciar Respostas
```

##### **INCLUSÃO (<<include>>) - SEMPRE ACONTECE:**
```
Um caso de uso SEMPRE inclui outro

Exemplo no chatbot:
"Gerenciar Respostas" <<include>> "Fazer Login"
(Admin SEMPRE precisa logar antes de gerenciar)
```

##### **EXTENSÃO (<<extend>>) - PODE ACONTECER:**
```
Um caso de uso PODE estender outro

Exemplo:
"Fazer Pergunta" <<extend>> "Salvar Histórico"
(Nem toda pergunta é salva no histórico)
```

---

## 📝 **CRIANDO O DIAGRAMA DO SEU CHATBOT**

### **PASSO 1: Identificar Atores (5 min)**
```
PENSEM NO CHATBOT DO SEU GRUPO:

ATOR 1: _________________________________
O que faz: _____________________________

ATOR 2: _________________________________
O que faz: _____________________________

ATOR 3: _________________________________
O que faz: _____________________________

DICA: Normalmente são 2-4 atores principais
```

### **PASSO 2: Listar Casos de Uso (10 min)**
```
PARA CADA ATOR, liste o que ele faz:

CASOS DE USO DO ATOR 1:
□ _____________________________________
□ _____________________________________
□ _____________________________________

CASOS DE USO DO ATOR 2:
□ _____________________________________
□ _____________________________________

CASOS DE USO DO ATOR 3:
□ _____________________________________
□ _____________________________________

DICA: 2-3 casos por ator principal
```

### **PASSO 3: Desenhar o Diagrama (10 min)**
```
ESTRUTURA:

1. RETÂNGULO grande = seu sistema chatbot
2. ATORES fora do retângulo
3. CASOS DE USO dentro do retângulo (formato oval)
4. LINHAS conectando atores aos casos de uso

EXEMPLO SIMPLES:

  Aluno ────┐
           │    ┌─────────────────────────┐
           └───→│  ○ Fazer Pergunta      │
                │                        │
                │  ○ Consultar Horário   │←──┐
                │                        │   │
Admin ──────────┤  ○ Gerenciar Respostas │   │ Sistema
                │                        │   │ Externo
                │  ○ Cadastrar FAQ       │←──┘
                └─────────────────────────┘
```

---

## 🧠 **EXERCÍCIOS PRÁTICOS**

### **Exercício 1: Identificar Atores**
```
CENÁRIO: Chatbot da Biblioteca Escolar

Quem seriam os ATORES principais?
a) Apenas estudantes
b) Estudante, Bibliotecário, Sistema de Empréstimos
c) Livros e computadores
d) React e banco de dados

RESPOSTA: _____ 
JUSTIFICATIVA: _____________________________
```

### **Exercício 2: Validar Casos de Uso**
```
Para um chatbot escolar, quais são casos de uso VÁLIDOS?

□ Consultar nota do aluno
□ Configurar servidor Apache
□ Buscar informação sobre eventos
□ Programar em JavaScript
□ Fazer pergunta sobre disciplina
□ Instalar banco MySQL

CONTE quantos você marcou: _____
```

### **Exercício 3: Relacionamentos**
```
No chatbot escolar:
- Todo administrador PRECISA fazer login antes de gerenciar
- Algumas perguntas PODEM gerar relatório automático

IDENTIFIQUE os relacionamentos:
Gerenciar Respostas _______ Fazer Login
Fazer Pergunta _______ Gerar Relatório

Opções: <<include>>, <<extend>>, associação simples
```

---

## ✅ **SIMULADO DA PROVA (questões reais)**

### **Questão 1:**
```
Em um diagrama de caso de uso para um assistente virtual educacional, 
quem seriam os ATORES principais do sistema?

A) Apenas o próprio chatbot
B) Aluno, Administrador e Sistema Externo
C) Professores e coordenadores apenas
D) Banco de dados e servidor
E) React e Loveable.dev

SUA RESPOSTA: _____
```

### **Questão 2:**
```
Para um chatbot que responde dúvidas sobre horários escolares, 
qual seria um CASO DE USO válido?

A) Configurar banco de dados
B) Consultar horário de funcionamento
C) Instalar Python no servidor
D) Criar interface no Loveable
E) Programar em React

SUA RESPOSTA: _____
```

### **Questão 3:**
```
No diagrama de caso de uso de um assistente virtual, o caso "Fazer Login" 
sempre acontece antes de "Gerenciar Respostas" (apenas para administradores). 
Que tipo de relacionamento isso representa?

A) Extensão (extend)
B) Inclusão (include)
C) Herança
D) Agregação
E) Dependência simples

SUA RESPOSTA: _____
```

### **Questão 4:**
```
Ao criar um diagrama de caso de uso para seu assistente virtual educacional, 
qual critério indica que o diagrama está CORRETAMENTE estruturado?

A) Todos os casos de uso estão conectados entre si
B) Os atores estão posicionados dentro do retângulo do sistema
C) Cada ator interage com pelo menos um caso de uso dentro do sistema
D) O sistema contém apenas casos de uso técnicos (como "conectar banco")
E) Todos os elementos usam a mesma cor e formato

SUA RESPOSTA: _____
```

**GABARITO: B, B, B, C**

---

## 💡 **DICAS PARA A PROVA**

### **Lembrar Sempre:**
```
ATORES:
✅ Pessoas ou sistemas que USAM o chatbot
❌ NÃO é o próprio chatbot
❌ NÃO são ferramentas de programação

CASOS DE USO:
✅ Ações que geram VALOR para o usuário
✅ Começam com VERBO
❌ NÃO são ações técnicas internas

DIAGRAMA:
✅ Atores FORA do retângulo
✅ Casos de uso DENTRO do retângulo
✅ Linhas conectam atores aos casos
```

### **Palavras-Chave:**
```
INCLUDE = sempre acontece junto
EXTEND = pode acontecer (opcional)
ATOR = quem usa o sistema
CASO DE USO = funcionalidade valiosa
SISTEMA = o que está sendo analisado
```

### **Macetes:**
```
SE A QUESTÃO PERGUNTA "QUEM":
→ Resposta provavelmente é sobre ATORES

SE PERGUNTA "O QUE FAZ":
→ Resposta é sobre CASOS DE USO

SE PERGUNTA "SEMPRE/OBRIGATÓRIO":
→ Resposta é INCLUDE

SE PERGUNTA "OPCIONAL/PODE":
→ Resposta é EXTEND
```

---

## 📋 **CHECKLIST FINAL**

### **Para a Prova, você deve saber:**
```
CONCEITOS:
□ Diferença entre ator e caso de uso
□ O que vai dentro/fora do retângulo do sistema
□ Quando usar include vs extend
□ Como identificar um diagrama bem feito

APLICAÇÃO NO CHATBOT:
□ Quem são os atores do seu projeto
□ Quais os principais casos de uso
□ Como desenhar o diagrama básico
□ Por que certas escolhas estão corretas
```

### **Para Casa:**
```
PRATICAR:
□ Desenhar diagrama do seu chatbot
□ Explicar suas escolhas
□ Revisar os conceitos com exemplos
□ Resolver questões similares online

REVISAR:
□ Diferença entre include e extend
□ O que caracteriza um bom ator
□ Formato correto dos casos de uso
□ Estrutura visual do diagrama
```

**Vocês conhecem o chatbot na prática - agora sabem explicar tecnicamente! 🚀**

---

## 📝 **ATIVIDADE EXTRA (Opcional)**

### **Desafio: Outros Sistemas**
```
CRIEM diagramas simples para:

1. SISTEMA DE MATRÍCULA ESCOLAR
Atores: ________________
Casos de uso: ___________

2. APP DE DELIVERY DE COMIDA
Atores: ________________
Casos de uso: ___________

3. SISTEMA DE BIBLIOTECA
Atores: ________________
Casos de uso: ___________

Isso ajuda a fixar os conceitos! 💪
```