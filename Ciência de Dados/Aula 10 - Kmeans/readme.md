# 🔍 Aula 10: K-means - Descobrindo Grupos Naturais nos Dados

## ⏱️ Cronograma da Aula (50 min)
* **(10 min) Introdução:** O que é agrupamento (clustering)
* **(15 min) Jogo:** Simulação do K-means com os alunos
* **(20 min) Prática:** Código e visualização
* **(5 min) Desafio:** Interpretar grupos em novos dados

## 🎯 Objetivo da Aula
Entender como o algoritmo K-means encontra grupos naturais (clusters) em dados não rotulados.

## 🧠 Conceito Simplificado
K-means é como organizar objetos em pilhas com base em sua semelhança. Cada objeto vai para a pilha cujo "representante" é mais parecido com ele.

## 🏫 Analogia da Sala de Aula
**"Formando Grupos de Trabalho"**:
1. Imagine que precisamos dividir a turma em 3 grupos
2. Escolhemos 3 alunos aleatórios como "representantes" iniciais
3. Cada aluno vai para o grupo do representante mais parecido com ele
4. Depois, cada grupo escolhe um novo representante (a média do grupo)
5. Repetimos até que os grupos estabilizem

## 💻 Vamos Praticar no Colab!

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# DADOS: Características de jogadores de videogame
# [Horas jogadas por dia, Gasto mensal em R$]
jogadores = np.array([
    [2, 15], [1.5, 10], [2.5, 20], [1, 5], [2, 12],  # Jogadores casuais
    [5, 40], [4.5, 50], [6, 45], [5.5, 35], [4, 30],  # Jogadores intermediários
    [9, 80], [8, 70], [10, 90], [8.5, 75], [9.5, 85]  # Jogadores hardcore
])

# NORMALIZAR os dados (importante para K-means!)
scaler = StandardScaler()
jogadores_normalizados = scaler.fit_transform(jogadores)

# VISUALIZAR os dados originais
plt.figure(figsize=(10, 6))
plt.scatter(jogadores[:, 0], jogadores[:, 1], s=100, c='gray')
plt.title('Jogadores de Videogame (Sem Grupos)', fontsize=16)
plt.xlabel('Horas por Dia', fontsize=14)
plt.ylabel('Gasto Mensal (R$)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.show()

# CRIAR E TREINAR o modelo K-means
# Queremos descobrir 3 grupos (k=3)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(jogadores_normalizados)

# OBTER os grupos identificados
grupos = kmeans.labels_

# VISUALIZAR os resultados
plt.figure(figsize=(12, 8))

# Cores diferentes para cada grupo
cores = ['#ff9999', '#66b3ff', '#99ff99']
nomes_grupos = ['Casuais', 'Intermediários', 'Hardcore']

for i in range(3):
    # Selecionar apenas os jogadores do grupo i
    indices_grupo = np.where(grupos == i)
    plt.scatter(
        jogadores[indices_grupo, 0], 
        jogadores[indices_grupo, 1],
        s=100, c=cores[i], label=nomes_grupos[i]
    )

# Mostrar os centróides (os "representantes" de cada grupo)
centroides = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(
    centroides[:, 0], centroides[:, 1],
    s=300, c='black', marker='X', label='Centróides'
)

plt.title('Grupos de Jogadores Identificados pelo K-means', fontsize=16)
plt.xlabel('Horas por Dia', fontsize=14)
plt.ylabel('Gasto Mensal (R$)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.show()

# ANALISAR os grupos (características médias)
print("Características médias de cada grupo:")
for i in range(3):
    indices_grupo = np.where(grupos == i)
    horas_media = jogadores[indices_grupo, 0].mean()
    gasto_medio = jogadores[indices_grupo, 1].mean()
    print(f"Grupo {i+1} ({nomes_grupos[i]}): {horas_media:.1f} horas/dia, R${gasto_medio:.2f}/mês")
```

## 🎯 Como Funciona o K-means

1. **Escolha o número K de clusters** (grupos) que você quer encontrar
2. **Selecione K pontos aleatórios** como centróides iniciais
3. **Atribua cada ponto ao centróide mais próximo**
4. **Recalcule os centróides** como a média de todos os pontos no cluster
5. **Repita os passos 3 e 4** até que os centróides não mudem mais

## 🛒 Aplicações no Mundo Real
- Segmentação de clientes para marketing personalizado
- Agrupamento de documentos por tema
- Compressão de imagens
- Identificação de padrões em dados de saúde
- Agrupamento de cidades com características semelhantes

## 📝 Exercício Prático
Use o código acima para agrupar os seguintes animais em 2 grupos, com base no seu **peso (kg)** e **velocidade (km/h)**.

```python
animais = np.array([
    [5000, 30],   # Elefante
    [100, 80],    # Guepardo
    [4000, 40],   # Rinoceronte
    [70, 70],     # Leão
    [3000, 25],   # Hipopótamo
    [60, 60],     # Lobo
])
```

Perguntas:
1. Quais grupos o K-means encontrou? Como você os descreveria?
2. Por que é importante normalizar os dados antes de usar K-means?
3. Se você mudasse para K=3, como os grupos mudariam?

## 💡 Dicas para Usar K-means
1. **Normalize seus dados** antes de aplicar K-means
2. **Escolha o K certo** usando o método do cotovelo
3. **Execute várias vezes** com sementes aleatórias diferentes
4. **Interprete os resultados** no contexto do seu problema

## 🎯 Aplicação no Projeto Final
Suas ideias de clustering podem incluir:
- Agrupar municípios com perfis semelhantes de saneamento
- Encontrar padrões de criminalidade entre estados
- Segmentar filmes por características similares
- Identificar grupos de contribuintes com comportamentos fiscais parecidos