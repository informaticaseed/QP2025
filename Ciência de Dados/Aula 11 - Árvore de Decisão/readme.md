# 🌳 Aula 11: Árvores de Decisão - Tomando Decisões Passo a Passo

## ⏱️ Cronograma da Aula (50 min)
* **(10 min) Introdução:** O que são árvores de decisão
* **(15 min) Jogo:** "20 perguntas" para entender o conceito
* **(20 min) Prática:** Construindo uma árvore no Python
* **(5 min) Desafio:** Interpretar uma árvore de decisão

## 🎯 Objetivo da Aula
Entender como as árvores de decisão fazem classificações usando uma série de perguntas simples.

## 🧠 Conceito Simplificado
Uma árvore de decisão é como um fluxograma de perguntas de "sim ou não" que nos leva a uma conclusão final.

## 🎮 Analogia do Jogo de Adivinhação
**"Jogo dos 20 Perguntas"**:
- Pense em um animal
- "Ele voa?" Se sim, vou por um caminho; se não, por outro
- "Vive na água?" E assim por diante
- Após algumas perguntas, posso adivinhar o animal
- Uma árvore de decisão funciona exatamente assim!

## 💻 Vamos Praticar no Colab!

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder

# DADOS: Vamos para o parque hoje?
dados = {
    'Clima': ['Ensolarado', 'Ensolarado', 'Nublado', 'Chuvoso', 'Chuvoso', 'Chuvoso', 'Nublado', 'Ensolarado', 'Ensolarado', 'Chuvoso'],
    'Temperatura': ['Quente', 'Quente', 'Quente', 'Amena', 'Fria', 'Fria', 'Fria', 'Amena', 'Fria', 'Amena'],
    'Umidade': ['Alta', 'Alta', 'Alta', 'Alta', 'Normal', 'Normal', 'Normal', 'Alta', 'Normal', 'Normal'],
    'Vento': ['Fraco', 'Forte', 'Fraco', 'Fraco', 'Fraco', 'Forte', 'Forte', 'Fraco', 'Fraco', 'Fraco'],
    'Ir ao Parque': ['Não', 'Não', 'Sim', 'Sim', 'Sim', 'Não', 'Sim', 'Não', 'Sim', 'Sim']
}

# Criar DataFrame
df = pd.DataFrame(dados)
print("Dados originais:")
print(df)

# PREPARAR OS DADOS
# Converter categorias em números
# O computador não entende texto, então precisamos converter para números
le_clima = LabelEncoder()
le_temp = LabelEncoder()
le_umidade = LabelEncoder()
le_vento = LabelEncoder()
le_parque = LabelEncoder()

df_numerico = df.copy()
df_numerico['Clima'] = le_clima.fit_transform(df['Clima'])
df_numerico['Temperatura'] = le_temp.fit_transform(df['Temperatura'])
df_numerico['Umidade'] = le_umidade.fit_transform(df['Umidade'])
df_numerico['Vento'] = le_vento.fit_transform(df['Vento'])
df_numerico['Ir ao Parque'] = le_parque.fit_transform(df['Ir ao Parque'])

print("\nDados convertidos em números:")
print(df_numerico)

# CRIAR E TREINAR o modelo
X = df_numerico[['Clima', 'Temperatura', 'Umidade', 'Vento']]  # Características
y = df_numerico['Ir ao Parque']  # Alvo (o que queremos prever)

# Criar a árvore de decisão (limitar a profundidade para simplificar)
arvore = DecisionTreeClassifier(max_depth=3, random_state=42)
arvore.fit(X, y)  # Treinar a árvore

# VISUALIZAR a árvore de decisão
plt.figure(figsize=(20, 10))
plot_tree(
    arvore, 
    feature_names=['Clima', 'Temperatura', 'Umidade', 'Vento'],
    class_names=['Não', 'Sim'],
    filled=True,  # Colorir os nós
    rounded=True,  # Cantos arredondados
    fontsize=12
)
plt.title('Árvore de Decisão: Ir ao Parque?', fontsize=18)
plt.show()

# ANALISAR a importância das características
importancia = pd.DataFrame({
    'Característica': X.columns,
    'Importância': arvore.feature_importances_
}).sort_values('Importância', ascending=False)

print("\nImportância das características:")
print(importancia)

# PREVER novos cenários
print("\nVamos prever alguns cenários novos:")

# Cenário 1: Ensolarado, Quente, Alta umidade, Vento Fraco
novo_cenario1 = [[
    le_clima.transform(['Ensolarado'])[0],
    le_temp.transform(['Quente'])[0],
    le_umidade.transform(['Alta'])[0],
    le_vento.transform(['Fraco'])[0]
]]
previsao1 = arvore.predict(novo_cenario1)
previsao1_texto = le_parque.inverse_transform(previsao1)[0]
print(f"Cenário 1: Ensolarado, Quente, Alta umidade, Vento Fraco → {previsao1_texto}")

# Cenário 2: Nublado, Fria, Normal umidade, Vento Forte
novo_cenario2 = [[
    le_clima.transform(['Nublado'])[0],
    le_temp.transform(['Fria'])[0],
    le_umidade.transform(['Normal'])[0],
    le_vento.transform(['Forte'])[0]
]]
previsao2 = arvore.predict(novo_cenario2)
previsao2_texto = le_parque.inverse_transform(previsao2)[0]
print(f"Cenário 2: Nublado, Fria, Normal umidade, Vento Forte → {previsao2_texto}")
```

## 🔍 Como Funciona uma Árvore de Decisão

1. **Começa com todos os dados** na raiz da árvore
2. **Encontra a melhor pergunta** para dividir os dados (que separa melhor as classes)
3. **Divide os dados** em dois grupos baseados na resposta
4. **Repete o processo** para cada novo grupo
5. **Para de dividir** quando atingir critérios de parada (profundidade máxima, pureza do nó, etc.)

## 📊 Aplicações no Mundo Real
- Diagnóstico médico
- Análise de risco de crédito
- Previsão de rotatividade de clientes
- Classificação de e-mails como spam
- Recomendação de produtos

## 📝 Exercício Prático
Crie uma árvore de decisão para classificar alunos como "Aprovado" ou "Reprovado" com base em:

```python
dados_alunos = {
    'Frequencia': ['Alta', 'Alta', 'Baixa', 'Média', 'Baixa', 'Alta', 'Média', 'Baixa', 'Média', 'Média'],
    'Tarefas': ['Completas', 'Parciais', 'Nenhuma', 'Completas', 'Nenhuma', 'Completas', 'Parciais', 'Parciais', 'Parciais', 'Completas'],
    'Notas_Provas': ['Boas', 'Boas', 'Ruins', 'Boas', 'Ruins', 'Boas', 'Ruins', 'Ruins', 'Ruins', 'Boas'],
    'Aprovado': ['Sim', 'Sim', 'Não', 'Sim', 'Não', 'Sim', 'Não', 'Não', 'Não', 'Sim']
}
```

Perguntas:
1. Qual característica é mais importante para a aprovação?
2. Que perguntas a árvore faz para decidir se um aluno será aprovado?
3. Um aluno com Frequência Média, Tarefas Completas e Notas Ruins seria aprovado?

## 💡 Vantagens das Árvores de Decisão
1. **Fáceis de entender e interpretar**
2. **Não precisam de normalização de dados**
3. **Lidam bem com dados numéricos e categóricos**
4. **Podem capturar relações não-lineares**
5. **Selecionam automaticamente as características mais importantes**

## 🎯 Aplicação no Projeto Final
Suas ideias para árvores de decisão podem incluir:
- Classificar municípios em diferentes níveis de desenvolvimento
- Prever vencedores do Oscar com base em características dos filmes
- Identificar fatores determinantes para alta criminalidade
- Classificar estados em grupos de alta/média/baixa arrecadação de impostos

---
