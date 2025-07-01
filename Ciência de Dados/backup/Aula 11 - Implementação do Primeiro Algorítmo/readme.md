# Semana 5: Implementação do Primeiro Algoritmo

## Objetivos da Aula
- Revisar conceitos fundamentais de algoritmos de machine learning
- Implementar o primeiro algoritmo escolhido para o projeto
- Avaliar os resultados preliminares do modelo
- Documentar o processo de implementação e avaliação

## Agenda (90 minutos)

### 1. Revisão de Conceitos de Machine Learning (20 min)
- **Tipos de aprendizado** (supervisionado, não supervisionado, por reforço)
- **Workflow de modelagem**:
  - Preparação dos dados
  - Treinamento do modelo
  - Avaliação do modelo
  - Ajuste de hiperparâmetros
- **Métricas de avaliação** para diferentes tipos de problemas:
  - Classificação: acurácia, precisão, recall, F1-score
  - Regressão: MSE, MAE, R²
  - Clustering: silhueta, inércia, etc.
- **Validação cruzada** e sua importância

### 2. Workshop de Implementação (60 min)
Nesta parte prática, cada grupo implementará seu primeiro algoritmo com orientação do professor.

#### Roteiro de Implementação:

1. **Preparação Final dos Dados (15 min)**
   - Revisão rápida dos dados preparados na semana anterior
   - Divisão em conjuntos de treino e teste
   - Verificação final de pré-processamento

2. **Implementação do Modelo (25 min)**
   - Instanciação do modelo com parâmetros iniciais
   - Treinamento do modelo com dados de treino
   - Predição com dados de teste
   - Avaliação com métricas apropriadas

3. **Visualização e Interpretação (20 min)**
   - Visualização dos resultados (matriz de confusão, curvas ROC, etc.)
   - Interpretação do modelo (importância de features, regras de decisão, etc.)
   - Documentação dos resultados e observações iniciais

### 3. Discussão e Próximos Passos (10 min)
- **Dificuldades comuns** encontradas durante a implementação
- **Direcionamento** para otimização dos modelos
- **Preparação** para implementação do segundo algoritmo na próxima semana

## Material de Referência por Tipo de Algoritmo

### Para Algoritmos de Classificação

#### Árvore de Decisão
```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Criar e treinar o modelo
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Fazer predições
y_pred = model.predict(X_test)

# Avaliar o modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy:.4f}")
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))

# Visualizar matriz de confusão
plt.figure(figsize=(8, 6))
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.title("Matriz de Confusão")
plt.show()

# Visualizar importância das features
if hasattr(X, 'columns'):
    feature_names = X.columns
else:
    feature_names = [f"Feature {i}" for i in range(X.shape[1])]
    
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(10, 6))
plt.title("Importância das Features")
plt.bar(range(len(indices)), importances[indices], align='center')
plt.xticks(range(len(indices)), [feature_names[i] for i in indices], rotation=90)
plt.tight_layout()
plt.show()
```

#### Random Forest
```python
from sklearn.ensemble import RandomForestClassifier

# Criar e treinar o modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# O restante do código de avaliação é similar ao da Árvore de Decisão
```

#### Regressão Logística
```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score

# Criar e treinar o modelo
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# Fazer predições de probabilidade (para curva ROC)
y_pred_proba = model.predict_proba(X_test)[:, 1]
y_pred = model.predict(X_test)

# Calcular AUC e plotar curva ROC
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
auc = roc_auc_score(y_test, y_pred_proba)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f'AUC = {auc:.4f}')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('Taxa de Falsos Positivos')
plt.ylabel('Taxa de Verdadeiros Positivos')
plt.title('Curva ROC')
plt.legend()
plt.show()
```

### Para Algoritmos de Regressão

#### Regressão Linear
```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

# Criar e treinar o modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Fazer predições
y_pred = model.predict(X_test)

# Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"R²: {r2:.4f}")

# Visualizar predições vs. valores reais
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--')
plt.xlabel('Valores Reais')
plt.ylabel('Valores Previstos')
plt.title('Previsão vs. Realidade')
plt.tight_layout()
plt.show()

# Visualizar coeficientes (se houver nomes de features)
if hasattr(X, 'columns'):
    coefs = pd.DataFrame(model.coef_, index=X.columns, columns=['Coeficiente'])
    coefs.sort_values('Coeficiente', ascending=False, inplace=True)
    
    plt.figure(figsize=(10, 6))
    coefs.plot(kind='bar')
    plt.title('Coeficientes do Modelo')
    plt.tight_layout()
    plt.show()
```

#### Random Forest Regressor
```python
from sklearn.ensemble import RandomForestRegressor

# Criar e treinar o modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# O restante do código de avaliação é similar ao da Regressão Linear
```

### Para Algoritmos de Clustering

#### K-Means
```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# Encontrar número ideal de clusters (método do cotovelo)
inertia = []
silhouette_scores = []
k_range = range(2, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)
    
    # Calcular silhouette score (evitar k=1 que não tem significado para silhouette)
    if k > 1:
        labels = kmeans.labels_
        silhouette_scores.append(silhouette_score(X, labels))

# Plotar método do cotovelo
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(k_range, inertia, 'o-')
plt.xlabel('Número de Clusters')
plt.ylabel('Inércia')
plt.title('Método do Cotovelo')

plt.subplot(1, 2, 2)
plt.plot(k_range[1:], silhouette_scores, 'o-')
plt.xlabel('Número de Clusters')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Score')

plt.tight_layout()
plt.show()

# Aplicar K-Means com o número escolhido de clusters
n_clusters = 3  # Ajuste conforme seus resultados
kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
labels = kmeans.fit_predict(X)

# Adicionar labels ao dataframe original
df_with_clusters = df.copy()
df_with_clusters['Cluster'] = labels

# Visualizar clusters (para as 2 primeiras features ou PCA)
plt.figure(figsize=(10, 8))
for i in range(n_clusters):
    cluster_data = df_with_clusters[df_with_clusters['Cluster'] == i]
    plt.scatter(
        cluster_data.iloc[:, 0],  # Primeira feature
        cluster_data.iloc[:, 1],  # Segunda feature
        label=f'Cluster {i}',
        alpha=0.7
    )

plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    s=200,
    marker='X',
    c='red',
    label='Centroids'
)
plt.title('Visualização dos Clusters')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()

# Análise de características por cluster
for i in range(n_clusters):
    print(f"\nCluster {i}:")
    cluster_data = df_with_clusters[df_with_clusters['Cluster'] == i]
    print(f"Tamanho: {len(cluster_data)}")
    print(cluster_data.describe().round(2))
```

#### DBSCAN
```python
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
import numpy as np

# Encontrar valor ideal para eps (distância)
nearest_neighbors = NearestNeighbors(n_neighbors=2)
nearest_neighbors.fit(X)
distances, _ = nearest_neighbors.kneighbors(X)
distances = np.sort(distances[:, 1])

plt.figure(figsize=(10, 6))
plt.plot(distances)
plt.title('K-Distance Graph')
plt.xlabel('Data Points sorted by distance')
plt.ylabel('Epsilon (distance to 2nd nearest neighbor)')
plt.grid(True)
plt.show()

# Aplicar DBSCAN com parâmetros escolhidos
eps = 0.5  # Ajuste conforme seu gráfico K-Distance
min_samples = 5  # Ajuste conforme necessário
dbscan = DBSCAN(eps=eps, min_samples=min_samples)
labels = dbscan.fit_predict(X)

# Adicionar labels ao dataframe original
df_with_clusters = df.copy()
df_with_clusters['Cluster'] = labels

# Visualizar clusters (incluindo outliers como -1)
plt.figure(figsize=(10, 8))
unique_labels = np.unique(labels)
for label in unique_labels:
    cluster_data = df_with_clusters[df_with_clusters['Cluster'] == label]
    if label == -1:
        plt.scatter(
            cluster_data.iloc[:, 0],
            cluster_data.iloc[:, 1],
            label='Outliers',
            c='black',
            alpha=0.5,
            s=10
        )
    else:
        plt.scatter(
            cluster_data.iloc[:, 0],
            cluster_data.iloc[:, 1],
            label=f'Cluster {label}',
            alpha=0.7
        )

plt.title('Visualização dos Clusters (DBSCAN)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()

# Estatísticas dos clusters
n_clusters = len(unique_labels) - (1 if -1 in labels else 0)
n_noise = list(labels).count(-1)
print(f"Número estimado de clusters: {n_clusters}")
print(f"Número estimado de outliers: {n_noise}")

# Calcular silhouette score (ignorando outliers)
if len(unique_labels) > 1 and -1 not in labels:
    silhouette_avg = silhouette_score(X, labels)
    print(f"Silhouette Score: {silhouette_avg:.3f}")
elif len(unique_labels) > 2:  # Tem pelo menos 2 clusters + outliers
    mask = labels != -1
    silhouette_avg = silhouette_score(X[mask], labels[mask])
    print(f"Silhouette Score (ignorando outliers): {silhouette_avg:.3f}")
```

## Checklist de Implementação do Primeiro Algoritmo

1. **Preparação dos Dados**
   - [ ] Dados divididos em conjuntos de treino e teste
   - [ ] Pré-processamento adequado (normalização, codificação, etc.)
   - [ ] Verificação de balanceamento de classes (para classificação)
   - [ ] Features selecionadas adequadamente

2. **Implementação do Algoritmo**
   - [ ] Algoritmo instanciado com parâmetros iniciais
   - [ ] Modelo treinado corretamente
   - [ ] Predições realizadas
   - [ ] Métricas de avaliação calculadas

3. **Visualização e Interpretação**
   - [ ] Gráficos de avaliação apropriados
   - [ ] Interpretação dos resultados
   - [ ] Análise de importância de features (quando aplicável)
   - [ ] Identificação de pontos fortes e fracos do modelo

4. **Documentação**
   - [ ] Processo documentado passo a passo
   - [ ] Justificativa para escolhas de hiperparâmetros
   - [ ] Resultados tabulados e organizados
   - [ ] Insights iniciais sobre o desempenho do modelo

## Entregáveis para a Próxima Aula

Para a próxima aula (Semana 6), cada grupo deve preparar:

1. **Notebook contendo**:
   - Implementação completa do primeiro algoritmo
   - Avaliação detalhada e interpretação dos resultados
   - Documentação de todo o processo

2. **Planejamento para o segundo algoritmo**:
   - Como ele se diferencia do primeiro
   - Expectativas de desempenho comparativo
   - Considerações específicas para implementação

## Recursos Adicionais

1. **Implementação de Algoritmos**:
   - [Scikit-learn Examples](https://scikit-learn.org/stable/auto_examples/index.html)
   - [Hands-On Machine Learning with Scikit-Learn](https://github.com/ageron/handson-ml2)
   - [Machine Learning Mastery](https://machinelearningmastery.com/start-here/)

2. **Avaliação de Modelos**:
   - [Scikit-learn Model Evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html)
   - [Yellowbrick: Machine Learning Visualization](https://www.scikit-yb.org/en/latest/)
   - [How to Evaluate Machine Learning Models](https://machinelearningmastery.com/how-to-evaluate-machine-learning-models/)