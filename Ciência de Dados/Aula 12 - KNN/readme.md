# 🏠 Aula 12: KNN (K-Nearest Neighbors) - Aprendendo com os Vizinhos

## ⏱️ Cronograma da Aula (50 min)
* **(10 min) Introdução:** O conceito de vizinhança e similaridade
* **(15 min) Demonstração:** Classificação por votação dos vizinhos
* **(20 min) Prática:** Implementação do KNN em Python
* **(5 min) Desafio:** Classificar novos pontos com KNN

## 🎯 Objetivo da Aula
Entender como o algoritmo KNN classifica novos dados com base na similaridade com exemplos conhecidos.

## 🧠 Conceito Simplificado
KNN é como perguntar a opinião das pessoas mais parecidas com você para tomar uma decisão.

## 🏙️ Analogia do Restaurante
**"Escolhendo um Restaurante"**:
- Você quer saber se vai gostar de um novo restaurante
- Pergunta a opinião de 5 amigos com gostos parecidos aos seus
- Se a maioria gostou, você provavelmente também vai gostar
- O KNN funciona assim: ele consulta os "vizinhos mais próximos" para decidir

## 💻 Vamos Praticar no Colab!

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from matplotlib.colors import ListedColormap

# DADOS: Características de frutas [peso em gramas, nível de doçura (0-10)]
frutas = np.array([
    [150, 7], [170, 8], [140, 6], [130, 7], [160, 8],  # Maçãs
    [60, 9], [80, 10], [70, 9], [50, 8], [75, 10],    # Morangos
    [250, 3], [300, 4], [280, 3], [270, 4], [260, 2]   # Abacates
])
# Rótulos das frutas: 0 = Maçã, 1 = Morango, 2 = Abacate
rotulos = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2])
nomes_frutas = ['Maçã', 'Morango', 'Abacate']

# NORMALIZAR os dados
scaler = StandardScaler()
frutas_normalizadas = scaler.fit_transform(frutas)

# VISUALIZAR os dados originais
plt.figure(figsize=(12, 8))
cores = ['red', 'green', 'blue']
for i in range(3):  # Para cada tipo de fruta
    indices = np.where(rotulos == i)
    plt.scatter(
        frutas[indices, 0], frutas[indices, 1],
        c=cores[i], label=nomes_frutas[i],
        s=100, edgecolor='k'
    )

plt.title('Características das Frutas', fontsize=16)
plt.xlabel('Peso (gramas)', fontsize=14)
plt.ylabel('Nível de Doçura (0-10)', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

# CRIAR E TREINAR o modelo KNN
k = 3  # Número de vizinhos a considerar
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(frutas_normalizadas, rotulos)

# VISUALIZAR as fronteiras de decisão
def plot_decision_boundaries(X, y, model, scaler):
    h = 0.02  # Tamanho da grade
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    
    # Escalonar os pontos da grade
    grid_points = np.c_[xx.ravel(), yy.ravel()]
    grid_points_scaled = scaler.transform(grid_points)
    
    # Prever as classes para cada ponto da grade
    Z = model.predict(grid_points_scaled)
    Z = Z.reshape(xx.shape)
    
    # Criar um mapa de cores personalizado
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
    
    # Plotar as regiões coloridas
    plt.figure(figsize=(12, 8))
    plt.contourf(xx, yy, Z, alpha=0.4, cmap=cmap_light)
    
    # Plotar os pontos de treinamento
    for i in range(3):
        indices = np.where(y == i)
        plt.scatter(
            X[indices, 0], X[indices, 1],
            c=cmap_bold.colors[i], 
            label=nomes_frutas[i],
            s=100, edgecolor='k'
        )
    
    plt.title(f'Fronteiras de Decisão do KNN (k={k})', fontsize=16)
    plt.xlabel('Peso (gramas)', fontsize=14)
    plt.ylabel('Nível de Doçura (0-10)', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.show()

# Mostrar as fronteiras de decisão
plot_decision_boundaries(frutas, rotulos, knn, scaler)

# TESTAR com uma nova fruta
nova_fruta = np.array([[200, 8]])  # Uma fruta pesando 200g com doçura 8
nova_fruta_normalizada = scaler.transform(nova_fruta)
previsao = knn.predict(nova_fruta_normalizada)
probabilidades = knn.predict_proba(nova_fruta_normalizada)

print(f"Nova fruta: Peso = 200g, Doçura = 8")
print(f"O KNN classificou como: {nomes_frutas[previsao[0]]}")
print(f"Probabilidades: Maçã: {probabilidades[0][0]:.2f}, Morango: {probabilidades[0][1]:.2f}, Abacate: {probabilidades[0][2]:.2f}")

# VISUALIZAR a nova fruta no gráfico
plt.figure(figsize=(12, 8))
for i in range(3):
    indices = np.where(rotulos == i)
    plt.scatter(
        frutas[indices, 0], frutas[indices, 1],
        c=cores[i], label=nomes_frutas[i],
        s=100, edgecolor='k'
    )

# Destacar a nova fruta
plt.scatter(
    nova_fruta[:, 0], nova_fruta[:, 1],
    c='yellow', marker='*', s=300, edgecolor='k',
    label='Nova Fruta'
)

# Mostrar os k vizinhos mais próximos
# Encontrar os índices dos k vizinhos mais próximos
vizinhos = knn.kneighbors(nova_fruta_normalizada, return_distance=False)[0]
for vizinho in vizinhos:
    plt.plot(
        [nova_fruta[0, 0], frutas[vizinho, 0]],
        [nova_fruta[0, 1], frutas[vizinho, 1]],
        'k--', alpha=0.6
    )
    plt.scatter(
        frutas[vizinho, 0], frutas[vizinho, 1],
        s=150, edgecolor='k', facecolor='none', linewidth=2
    )

plt.title('Nova Fruta e seus Vizinhos Mais Próximos', fontsize=16)
plt.xlabel('Peso (gramas)', fontsize=14)
plt.ylabel('Nível de Doçura (0-10)', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()
```

## 🧩 Como Funciona o KNN

1. **Calcula a distância** entre o novo ponto e todos os pontos conhecidos
2. **Seleciona os K vizinhos mais próximos** (com menor distância)
3. **Para classificação**: escolhe a classe mais comum entre os vizinhos
4. **Para regressão**: calcula a média dos valores dos vizinhos

## 📏 Tipos de Distância
- **Euclidiana**: reta entre dois pontos (a mais comum)
- **Manhattan**: distância seguindo apenas linhas horizontais e verticais
- **Minkowski**: generalização que inclui as duas anteriores

## 📊 Aplicações no Mundo Real
- Sistemas de recomendação ("quem gostou disto também gostou daquilo")
- Reconhecimento facial
- Diagnóstico médico baseado em casos similares
- Previsão de preços imobiliários
- Classificação de documentos

## 📝 Exercício Prático
Use o KNN para classificar filmes em "Ação", "Comédia" ou "Drama" com base em:
- Número de cenas de ação (0-10)
- Número de piadas (0-10)

```python
filmes = np.array([
    [8, 2], [9, 1], [7, 3], [9, 2], [8, 1],  # Ação
    [2, 9], [3, 8], [1, 10], [2, 8], [3, 9],  # Comédia
    [4, 2], [5, 3], [3, 1], [4, 1], [5, 2]   # Drama
])
generos = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2])
```

Perguntas:
1. Como seria classificado um filme com 6 cenas de ação e 6 piadas?
2. Como o valor de K afeta a classificação?
3. Quais são as vantagens e desvantagens do KNN?

## 💡 Vantagens do KNN
1. **Simples de entender e implementar**
2. **Não faz suposições sobre a distribuição dos dados**
3. **Pode capturar padrões complexos**
4. **Funciona bem para classificação e regressão**

## ⚠️ Limitações
- **Computacionalmente intensivo** para grandes conjuntos de dados
- **Sensível a características irrelevantes**
- **Requer normalização** das características
- **Desempenho cai em espaços de alta dimensão**

## 🎯 Aplicação no Projeto Final
Suas ideias para KNN podem incluir:
- Sistema de recomendação de filmes
- Classificação de municípios em grupos de desenvolvimento similares
- Previsão de comportamento eleitoral com base em regiões similares
- Identificação de padrões de criminalidade similares entre estados

---