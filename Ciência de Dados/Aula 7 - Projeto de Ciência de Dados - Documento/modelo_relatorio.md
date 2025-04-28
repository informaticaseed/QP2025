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
![Gráfico de Rendimento Médio x Índice de Gini](https://images.app.goo.gl/oAjNFWcBYYnDLRoCA)
- O que mostra: Relação entre rendimento médio e índice de Gini por estado

### Problemas Encontrados
- Dados faltantes em alguns períodos para estados específicos, especialmente durante 2020, provavelmente devido à pandemia.
- Dificuldade em normalizar os valores monetários considerando a inflação ao longo do período estudado.

## 🤖 4. Nossos Algoritmos

### Primeiro Algoritmo: Análise de Correlação e Regressão Linear
**O que faz:** Entende como diferentes variáveis socioeconômicas se relacionam com o índice de Gini.
**Por que usamos:** Para identificar correlações significativas, como a correlação de 0.72 entre a proporção de pessoas com ensino superior e menor desigualdade.

### Segundo Algoritmo: Análise de Clusters (K-means)
**O que faz:** Agrupa os estados brasileiros em clusters com base em indicadores de renda e desigualdade.
**Por que usamos:** Para identificar grupos de estados com características semelhantes, como os estados do Sul e Sudeste que tendem a formar um cluster.

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