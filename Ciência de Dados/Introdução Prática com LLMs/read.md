# Aprendizado de Máquina: Uma Introdução Prática com LLMs
*Aula 1: Introdução ao Aprendizado Supervisionado*

## 🎯 Objetivos da Aula
- Entender o que é Aprendizado de Máquina
- Explorar o Aprendizado Supervisionado na prática
- Interagir com LLMs (Large Language Models)
- Criar nosso primeiro projeto de classificação

## 🤔 Motivação: Por que estudar isso?

### Exemplos do Dia a Dia
- Netflix recomendando filmes
- Spotify sugerindo músicas
- Instagram mostrando posts relevantes
- Gmail filtrando spam

### O Poder dos LLMs
- ChatGPT respondendo perguntas
- GitHub Copilot ajudando a programar
- Midjourney criando imagens
- Claude auxiliando em tarefas complexas

## 🎮 Atividade Prática 1: "Ensinando" uma IA
1. Abra o ChatGPT
2. Digite: "Vamos brincar de um jogo. Eu vou pensar em um animal e você tentará adivinhar fazendo perguntas sobre suas características. A cada resposta, explique como isso ajuda na classificação."
3. Observe como a IA aprende com cada informação

## 📚 Conceitos Fundamentais

### O que é Aprendizado Supervisionado?
- É como ensinar com exemplos
- Dados de entrada → Rótulos (respostas corretas)
- A máquina aprende padrões
- Depois pode classificar novos dados

### Analogia com Aprendizado Humano
Professor → Aluno → Prova
Dados Rotulados → Modelo → Previsões

## 💡 Atividade Prática 2: Construindo um Classificador
```python
# Exemplo simples de classificação de sentimentos
textos = [
    "Adorei o filme!",
    "Filme terrível",
    "Muito bom mesmo",
    "Não gostei nada"
]
sentimentos = ["positivo", "negativo", "positivo", "negativo"]

# Os alunos tentam criar regras para classificação
# Depois comparamos com a classificação do ChatGPT
```

## 🔨 Projeto Prático: Classificador de Textos com ChatGPT

### Passo 1: Coleta de Dados
- Cada aluno contribui com 2 frases (positiva e negativa)
- Criamos nossa base de dados colaborativa

### Passo 2: Classificação
- Usamos o ChatGPT para classificar os textos
- Comparamos com nossa classificação manual
- Discutimos as diferenças

### Passo 3: Análise
- Por que o modelo acertou/errou?
- Quais padrões ele identificou?
- Como podemos melhorar?

## 🎯 Desafio para Casa
1. Escolha um tema de seu interesse (músicas, filmes, jogos)
2. Colete 10 exemplos (5 positivos, 5 negativos)
3. Use o ChatGPT para classificá-los
4. Documente os resultados no GitHub

## 📚 Recursos Adicionais
- [Tutorial ChatGPT](https://github.com/openai/chatgpt-tutorial)
- [Markdown Guide](https://www.markdownguide.org/)
- [GitHub Pages](https://pages.github.com/)
- [Google Colab](https://colab.research.google.com/)

## 🤝 Projeto em Grupo
- Formar grupos de 3-4 alunos
- Cada grupo escolhe um tema diferente
- Criar um mini-projeto de classificação
- Apresentar resultados na próxima aula

## 💻 Dicas para Documentação
1. Use o GitHub para guardar todo material
2. Organize em pastas:
   - /aulas
   - /projetos
   - /recursos
3. Crie um README.md bonito
4. Use emojis para deixar mais visual
5. Inclua exemplos práticos

## 🌟 Próxima Aula
- Aprofundamento em técnicas de classificação
- Métricas de avaliação
- Projeto prático com dados reais