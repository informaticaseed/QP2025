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

Como a desigualdade de renda varia entre as diferentes regiões do Brasil e quais fatores estão mais relacionados com maior ou menor desigualdade?

### Por que isso é importante?
Entender a desigualdade de renda é crucial para formular políticas públicas que promovam a justiça social e o desenvolvimento econômico equilibrado.

### Nossas 5 Perguntas Específicas
1. Quais estados apresentam os maiores e menores índices de desigualdade de renda?
2. Existe correlação entre rendimento médio e índice de Gini por estado?
3. Como a distribuição de renda mudou no período de 2012 a 2022?
4. Quais regiões tiveram a maior redução de desigualdade no período analisado?
5. Existe relação entre concentração de renda nos 10% mais ricos e os indicadores sociais?

## 🔍 3. O Que Descobrimos

### Fatos Interessantes
1. O Distrito Federal apresenta o maior rendimento médio mensal (R$ 3.825,00), mas também um dos maiores índices de Gini (0,58), indicando alta desigualdade.
2. Identificamos uma tendência de aumento da desigualdade nos períodos de crise econômica, especialmente entre 2015-2016 e durante a pandemia em 2020.
3. Observamos que estados da região Nordeste, apesar de terem rendimento médio mais baixo, apresentaram maior redução da desigualdade no período analisado.

### Nossos Gráficos
**Gráfico 1:** Rendimento Médio x Índice de Gini
![Gráfico de Rendimento Médio x Índice de Gini](https://i.imgur.com/exemplo.png)
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