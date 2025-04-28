# 📊 Relatório do Projeto - Ciência de Dados

## 👥 Informações do Grupo
**Turma:** 2ºC
**Grupo:** 3
**Integrantes:** Ana Silva, Bruno Santos, Carolina Oliveira, Daniel Pereira

**Link do Dataset:** [PNAD Contínua - Rendimento](https://basedosdados.org/dataset/90324ba8-9c39-4191-8a4-302f93732464)

## 📈 1. Nossos Dados

### Sobre o Dataset
- **Nome do dataset:** PNAD Contínua - Rendimento
- **Tamanho:** 27 linhas e 15 colunas
- **Período:** 2012 até 2022

### Principais Informações
- **Tipo de dados:** rendimento médio mensal, índice de Gini, distribuição de renda por percentis
- **Região coberta:** Brasil
- **Fonte original:** IBGE

## ❓ 2. Nossa Pergunta Principal

**Queremos descobrir:** Como o dinheiro é distribuído de forma diferente em cada região do Brasil?

### Por que isso é importante?
Estudar este tema nos ajuda a:
- Entender melhor as diferenças entre regiões ricas e pobres
- Ver onde precisamos de mais atenção do governo
- Descobrir o que funciona para diminuir a desigualdade

### Nossas 5 Perguntas Específicas
1. Quais são os estados mais ricos e mais pobres do Brasil?
2. Os estados mais ricos são também os mais desiguais?
3. A diferença entre ricos e pobres aumentou ou diminuiu desde 2012?
4. Qual região do Brasil melhorou mais nos últimos anos?
5. Os estados com melhor educação têm menos desigualdade?

## 🔍 3. O Que Descobrimos

### Fatos Interessantes
1. "Brasília é a cidade mais rica, mas também uma das mais desiguais"
2. "Durante a pandemia em 2020, a desigualdade aumentou em quase todo o país"
3. "No Nordeste, mesmo sendo uma região mais pobre, a desigualdade diminuiu mais que em outras regiões"

### Nossos Gráficos
**Exemplo de Gráfico:** Renda Média por Estado
![Gráfico de Rendimento Médio x Índice de Gini](graficos-PNAD-continua-rendimento-de-todas-as-fontes-2.png)
- O que mostra: Relação entre rendimento médio e índice de Gini por estado

### Problemas Encontrados
- Dados faltantes em alguns períodos para estados específicos, especialmente durante 2020, provavelmente devido à pandemia.
- Dificuldade em normalizar os valores monetários considerando a inflação ao longo do período estudado.

## 🤖 4. Nossos Algoritmos

### Primeiro Algoritmo: Classificação com Árvore de Decisão
**O que faz:** Classifica os estados em grupos de "alta", "média" ou "baixa" desigualdade
**Por que usamos:** Para responder nossa pergunta "Quais estados apresentam os maiores e menores índices de desigualdade de renda?"
**Exemplo de resultado:** 
- Alta desigualdade: Distrito Federal, São Paulo
- Média desigualdade: Minas Gerais, Goiás
- Baixa desigualdade: Santa Catarina, Rio Grande do Sul

### Segundo Algoritmo: Análise de Clusters (K-means)
**O que faz:** Agrupa os estados brasileiros que são parecidos
**Por que usamos:** Para encontrar grupos de estados com características semelhantes
**Exemplo de resultado:** Encontramos 3 grupos de estados:
- Grupo 1: Estados ricos (Sul e Sudeste)
- Grupo 2: Estados de renda média (Centro-Oeste)
- Grupo 3: Estados de menor renda (Norte e Nordeste)

## 📋 5. Próximos Passos
1. Aprofundar a análise temporal para identificar tendências e sazonalidades na desigualdade
2. Incluir mais variáveis socioeconômicas para melhorar o modelo de regressão
3. Refinar a análise de clusters e interpretar as características de cada grupo
4. Criar visualizações interativas para facilitar a apresentação dos resultados

## 👥 6. O Que Cada Um Fez
- **Ana Silva:** Fez os gráficos
- **Bruno Santos:** Organizou os dados
- **Carolina Oliveira:** Escreveu o relatório
- **Daniel Pereira:** Fez as análises

---
**Data de Entrega:** 05/05/2025
**Link do Notebook:** [Cole aqui o link do Google Colab]