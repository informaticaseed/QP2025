# 🎓 **Aprendizado Não Supervisionado: Descobrindo Padrões Ocultos**

## 🎮 Analogia com Jogos
Imagine que você está jogando um jogo de organizar objetos:
- **Supervisionado**: Você tem um guia mostrando onde cada objeto deve ir
- **Não Supervisionado**: Você precisa agrupar objetos parecidos sem instruções

## 🏫 Exemplos da Escola
- **Organizar a sala**: Alunos naturalmente formam grupos por afinidade
- **Cantina**: Pessoas com gostos parecidos pedem lanches similares
- **Biblioteca**: Livros são agrupados por assuntos relacionados

## 📌 **Objetivos**
- Entender o que é **Aprendizado Não Supervisionado**.
- Explorar exemplos do dia a dia.
- Implementar um **algoritmo de agrupamento (K-Means)** no Python.

---

## 🔎 **O que é Aprendizado Não Supervisionado?**
É um tipo de aprendizado de máquina onde **não existem rótulos nos dados**. O objetivo é encontrar padrões e estruturas ocultas sem orientação.

### 🧐 **Diferença para o Aprendizado Supervisionado**
| Supervisionado | Não Supervisionado |
|---------------|------------------|
| Possui rótulos (X → Y) | Não possui rótulos |
| Exemplo: classificar e-mails como spam | Exemplo: agrupar clientes por comportamento |
| Usa técnicas como Regressão e Classificação | Usa técnicas como Agrupamento e Redução de Dimensionalidade |

---

## 🏗 **Aplicações Reais do Aprendizado Não Supervisionado**
- **Netflix / Spotify**: Agrupamento de usuários com gostos parecidos.
- **Detecção de Fraudes**: Encontrar padrões suspeitos em transações bancárias.
- **Segmentação de Clientes**: Dividir clientes em grupos para campanhas de marketing.
- **Compressão de Dados**: Reduzir a dimensionalidade de imagens e textos.

---

## 🎯 **Foco da Aula: Algoritmo K-Means**
Um dos principais algoritmos de **Aprendizado Não Supervisionado** é o **K-Means**, que divide os dados em **K grupos**, tentando minimizar a distância entre os pontos dentro de cada grupo.

**Passos do K-Means:**
1. Escolher **K** (quantidade de grupos).
2. Inicializar **K centros** aleatórios.
3. Atribuir cada ponto ao centro mais próximo.
4. Atualizar os centros com base nos grupos.
5. Repetir até a convergência.

## 🎯 K-Means: O Jogo dos Centroides
Imagine que você é professor de Educação Física organizando times:
1. Escolha K capitães (centroides)
2. Cada aluno vai para o capitão mais próximo
3. Capitães se movem para o centro do seu grupo
4. Repita até todos estarem satisfeitos

---

## 🔬 **Atividade Prática: Agrupando Dados com K-Means**

### 📌 **Objetivo**
Vamos usar **K-Means** para agrupar **dados fictícios de clientes** com base em **renda e gasto anual**.

### ⚡ **Código para Google Colab**
Copie e cole no **Google Colab** para rodar diretamente.

```python
# Instalar bibliotecas necessárias (caso não estejam instaladas)
!pip install matplotlib scikit-learn pandas

# Importar bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 📌 1. Criando um conjunto de dados fictício
np.random.seed(42)
clientes = pd.DataFrame({
    'Renda Anual (mil R$)': np.random.randint(20, 150, 100),
    'Gasto Anual (mil R$)': np.random.randint(10, 100, 100)
})

# 📌 2. Normalizar os dados (importante para K-Means)
scaler = StandardScaler()
clientes_normalizado = scaler.fit_transform(clientes)

# 📌 3. Aplicar K-Means com K=3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clientes['Grupo'] = kmeans.fit_predict(clientes_normalizado)

# 📌 4. Visualizar os grupos
plt.figure(figsize=(8,6))
plt.scatter(clientes['Renda Anual (mil R$)'], clientes['Gasto Anual (mil R$)'], c=clientes['Grupo'], cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0] * scaler.scale_[0] + scaler.mean_[0], 
            kmeans.cluster_centers_[:, 1] * scaler.scale_[1] + scaler.mean_[1], 
            s=300, c='red', marker='X', label='Centros dos Clusters')
plt.xlabel("Renda Anual (mil R$)")
plt.ylabel("Gasto Anual (mil R$)")
plt.title("Segmentação de Clientes com K-Means")
plt.legend()
plt.show()
```

---

## 📊 **Discussão em Sala**
1. O que podemos observar no gráfico?
2. Se aumentarmos o número de clusters, o que acontece?
3. Como podemos usar essa técnica em problemas do mundo real?
4. Qual seria um desafio do K-Means? (Dica: Escolher **K** certo!)

---

## 🎯 **Desafio para os Alunos**
1. Mude o número de clusters **K** e veja como afeta os grupos.
2. Adicione uma nova variável, como **idade**, e refaça a análise.
3. Pesquise sobre outros métodos de agrupamento, como **DBSCAN**.

---

### **🔜 Próxima Aula**
- Como escolher o melhor número de clusters? (**Método do Cotovelo**)
- Introdução a **Redução de Dimensionalidade (PCA)**.

---