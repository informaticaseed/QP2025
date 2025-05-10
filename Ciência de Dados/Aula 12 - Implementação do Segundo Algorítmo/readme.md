# Semana 6: Implementação do Segundo Algoritmo

## Objetivos da Aula
- Revisar o progresso e os resultados do primeiro algoritmo
- Implementar o segundo algoritmo escolhido para o projeto
- Realizar uma comparação inicial entre os dois algoritmos
- Planejar a avaliação comparativa completa

## Agenda (90 minutos)

### 1. Revisão do Primeiro Algoritmo (15 min)
- **Compartilhamento de experiências** dos grupos com o primeiro algoritmo
- **Desafios comuns** enfrentados e soluções encontradas
- **Resultados preliminares** e expectativas para o segundo algoritmo
- **Boas práticas** identificadas durante a implementação

### 2. Workshop de Implementação do Segundo Algoritmo (60 min)
Durante esta atividade prática, cada grupo implementará seu segundo algoritmo com orientação do professor.

#### Roteiro de Implementação:

1. **Preparação e Contextualização (5 min)**
   - Revisão do segundo algoritmo escolhido
   - Diferenças em relação ao primeiro algoritmo
   - Expectativas específicas para este algoritmo

2. **Implementação e Treinamento (25 min)**
   - Implementação do segundo algoritmo usando os mesmos dados pré-processados
   - Configuração de hiperparâmetros iniciais
   - Treinamento do modelo

3. **Avaliação e Visualização (15 min)**
   - Cálculo das mesmas métricas usadas para o primeiro algoritmo
   - Criação de visualizações para avaliação do modelo
   - Documentação dos resultados iniciais

4. **Comparação Preliminar (15 min)**
   - Comparação lado a lado das métricas dos dois algoritmos
   - Identificação de pontos fortes e fracos de cada abordagem
   - Documentação das diferenças observadas

### 3. Planejamento da Análise Comparativa (15 min)
- **Framework para comparação sistemática** dos algoritmos
- **Considerações específicas** para cada tipo de problema
- **Próximos passos** para análise aprofundada e otimização
- **Orientações para documentação** da comparação

## Material de Apoio para Comparação de Algoritmos

### Framework para Comparação Sistemática

#### 1. Tabela Comparativa de Métricas

**Para Classificação:**

| Métrica | Algoritmo 1 | Algoritmo 2 |
|---------|------------|------------|
| Acurácia | | |
| Precisão | | |
| Recall | | |
| F1-Score | | |
| AUC-ROC | | |
| Tempo de Treinamento | | |
| Tempo de Inferência | | |

**Para Regressão:**

| Métrica | Algoritmo 1 | Algoritmo 2 |
|---------|------------|------------|
| MSE | | |
| RMSE | | |
| MAE | | |
| R² | | |
| Tempo de Treinamento | | |
| Tempo de Inferência | | |

**Para Clustering:**

| Métrica | Algoritmo 1 | Algoritmo 2 |
|---------|------------|------------|
| Silhouette Score | | |
| Inércia/Distorção | | |
| Número de Clusters | | |
| Tempo de Execução | | |
| % de Outliers | | |

#### 2. Análise Qualitativa

| Aspecto | Algoritmo 1 | Algoritmo 2 |
|---------|------------|------------|
| Interpretabilidade | | |
| Facilidade de implementação | | |
| Robustez a outliers | | |
| Capacidade de generalização | | |
| Necessidade de dados | | |
| Complexidade computacional | | |
| Facilidade de manutenção | | |

### Código de Exemplo para Comparação Visual

#### Para Algoritmos de Classificação

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, roc_curve, auc
import seaborn as sns

# Suponha que você já tenha:
# - model1, model2: os dois modelos treinados
# - X_test, y_test: conjunto de teste
# - y_pred1, y_pred2: predições dos dois modelos
# - y_prob1, y_prob2: probabilidades preditas (para ROC)

# Comparação de Matrizes de Confusão
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

cm1 = confusion_matrix(y_test, y_pred1)
cm2 = confusion_matrix(y_test, y_pred2)

sns.heatmap(cm1, annot=True, fmt="d", cmap="Blues", ax=axes[0])
axes[0].set_title(f'Matriz de Confusão - {modelo1_nome}')
axes[0].set_xlabel('Previsto')
axes[0].set_ylabel('Real')

sns.heatmap(cm2, annot=True, fmt="d", cmap="Blues", ax=axes[1])
axes[1].set_title(f'Matriz de Confusão - {modelo2_nome}')
axes[1].set_xlabel('Previsto')
axes[1].set_ylabel('Real')

plt.tight_layout()
plt.show()

# Comparação de Curvas ROC
plt.figure(figsize=(10, 8))

# ROC para o primeiro modelo
fpr1, tpr1, _ = roc_curve(y_test, y_prob1)
roc_auc1 = auc(fpr1, tpr1)
plt.plot(fpr1, tpr1, label=f'{modelo1_nome} (AUC = {roc_auc1:.3f})')

# ROC para o segundo modelo
fpr2, tpr2, _ = roc_curve(y_test, y_prob2)
roc_auc2 = auc(fpr2, tpr2)
plt.plot(fpr2, tpr2, label=f'{modelo2_nome} (AUC = {roc_auc2:.3f})')

# Linha de referência (classificador aleatório)
plt.plot([0, 1], [0, 1], 'k--')

plt.xlabel('Taxa de Falsos Positivos')
plt.ylabel('Taxa de Verdadeiros Positivos')
plt.title('Comparação de Curvas ROC')
plt.legend(loc='lower right')
plt.grid(True, alpha=0.3)
plt.show()

# Comparação de Métricas de Desempenho
metrics = {
    'Acurácia': [accuracy1, accuracy2],
    'Precisão': [precision1, precision2],
    'Recall': [recall1, recall2],
    'F1-Score': [f1_score1, f1_score2],
    'AUC-ROC': [roc_auc1, roc_auc2]
}

model_names = [modelo1_nome, modelo2_nome]
x = np.arange(len(metrics))
width = 0.35
fig, ax = plt.subplots(figsize=(12, 6))

for i, (metric, values) in enumerate(metrics.items()):
    ax.bar(x[i] - width/2, values[0], width, label=model_names[0])
    ax.bar(x[i] + width/2, values[1], width, label=model_names[1])

ax.set_ylabel('Valor')
ax.set_title('Comparação de Métricas de Desempenho')
ax.set_xticks(x)
ax.set_xticklabels(metrics.keys())
ax.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()
```

#### Para Algoritmos de Regressão

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Suponha que você já tenha:
# - model1, model2: os dois modelos treinados
# - X_test, y_test: conjunto de teste
# - y_pred1, y_pred2: predições dos dois modelos

# Comparação de Predições vs. Valores Reais
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

axes[0].scatter(y_test, y_pred1, alpha=0.7)
axes[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--')
axes[0].set_xlabel('Valores Reais')
axes[0].set_ylabel('Valores Previstos')
axes[0].set_title(f'Previsão vs. Realidade - {modelo1_nome}')

axes[1].scatter(y_test, y_pred2, alpha=0.7)
axes[1].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--')
axes[1].set_xlabel('Valores Reais')
axes[1].set_ylabel('Valores Previstos')
axes[1].set_title(f'Previsão vs. Realidade - {modelo2_nome}')

plt.tight_layout()
plt.show()

# Análise de Resíduos
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

residuals1 = y_test - y_pred1
residuals2 = y_test - y_pred2

axes[0].scatter(y_pred1, residuals1, alpha=0.7)
axes[0].axhline(y=0, color='k', linestyle='--')
axes[0].set_xlabel('Valores Previstos')
axes[0].set_ylabel('Resíduos')
axes[0].set_title(f'Análise de Resíduos - {modelo1_nome}')

axes[1].scatter(y_pred2, residuals2, alpha=0.7)
axes[1].axhline(y=0, color='k', linestyle='--')
axes[1].set_xlabel('Valores Previstos')
axes[1].set_ylabel('Resíduos')
axes[1].set_title(f'Análise de Resíduos - {modelo2_nome}')

plt.tight_layout()
plt.show()

# Histograma dos Resíduos
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

axes[0].hist(residuals1, bins=30, alpha=0.7)
axes[0].axvline(x=0, color='k', linestyle='--')
axes[0].set_xlabel('Resíduos')
axes[0].set_ylabel('Frequência')
axes[0].set_title(f'Distribuição dos Resíduos - {modelo1_nome}')

axes[1].hist(residuals2, bins=30, alpha=0.7)
axes[1].axvline(x=0, color='k', linestyle='--')
axes[1].set_xlabel('Resíduos')
axes[1].set_ylabel('Frequência')
axes[1].set_title(f'Distribuição dos Resíduos - {modelo2_nome}')

plt.tight_layout()
plt.show()

# Comparação de Métricas de Desempenho
mse1 = mean_squared_error(y_test, y_pred1)
rmse1 = np.sqrt(mse1)
mae1 = mean_absolute_error(y_test, y_pred1)
r2_1 = r2_score(y_test, y_pred1)

mse2 = mean_squared_error(y_test, y_pred2)
rmse2 = np.sqrt(mse2)
mae2 = mean_absolute_error(y_test, y_pred2)
r2_2 = r2_score(y_test, y_pred2)

metrics = {
    'MSE': [mse1, mse2],
    'RMSE': [rmse1, rmse2],
    'MAE': [mae1, mae2],
    'R²': [r2_1, r2_2]
}

model_names = [modelo1_nome, modelo2_nome]
x = np.arange(len(metrics))
width = 0.35
fig, ax = plt.subplots(figsize=(12, 6))

for i, (metric, values) in enumerate(metrics.items()):
    if metric == 'R²':  # Esta métrica é melhor quanto mais próxima de 1
        ax.bar(x[i] - width/2, values[0], width, label=model_names[0])
        ax.bar(x[i] + width/2, values[1], width, label=model_names[1])
    else:  # Estas métricas são melhores quanto menores forem
        ax.bar(x[i] - width/2, values[0], width, label=model_names[0])
        ax.bar(x[i] + width/2, values[1], width, label=model_names[1])

ax.set_ylabel('Valor')
ax.set_title('Comparação de Métricas de Desempenho')
ax.set_xticks(x)
ax.set_xticklabels(metrics.keys())
ax.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()
```

#### Para Algoritmos de Clustering

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.cm as cm

# Suponha que você já tenha:
# - model1, model2: os dois modelos de clustering
# - X: dados de entrada
# - labels1, labels2: rótulos de cluster de cada modelo

# Visualização dos Clusters (2D)
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Para o primeiro algoritmo (ex: K-Means)
for i in np.unique(labels1):
    if i == -1:  # Outliers (no caso do DBSCAN)
        axes[0].scatter(X[labels1 == i, 0], X[labels1 == i, 1], 
                       marker='x', c='k', label='Outliers', alpha=0.5)
    else:
        axes[0].scatter(X[labels1 == i, 0], X[labels1 == i, 1], 
                       label=f'Cluster {i}', alpha=0.7)
        
axes[0].set_title(f'Clusters - {modelo1_nome}')
axes[0].set_xlabel('Feature 1')
axes[0].set_ylabel('Feature 2')
axes[0].legend()

# Para o segundo algoritmo (ex: DBSCAN)
for i in np.unique(labels2):
    if i == -1:  # Outliers (no caso do DBSCAN)
        axes[1].scatter(X[labels2 == i, 0], X[labels2 == i, 1], 
                       marker='x', c='k', label='Outliers', alpha=0.5)
    else:
        axes[1].scatter(X[labels2 == i, 0], X[labels2 == i, 1], 
                       label=f'Cluster {i}', alpha=0.7)
        
axes[1].set_title(f'Clusters - {modelo2_nome}')
axes[1].set_xlabel('Feature 1')
axes[1].set_ylabel('Feature 2')
axes[1].legend()

plt.tight_layout()
plt.show()

# Comparação de Silhouette Scores (removendo outliers do DBSCAN se necessário)
plt.figure(figsize=(12, 6))

n_clusters1 = len(np.unique(labels1))
if -1 in np.unique(labels1):
    n_clusters1 -= 1
    mask1 = labels1 != -1
    silhouette_vals1 = silhouette_samples(X[mask1], labels1[mask1])
else:
    silhouette_vals1 = silhouette_samples(X, labels1)
    
n_clusters2 = len(np.unique(labels2))
if -1 in np.unique(labels2):
    n_clusters2 -= 1
    mask2 = labels2 != -1
    silhouette_vals2 = silhouette_samples(X[mask2], labels2[mask2])
else:
    silhouette_vals2 = silhouette_samples(X, labels2)

# Calcular silhouette score médio para cada algoritmo
silhouette_avg1 = np.mean(silhouette_vals1)
silhouette_avg2 = np.mean(silhouette_vals2)

# Plotar comparação de Silhouette Scores
plt.bar([modelo1_nome, modelo2_nome], [silhouette_avg1, silhouette_avg2])
plt.ylabel('Silhouette Score Médio')
plt.title('Comparação de Silhouette Scores')
plt.grid(True, alpha=0.3, axis='y')
plt.show()

# Distribuição de tamanhos de cluster
cluster_sizes1 = np.bincount(labels1[labels1 != -1] if -1 in labels1 else labels1)
cluster_sizes2 = np.bincount(labels2[labels2 != -1] if -1 in labels2 else labels2)

fig, axes = plt.subplots(1, 2, figsize=(15, 6))

axes[0].bar(range(len(cluster_sizes1)), cluster_sizes1)
axes[0].set_xlabel('Cluster')
axes[0].set_ylabel('Número de Pontos')
axes[0].set_title(f'Distribuição de Clusters - {modelo1_nome}')

axes[1].bar(range(len(cluster_sizes2)), cluster_sizes2)
axes[1].set_xlabel('Cluster')
axes[1].set_ylabel('Número de Pontos')
axes[1].set_title(f'Distribuição de Clusters - {modelo2_nome}')

plt.tight_layout()
plt.show()
```

## Checklist para Comparação dos Algoritmos

1. **Preparação para Comparação**
   - [ ] Ambos os algoritmos usam o mesmo conjunto de dados pré-processados
   - [ ] Mesmas métricas de avaliação são calculadas para os dois modelos
   - [ ] Mesmas visualizações são geradas para comparação visual direta
   - [ ] Tempo de treinamento e inferência são registrados (se relevante)

2. **Avaliação Quantitativa**
   - [ ] Tabela comparativa de métricas criada
   - [ ] Gráficos de barras/radar para comparação de métricas
   - [ ] Testes estatísticos para avaliar diferenças significativas (opcional)
   - [ ] Análise de casos específicos onde os modelos diferem mais

3. **Avaliação Qualitativa**
   - [ ] Interpretabilidade dos modelos comparada
   - [ ] Facilidade de implementação e manutenção avaliada
   - [ ] Robustez a diferentes cenários considerada
   - [ ] Escalabilidade e requisitos computacionais analisados

4. **Documentação da Comparação**
   - [ ] Descrição clara das principais diferenças entre os algoritmos
   - [ ] Justificativa para os resultados observados
   - [ ] Identificação de situações onde cada algoritmo se destaca
   - [ ] Recomendações para escolha do algoritmo mais adequado

## Entregáveis para a Próxima Aula

Para a próxima aula (Semana 7), cada grupo deve preparar:

1. **Notebook contendo**:
   - Implementação completa de ambos os algoritmos
   - Comparação detalhada entre os dois modelos
   - Avaliação crítica dos resultados
   - Documentação de todo o processo

2. **Plano de otimização**:
   - Abordagem para melhorar o desempenho dos modelos
   - Ajustes de hiperparâmetros a serem testados
   - Técnicas adicionais a serem consideradas

## Recursos Adicionais

1. **Comparação de Algoritmos**:
   - [Comparing Machine Learning Algorithms](https://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/)
   - [Scikit-learn Algorithm Comparison](https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html)
   - [How to Compare Machine Learning Algorithms](https://machinelearningmastery.com/compare-machine-learning-algorithms-python-scikit-learn/)

2. **Visualização de Comparações**:
   - [Yellowbrick: Visual Model Evaluation](https://www.scikit-yb.org/en/latest/api/model_selection/index.html)
   - [Seaborn for Statistical Visualization](https://seaborn.pydata.org/examples/index.html)
   - [Matplotlib Guide for Comparison Plots](https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html)